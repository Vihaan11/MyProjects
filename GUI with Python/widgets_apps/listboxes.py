from windows import dpi_awareness
import tkinter as tk
from tkinter import ttk

dpi_awareness()

root = tk.Tk()
root.geometry('600x400')
root.title("TITLE")

# Code goes here👇

top_languages = (
    "Python",
    "JavaScript",
    "Java",
    "C#",
    "C++",
    "R",
    "SQL",
    "Go",
    "Kotlin",
    "Swift")

langs = tk.StringVar(value=top_languages)
langs_select = tk.Listbox(root, listvariable=langs, height=10)
langs_select.pack()

langs_select['selectmode'] = 'extended'



root.mainloop()