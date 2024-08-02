import tkinter as tk
from tkinter import ttk

def dpi_awareness():
    try:
        from ctypes import windll
        windll.shcore.SetProcessDpiAwareness(1)
    except:
        pass

dpi_awareness()

root = tk.Tk()
root.title("TITLE")
style = ttk.Style(root)

# Code goes here👇

label = ttk.Label(root, text="Label")

print(style.element_options("Label.border"))
print(style.element_options("Label.padding"))
print(style.element_options("Label.label"))

# style.configure('Tlabel', border=)

# root.mainloop()
