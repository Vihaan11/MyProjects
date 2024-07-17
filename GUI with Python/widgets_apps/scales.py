from windows import dpi_awareness
import tkinter as tk
from tkinter import ttk

dpi_awareness()

root = tk.Tk()
root.geometry('600x400')
root.title("TITLE")

# Code goes here👇

def scale_get(event):
    print(scale.get())

scale = ttk.Scale(root, orient="horizontal", from_=0, to=10, command=scale_get)
scale.pack(fill='x')

root.mainloop()
