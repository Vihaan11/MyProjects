import tkinter as tk
from tkinter import ttk
import ttkthemes

root = tk.Tk()
root.geometry("600x400")
style = ttkthemes.ThemedStyle(root)
print(style.theme_names())

style.theme_use('aquativo')

# myheader = tk.Label(root, text="Rectangle 1", bg='green')
# myheader.pack(side='left', fill='both', expand=True)
#
# myheader2 = tk.Label(root, text="Rec", bg='black')
# myheader2.pack(side='top', fill='both', expand=True)
#
# myheader3 = tk.Label(root, text="Rectangle 2", bg='red')
# myheader3.pack(side='left', fill='both', expand=True)

myheader3 = tk.Label(root, text="Rectangle 2", bg='red')
myheader3.pack(side='left', expand=True)

root.mainloop()