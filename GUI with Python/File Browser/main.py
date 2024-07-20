import os
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def refresh_func(*args):
    for folder,subfolders,files in os.walk(str(folder_path.get().replace("\\", "//"))):
        fileView.insert('1.0', files)
        root.update()


def dpi_awareness():
    try:
        from ctypes import windll
        windll.shcore.SetProcessDpiAwareness(1)
    except:
        pass

dpi_awareness()

class BrowserWindow(tk.Tk):
    def __init__(self, **kw):
        super().__init__()
        self.title("File Browser by LivVyas")
        self.geometry('700x700')

class Ribbon(ttk.Frame):
    def __init__(self, container=None, **kw):
        super().__init__(container)

        title = ttk.Label(self, text="Options")
        title.grid()


root=BrowserWindow()

main = Ribbon(root)
main.grid(row=0, column=0)

cut_button = ttk.Button(main, text="Cut")
copy_button = ttk.Button(main, text="Copy")
paste_button = ttk.Button(main, text="Paste")
rf_button = ttk.Button(main, text="Refresh", command=refresh_func)

cut_button.grid(row=1, column=0)
copy_button.grid(row=1, column=1)
paste_button.grid(row=1, column=2)
rf_button.grid(row=1, column=3)

PathView = ttk.Frame(root)
PathView.grid(row=1,column=0)

PathTitle = ttk.Label(PathView, text="Path: ")
PathTitle.grid(row=1,column=0)

folder_path = tk.StringVar()
folder_viewpath = ttk.Entry(PathView, textvariable=tk.StringVar, width=80)
folder_viewpath.grid(row=1, column=1)

fileView = tk.Text(root, height=8, state="normal")
fileView.grid()

root.mainloop()