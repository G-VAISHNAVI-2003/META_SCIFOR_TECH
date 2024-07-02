import tkinter as tk
from tkinter import messagebox

def online():
    name = e_name.get()

    if not name :
        messagebox.showerror("fill the name")
    else:
        messagebox.showinfo("success","well done")
root = tk.Tk()
root.title("Online form")
l_name = tk.Label(root,text="Name:")
l_name.grid(row=0,column=0,sticky='w')
e_name = tk.Entry(root)
e_name.grid(row=0, column=1)

submit_button = tk.Button(root, text="SUBMIT", command=online, bg="green")
submit_button.grid(row=5, columnspan=2, pady=10)
root.mainloop()






