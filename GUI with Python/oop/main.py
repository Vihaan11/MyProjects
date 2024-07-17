import tkinter as tk
from tkinter import ttk


def dpi_awareness():
    try:
        from ctypes import windll
        windll.shcore.SetProcessDpiAwareness(1)
    except:
        pass


dpi_awareness()

# Code goes here👇

class HelloWorld(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Hello World')

        UserInputFrame(self).pack()


class UserInputFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        self.user_input = tk.StringVar()

        label = ttk.Label(self, text="Enter your name")
        entry = ttk.Entry(self, width=20, textvariable=self.user_input)
        button = ttk.Button(self, command=self.greet)
        label.pack()
        entry.pack()
        button.pack()

    def greet(self):
        print(f"Hello, {self.user_input.get() or 'name'}!")


root = HelloWorld()
root.mainloop()

root.mainloop()
