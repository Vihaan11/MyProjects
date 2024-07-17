import tkinter as tk
from tkinter import ttk

project = 'EXAMPLE'

root = tk.Tk()
root.geometry('800x500')


def get_width():
    root.update()
    return root.winfo_width()


left_menu = tk.Frame(root, bg='orange')
left_menu.pack(side='left', fill='y', expand=False)

mylabel = tk.Label(left_menu, text=f"Files in Project {project}", bg='orange')
mylabel.pack(side='top')

button = ttk.Button(left_menu, text="destroy", command=mylabel.destroy)
button.pack(side='bottom', padx=40, pady=20)

editor_frame = tk.Frame(root)
editor_frame.pack(side='left', fill='x', expand=False)  # Use 'x' for horizontal fill

editor = tk.Text(editor_frame, height=20, font='Calibri 15 italic')
editor.grid(row=0, column=0, sticky='nsew')  # Use sticky for resizing

text_scrollbar = ttk.Scrollbar(editor_frame, orient='vertical', command=editor.yview)
text_scrollbar.grid(row=0, column=1, sticky='ns')
editor['yscrollcommand'] = text_scrollbar.set


def on_resize(event):
    # Your function to be executed on resize
    if event.widget == root:  # Check if event is from the root window
        # Calculate adjusted width for editor
        adjusted_width = int(get_width()) - left_menu.winfo_width() - text_scrollbar.winfo_width() - 50

        if adjusted_width > 0:  # Prevent negative width
            editor['width'] = adjusted_width
        else:
            editor['width'] = 100  # Set a minimum width

        editor_frame.update()
        root.update()


root.bind("<Configure>", on_resize)

root.mainloop()
