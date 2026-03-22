def convert_c_to_f(celsius):
    celsius = float(celsius)
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

user=input("Enter temperature in Celsius: ")
print(f"{user} Celsius is {convert_c_to_f(user)} Fahrenheit")
