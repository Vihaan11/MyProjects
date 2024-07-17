from windows import dpi_awareness
import tkinter as tk
from tkinter import ttk

dpi_awareness()

root = tk.Tk()
root.geometry('600x400')
root.title("TITLE")

# Code goes here👇

mylabel1 = ttk.Label(root, text="Hello world", padding=20)
mylabel1.pack()

ttk.Separator(root, orient='horizontal').pack(fill='x')

mylabel2 = ttk.Label(root, text="Hello world", padding=20)
mylabel2.pack()


root.mainloop()