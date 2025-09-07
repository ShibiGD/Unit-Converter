# unit_converter_gui.py
import tkinter as tk
from tkinter import ttk, messagebox

# Conversion factors relative to meters
conversion_factors = {
    "Meters": 1.0,
    "Kilometers": 1000.0,
    "Centimeters": 0.01,
    "Millimeters": 0.001,
    "Miles": 1609.34,
    "Yards": 0.9144,
    "Feet": 0.3048,
    "Inches": 0.0254,
}


def convert():
    try:
        value = float(entry_value.get())
        from_unit = combo_from.get()
        to_unit = combo_to.get()

        meters = value * conversion_factors[from_unit]
        result = meters / conversion_factors[to_unit]

        label_result.config(
            text=f"{value} {from_unit} = {result:.4f} {to_unit}"
        )
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a numeric value.")


# Create window
root = tk.Tk()
root.title("Length Unit Converter")
root.geometry("400x250")

# Input field
tk.Label(root, text="Enter value:").pack(pady=5)
entry_value = tk.Entry(root)
entry_value.pack()

# From unit dropdown
tk.Label(root, text="From:").pack(pady=5)
combo_from = ttk.Combobox(root, values=list(conversion_factors.keys()))
combo_from.current(0)
combo_from.pack()

# To unit dropdown
tk.Label(root, text="To:").pack(pady=5)
combo_to = ttk.Combobox(root, values=list(conversion_factors.keys()))
combo_to.current(1)
combo_to.pack()

# Convert button
btn_convert = tk.Button(root, text="Convert", command=convert)
btn_convert.pack(pady=10)

# Result label
label_result = tk.Label(root, text="Result will appear here", font=("Arial", 12))
label_result.pack(pady=10)

# Run program
root.mainloop()
