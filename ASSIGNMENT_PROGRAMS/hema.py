import tkinter as tk
import math

def calculate():
    try:
        result.set(eval(entry.get()))
    except:
        result.set("Error")

def sqrt():
    try:
        result.set(math.sqrt(float(entry.get())))
    except:
        result.set("Error")

def trig_func(func):  
    try:
        angle = float(entry.get())
        if func == 'sin':
            result.set(math.sin(math.radians(angle)))
        elif func == 'cos':
            result.set(math.cos(math.radians(angle)))
        elif func == 'tan':
            result.set(math.tan(math.radians(angle)))
    except:
        result.set("Error")

# Create main window
root = tk.Tk()
root.title("Scientific Calculator")

# Entry widget for input
entry = tk.Entry(root, width=30)
entry.grid(row=0, column=0, columnspan=5)

# Result label
result = tk.StringVar()
result_label = tk.Label(root, textvariable=result, width=30)
result_label.grid(row=1, column=0, columnspan=5)

# Buttons for basic arithmetic operations
buttons = [
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 3, 3),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3),
    ('0', 5, 0), ('.', 5, 1), ('+', 5, 3)
]
for (text, row, column) in buttons:
    tk.Button(root, text=text, width=5, command=lambda t=text: entry.insert(tk.END, t)).grid(row=row, column=column)

# Additional buttons for square root and trigonometric functions
tk.Button(root, text='sqrt', width=5, command=sqrt).grid(row=6, column=0)
tk.Button(root, text='sin', width=5, command=lambda: trig_func('sin')).grid(row=6, column=1)
tk.Button(root, text='cos', width=5, command=lambda: trig_func('cos')).grid(row=6, column=2)
tk.Button(root, text='tan', width=5, command=lambda: trig_func('tan')).grid(row=6, column=3)

# Button for clearing entry
tk.Button(root, text='C', width=5, command=lambda: entry.delete(0, tk.END)).grid(row=7, column=0)

# BUTTON to operate ‘=’
tk.Button(root, text='=', width=5, command=calculate).grid(row=5, column=2)

# Run the application
root.mainloop()
