import tkinter as tk
from tkinter import ttk

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

root = tk.Tk()
root.title("Greeter")

style = ttk.Style(root)

print(style.theme_names())
print(style.theme_use('xpnative'))

root.columnconfigure(0, weight=1)
# Code goes here

# tk.Label(root, text='Hi!').pack(expand=True)

name_field = ttk.Frame(root, padding=(20,10))
name_field.grid(row=0, column=0)

buttons = ttk.Frame(root, padding=(20,10))
buttons.grid(row=1, column=0)

usrname = tk.StringVar()

def greet():
    print(f"Hello, {usrname.get() or 'name'}")


mylabel = tk.Label(name_field, text="Name:")
mylabel.grid(row=0, column=0)

entry_field = ttk.Entry(name_field, width=25, textvariable=usrname)
entry_field.grid(row=0, column=1)
entry_field.focus()

greet_button = ttk.Button(buttons, text="Greet", command=greet)
greet_button.grid(row=0, column=0)

quit_button = ttk.Button(buttons, text="QUIT", command=root.destroy)
quit_button.grid(row=0, column=1)

root.mainloop()
