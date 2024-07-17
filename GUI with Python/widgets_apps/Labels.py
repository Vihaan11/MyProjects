from windows import dpi_awareness
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
# from tkinter.ttk import Button as ttkButton

dpi_awareness()

root = tk.Tk()
root.geometry('600x400')
root.resizable(False,False)
root.title("Label")

# Code goes here

InputName = tk.StringVar()

ttk.Entry(root, width=25, textvariable=InputName).pack()
# .focus())

label = tk.Label(root, textvariable=InputName, padx=20, pady=20, font=tuple(('Segoe UI', 20, 'bold')))
label.pack()
img = Image.open('C://Users//vihaa//Desktop//forfun//1003.jpg').resize((400, 200))
photo = ImageTk.PhotoImage(img)

tkimage = tk.Label(root, text="See this racing lambo 💪🫵👊👇", image=photo, padx=5, pady=5, compound='bottom')
tkimage.pack()

root.mainloop()