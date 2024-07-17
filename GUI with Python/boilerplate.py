import tkinter as tk
from tkinter import ttk
import ttkthemes

def dpi_awareness():
    try:
        from ctypes import windll
        windll.shcore.SetProcessDpiAwareness(1)
    except:
        pass

dpi_awareness()

root = tk.Tk()
style = ttkthemes.ThemedStyle(root)
style.theme_use('aquativo')
height = root.winfo_screenheight()
width = root.winfo_screenwidth()
center_x = (width-600) // 2
center_y = (height-400) // 2
root.geometry(f'600x300+{center_x}+{center_y}')
# root.resizable(False,False)
root.title("TITLE")

# Code goes here👇



root.mainloop()
