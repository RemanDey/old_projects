import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from datetime import datetime
import csv
import os

from matplotlib.backends.backend_pdf import PdfPages

FILENAME = "jee_progress.csv"
subjects = ["Physics", "Chemistry", "Mathematics"]
data = {subj: [] for subj in subjects}

def load_data():
    if os.path.exists(FILENAME):
        with open(FILENAME, mode="r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                add_row_to_data(row["subject"], row["date"], int(row["correct_questions"]), float(row["time_taken"]), update_csv=False)

def save_all_data():
    with open(FILENAME, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["subject", "date", "correct_questions", "time_taken"])
        for subject in data:
            for date, coeff, correct, time in data[subject]:
                writer.writerow([subject, date.strftime("%Y-%m-%d"), correct, time])

def add_row_to_data(subject, date_str, correct, time, update_csv=True):
    date = datetime.strptime(date_str, "%Y-%m-%d")
    coefficient = correct / time
    data[subject].append((date, coefficient, correct, time))
    tree.insert('', 'end', values=(subject, date.strftime("%Y-%m-%d"), correct, time, round(coefficient, 3)))
    if update_csv:
        save_all_data()

def add_entry():
    subject = subject_var.get()
    date_str = date_entry.get()
    correct = correct_entry.get()
    time = time_entry.get()
    try:
        date = datetime.strptime(date_str, "%Y-%m-%d")
        correct = int(correct)
        time = float(time)
        if time <= 0:
            raise ValueError("Time must be positive.")
        add_row_to_data(subject, date_str, correct, time)
        messagebox.showinfo("Success", f"Entry added for {subject} on {date_str}")
    except ValueError as e:
        messagebox.showerror("Error", f"Invalid input: {e}")

def delete_entry():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Select Entry", "Please select a row to delete.")
        return
    for item in selected:
        values = tree.item(item)["values"]
        subject, date_str, correct, time, _ = values
        date = datetime.strptime(date_str, "%Y-%m-%d")
        data[subject] = [entry for entry in data[subject] if not (entry[0] == date and entry[2] == int(correct) and entry[3] == float(time))]
        tree.delete(item)
    save_all_data()
    messagebox.showinfo("Deleted", "Selected entry deleted.")

def edit_entry():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Select Entry", "Please select a row to edit.")
        return
    item = selected[0]
    values = tree.item(item)["values"]
    subject, date_str, correct, time, _ = values
    edit_window = tk.Toplevel(root)
    edit_window.title("Edit Entry")

    def apply_edit():
        new_subject = edit_subject_var.get()
        new_date_str = edit_date_entry.get()
        new_correct = int(edit_correct_entry.get())
        new_time = float(edit_time_entry.get())
        new_date = datetime.strptime(new_date_str, "%Y-%m-%d")
        new_coeff = new_correct / new_time

        # Delete old
        old_date = datetime.strptime(date_str, "%Y-%m-%d")
        data[subject] = [entry for entry in data[subject] if not (entry[0] == old_date and entry[2] == int(correct) and entry[3] == float(time))]

        # Add new
        data[new_subject].append((new_date, new_coeff, new_correct, new_time))
        save_all_data()

        tree.item(item, values=(new_subject, new_date_str, new_correct, new_time, round(new_coeff, 3)))
        edit_window.destroy()
        messagebox.showinfo("Updated", "Entry updated successfully.")

    # Edit window layout
    ttk.Label(edit_window, text="Subject:").grid(row=0, column=0)
    edit_subject_var = tk.StringVar(value=subject)
    ttk.Combobox(edit_window, textvariable=edit_subject_var, values=subjects, state="readonly").grid(row=0, column=1)

    ttk.Label(edit_window, text="Date (YYYY-MM-DD):").grid(row=1, column=0)
    edit_date_entry = ttk.Entry(edit_window)
    edit_date_entry.insert(0, date_str or datetime.now().strftime("%Y-%m-%d"))
    edit_date_entry.grid(row=1, column=1)

    ttk.Label(edit_window, text="Correct Questions:").grid(row=2, column=0)
    edit_correct_entry = ttk.Entry(edit_window)
    edit_correct_entry.insert(0, correct)
    edit_correct_entry.grid(row=2, column=1)

    ttk.Label(edit_window, text="Time Taken:").grid(row=3, column=0)
    edit_time_entry = ttk.Entry(edit_window)
    edit_time_entry.insert(0, time)
    edit_time_entry.grid(row=3, column=1)

    ttk.Button(edit_window, text="Apply Changes", command=apply_edit).grid(row=4, column=0, columnspan=2, pady=10)

def plot_graph(show=True, save=False):
    plt.figure(figsize=(10, 6))
    for subject, entries in data.items():
        if entries:
            entries.sort()
            dates = [entry[0] for entry in entries]
            coeffs = [entry[1] for entry in entries]
            plt.plot(dates, coeffs, marker='o', label=subject)
    plt.title("JEE Advanced Success Coefficient Over Time")
    plt.xlabel("Date")
    plt.ylabel("Success Coefficient (Correct Questions / Time)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    if save:
        with PdfPages("jee_progress_graph.pdf") as pdf:
            pdf.savefig()
            messagebox.showinfo("Exported", "Graph successfully exported as PDF.")
    if show:
        plt.show()
#Stats
def show_stats():
    stats_window = tk.Toplevel(root)
    stats_window.title("Preparation Stats")

    row_idx = 0
    for subject in subjects + ["Overall"]:
        if subject == "Overall":
            entries = sum(data.values(), [])
        else:
            entries = data[subject]

        if not entries:
            continue

        total_qs = sum(e[2] for e in entries)
        total_time = sum(e[3] for e in entries)
        avg_coeff = total_qs / total_time if total_time > 0 else 0
        best_entry = max(entries, key=lambda x: x[1])
        best_coeff = best_entry[1]
        best_date = best_entry[0].strftime("%Y-%m-%d")
        count = len(entries)

        ttk.Label(stats_window, text=f"📚 {subject}").grid(row=row_idx, column=0, sticky="w", pady=(10, 0))
        row_idx += 1
        ttk.Label(stats_window, text=f"  • Total Questions: {total_qs}").grid(row=row_idx, column=0, sticky="w")
        row_idx += 1
        ttk.Label(stats_window, text=f"  • Total Time: {round(total_time, 2)} mins").grid(row=row_idx, column=0, sticky="w")
        row_idx += 1
        ttk.Label(stats_window, text=f"  • Avg Success Coefficient: {avg_coeff:.3f}").grid(row=row_idx, column=0, sticky="w")
        row_idx += 1
        ttk.Label(stats_window, text=f"  • Best Coefficient: {best_coeff:.3f} on {best_date}").grid(row=row_idx, column=0, sticky="w")
        row_idx += 1
        ttk.Label(stats_window, text=f"  • Entries: {count}").grid(row=row_idx, column=0, sticky="w")
        row_idx += 1

# GUI Setup
root = tk.Tk()
root.title("JEE Advanced Progress Tracker")

# Entry fields
ttk.Label(root, text="Subject:").grid(row=0, column=0)
subject_var = tk.StringVar(value=subjects[0])
ttk.Combobox(root, textvariable=subject_var, values=subjects, state="readonly").grid(row=0, column=1)

ttk.Label(root, text="Date (YYYY-MM-DD):").grid(row=1, column=0)
date_entry = ttk.Entry(root)
date_entry.insert(0, datetime.now().strftime("%Y-%m-%d"))  # autofill today's date
date_entry.grid(row=1, column=1)

ttk.Label(root, text="Correct Questions:").grid(row=2, column=0)
correct_entry = ttk.Entry(root)
correct_entry.grid(row=2, column=1)

ttk.Label(root, text="Time Taken (minutes):").grid(row=3, column=0)
time_entry = ttk.Entry(root)
time_entry.grid(row=3, column=1)

ttk.Button(root, text="Add Entry", command=add_entry).grid(row=4, column=0, columnspan=2, pady=5)
ttk.Button(root, text="Edit Selected", command=edit_entry).grid(row=5, column=0, columnspan=2, pady=2)
ttk.Button(root, text="Delete Selected", command=delete_entry).grid(row=6, column=0, columnspan=2, pady=2)
ttk.Button(root, text="Plot Graph", command=lambda: plot_graph(show=True)).grid(row=7, column=0, columnspan=2, pady=2)
ttk.Button(root, text="Export Graph as PDF", command=lambda: plot_graph(show=False, save=True)).grid(row=8, column=0, columnspan=2, pady=2)
ttk.Button(root, text="Show Stats", command=show_stats).grid(row=9, column=0, columnspan=2, pady=(5, 10))


# Table view
ttk.Label(root, text="Past Entries:").grid(row=9, column=0, columnspan=2, pady=(10, 5))
columns = ("Subject", "Date", "Correct Questions", "Time Taken", "Success Coefficient")
tree = ttk.Treeview(root, columns=columns, show="headings", height=10)
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, anchor='center', width=130)
tree.grid(row=10, column=0, columnspan=2, padx=10)

scrollbar = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
scrollbar.grid(row=10, column=2, sticky='ns')
tree.configure(yscrollcommand=scrollbar.set)

load_data()
root.mainloop()
