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
# height = root.winfo_screenheight()
# width = root.winfo_screenwidth()
# center_x = (width-600) // 2
# center_y = (height-400) // 2
# root.geometry(f'600x300+{center_x}+{center_y}')
root.title("TITLE")

# Code goes here👇



root.mainloop()
