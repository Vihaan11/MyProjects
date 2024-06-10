from tkinter import *
from PIL import Image, ImageTk

root = Tk()

# WidthxHeight
root.geometry("733x434")

root.title("LivVyas")

# width,height
width, height = (600, 400)
# root.maxsize(1200,900)

root.minsize(750,500)

mylabel = Label(text='Welcome to PyCharm')
mylabel.pack()

image = Image.open("C://Users//vihaa//Downloads//Complete-python-3-bootcamp-completion-certificate.jpg")
photo = ImageTk.PhotoImage(image=image)

mylabel2 = Label(image=photo)
mylabel2.pack()

root.mainloop()