from windows import dpi_awareness
import tkinter as tk
from tkinter import ttk

dpi_awareness()

root = tk.Tk()
root.geometry('600x400')
root.title("TITLE")

# Code goes here👇

selected_value = tk.StringVar()

my_dropdown = ttk.Combobox(root, textvariable=selected_value, values=("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"), state='readonly')
my_dropdown.pack()


def handler(event):
    print(f"Today is {selected_value.get()}")
    print("But we are going to change that to friday")
    selected_value.set("Friday")
    print(my_dropdown.get())


my_dropdown.bind('<<ComboboxSelected>>', handler)

root.mainloop()

print(f"\n{selected_value.get()} was selected")