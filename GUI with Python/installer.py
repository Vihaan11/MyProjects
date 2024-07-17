def dpi_awareness():
    try:
        from ctypes import windll
        windll.shcore.SetProcessDpiAwareness(1)
    except:
        pass

import tkinter as tk
from tkinter import ttk
from time import sleep as wait

dpi_awareness()


def starter(*args):
    def exit_confirm(*args):
        exit_warning_window = tk.Tk()
        height = exit_warning_window.winfo_screenheight()
        width = exit_warning_window.winfo_screenwidth()
        center_x = (width-300) // 2
        center_y = (height-70) // 2
        exit_warning_window.geometry(f'300x70+{center_x}+{center_y}')
        exit_warning_window.resizable(False,False)
        exit_warning_window.title("Confirmation request")

        confirm_question = ttk.Label(exit_warning_window, text="Do you want to quit the setup?")
        confirm_question.pack()

        confirm_exit_buttons_frame = ttk.Frame(exit_warning_window)
        confirm_exit_buttons_frame.pack()

        yes_button = ttk.Button(confirm_exit_buttons_frame, text="Yes",command=quit)
        yes_button.grid(row=0, column=0)

        yes_button = ttk.Button(confirm_exit_buttons_frame, text="No", state='active',command=exit_warning_window.destroy)
        yes_button.grid(row=0, column=1)

        exit_warning_window.mainloop()


    def second_screen(*args):
        global second_window_path
        first_window_intro.destroy()
        wait(.05)
        second_window_path = tk.Tk()
        height = second_window_path.winfo_screenheight()
        width = second_window_path.winfo_screenwidth()
        center_x = (width-764) // 2
        center_y = (height-350) // 2
        second_window_path.geometry(f'764x217+{center_x}+{center_y}')
        second_window_path.resizable(False,False)
        second_window_path.title("Setup Wizard")
        # Code goes here👇

        header_frame = ttk.Frame(second_window_path)
        header_frame.grid()

        header_text = ttk.Label(header_frame, text='Select Path', padding=20, font=("Arial", 20))
        header_text.pack()

        body_frame = ttk.Frame(second_window_path)
        body_frame.grid(row=1)

        body_text = ttk.Label(body_frame, text='Select Path to install in:', padding=20)
        body_text.pack()

        buttons = ttk.Frame(second_window_path)
        buttons.grid(row=2, column=1)

        Next_button = ttk.Button(buttons, text='Next >', state='active', command=second_screen)
        Next_button.grid(column=1, row=0)

        Back_button = ttk.Button(buttons, text='< Back', command=starter)
        Back_button.grid(row=0, column=0)

        second_window_path.mainloop()
        
    try:
        second_window_path.destroy()
    except:
        pass

    first_window_intro = tk.Tk()
    height = first_window_intro.winfo_screenheight()
    width = first_window_intro.winfo_screenwidth()
    center_x = (width-764) // 2
    center_y = (height-350) // 2
    first_window_intro.geometry(f'764x217+{center_x}+{center_y}')
    first_window_intro.resizable(False,False)
    first_window_intro.title("Setup Wizard")
    # Code goes here👇

    header_frame = ttk.Frame(first_window_intro)
    header_frame.grid()

    header_text = ttk.Label(header_frame, text='Welcome to LivVyas Manager setup', padding=20, font=("Arial", 20))
    header_text.pack()

    body_frame = ttk.Frame(first_window_intro)
    body_frame.grid(row=1)

    body_text = ttk.Label(body_frame, text='Setup wil guide you though the process of LivVyas Manager installation\nClick next to continue', padding=20)
    body_text.pack()

    buttons = ttk.Frame(first_window_intro)
    buttons.grid(row=2, column=1)

    Next_button = ttk.Button(buttons, text='Next >', state='active', command=second_screen)
    Next_button.grid(column=1, row=0)

    Back_button = ttk.Button(buttons, text='Quit Setup', command=exit_confirm)
    Back_button.grid(row=0, column=0)

    first_window_intro.mainloop()


starter()

# Aquativo