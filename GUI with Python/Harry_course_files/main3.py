from tkinter import *

root = Tk()
root.geometry("600x400")
root.minsize(width=600, height=400)
# root.maxsize(width=1420, height=580)
root.title("LivVyas Manager App")

f1 = Frame(root, bg='grey', borderwidth=5, relief='sunken')
f1.pack(side='left', fill='y')

f2 = Frame(root, borderwidth=5, bg='grey', relief='sunken')
f2.pack(side='top', fill='x')

l1 = Label(f1, text="Project PyCharm")
l1.pack(pady=140)

l1 = Label(f2, text="Welcome to sublime text", font="calibri 20 bold", fg="#ff00ea")
l1.pack()

root.mainloop()
