from windows import dpi_awareness
import tkinter as tk
from tkinter import ttk

dpi_awareness()

root = tk.Tk()
root.geometry('600x400')
root.title("TITLE")

# Code goes here👇
option = tk.StringVar()

def get_selection():
    print(option.get())

mylabel = tk.Label(root, text="My Label", fg='red')

checkbox1 = ttk.Checkbutton(
    root,
    text="Option Checkbox",
    variable=option,
    command=get_selection,
    onvalue="ON",
    offvalue="OFF"

)

storage_var = tk.StringVar()

myradio=ttk.Radiobutton(
    root,
    text="Option 1",
    variable=storage_var,
    value="opt1"
)

myradio2=ttk.Radiobutton(
    root,
    text="Option 2",
    variable=storage_var,
    value="opt2"
)

myradio3=ttk.Radiobutton(
    root,
    text="Option 3",
    variable=storage_var,
    value="opt3"
)


mylabel.grid(row=0, column=0, sticky='ew')
checkbox1.grid(row=1, column=0, sticky='ew')
tk.Label(root, text="").grid(row=2, column=0, sticky='ew')
myradio.grid(row=3, column=0, sticky='ew')
myradio2.grid(row=4, column=0, sticky='ew')
myradio3.grid(row=5, column=0, sticky='ew')


root.mainloop()