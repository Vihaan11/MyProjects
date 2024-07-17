# from windows import dpi_awareness
import tkinter as tk
from tkinter import ttk
import ttkthemes
# from PIL import ImageTk, Image
# from tkinter.ttk import Button as ttkButton

# dpi_awareness()

root = tk.Tk()
root.geometry('600x400')
root.resizable(False,False)
root.title("Text")
root.grid_columnconfigure(0,weight=1)
root.grid_rowconfigure(0,weight=1)

style = ttkthemes.ThemedStyle(root)
print(style.theme_names())

style.theme_use('aquativo')

# Code goes here

text = tk.Text(root, height=200)
text.grid(row=0, column=0, sticky='ew')

def printer():
    print(text.get('1.0', 'end'))

# button1 = ttk.Button(root, text="Print in console", state='normal', command=printer)
# button1.pack()
#
# button2 = ttk.Button(root, text="QUIT", state='normal', command=root.destroy)
# button2.pack()

text.insert('1.0', "Please enter a comment...")

text_scrollbar = ttk.Scrollbar(root, orient='vertical', command=text.yview)
text_scrollbar.grid(row=0, column=1, sticky='ns')
text['yscrollcommand'] = text_scrollbar.set

# text_scrollbar2 = ttk.Scrollbar(root, orient='horizontal', command=text.xview)
# text_scrollbar2.grid(row=1, column=0, sticky='ew')
# text['xscrollcommand'] = text_scrollbar2.set

root.mainloop()