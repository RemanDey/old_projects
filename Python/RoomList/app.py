from flask import Flask, jsonify, request, render_template, redirect, url_for
import json
import threading
import os

app = Flask(__name__, static_folder="static", template_folder="templates")
DATA_FILE = os.path.join(os.path.dirname(__file__), "status.json")
lock = threading.Lock()

# utility functions
def read_data():
    with lock:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)

def write_data(data):
    with lock:
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

def total_present(data):
    return sum(1 for p in data["people"].values() if p.get("present"))

# routes
@app.route("/")
def dashboard():
    # frontend will fetch the API, but pass names for links
    names = list(read_data()["people"].keys())
    return render_template("dashboard.html", names=names)

@app.route("/update/<name>")
def update_page(name):
    data = read_data()
    if name not in data["people"]:
        return "User not found", 404
    return render_template("update.html", name=name)

# API: get all statuses
@app.route("/api/status", methods=["GET"])
def api_status():
    data = read_data()
    data_copy = data.copy()
    data_copy["total_present"] = total_present(data)
    return jsonify(data_copy)

# API: get single user's status
@app.route("/api/status/<name>", methods=["GET"])
def api_status_user(name):
    data = read_data()
    person = data["people"].get(name)
    if person is None:
        return jsonify({"error": "not found"}), 404
    return jsonify({"name": name, "present": bool(person.get("present", False)), "note": person.get("note", "")})

# API: update a user's status
@app.route("/api/update", methods=["POST"])
def api_update():
    payload = request.get_json(force=True)
    name = payload.get("name")
    present = payload.get("present")
    note = payload.get("note", "")

    if not name:
        return jsonify({"error": "missing name"}), 400

    data = read_data()
    if name not in data["people"]:
        return jsonify({"error": "user not found"}), 404

    # sanitize/normalize
    data["people"][name]["present"] = bool(present)
    data["people"][name]["note"] = str(note)[:1000]  # limit note length a bit

    write_data(data)
    return jsonify({"ok": True, "total_present": total_present(data)})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
