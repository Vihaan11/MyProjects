from windows import dpi_awareness
import tkinter as tk
from tkinter import ttk

dpi_awareness()

root = tk.Tk()
root.geometry('600x400')
root.title("TITLE")

# Code goes here👇

initial_value = tk.StringVar(value=20)
spin_box = ttk.Spinbox(
    root,
    values=(0,5,10,15,20,25,30,35,40,45),
    textvariable=initial_value,
    wrap=True
)
spin_box.pack()

root.mainloop()