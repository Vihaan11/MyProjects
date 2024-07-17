import tkinter as tk
from tkinter import ttk

def dpi_awareness():
    try:
        from ctypes import windll
        windll.shcore.SetProcessDpiAwareness(1)
    except:
        pass

dpi_awareness()

class Installer_Window(tk.Tk):
    def __init__(self, title, height, width):
        super().__init__()
        self.geometry(f'{width}x{height}')

        center_x = (self.winfo_screenwidth() - (width+100)) // 2
        center_y = (self.winfo_screenheight() - height) // 2
        self.geometry(f'{width}x{height}+{int(center_x)}+{int(center_y)}')

        self.resizable(False,False)
        self.title(title)
        # Code goes here👇


    def config(self, **kwargs):
        def exit_confirm(*args):
            exit_warning_window = tk.Tk()
            center_x = (exit_warning_window.winfo_screenwidth() - 300) / 2
            center_y = (exit_warning_window.winfo_screenheight() - 70) / 2
            exit_warning_window.geometry(f'300x70+{int(center_x)}+{int(center_y)}')
            exit_warning_window.resizable(False, False)
            exit_warning_window.title("Confirmation request")

            confirm_question = ttk.Label(exit_warning_window, text="Do you want to quit the setup?")
            confirm_question.pack()

            confirm_exit_buttons_frame = ttk.Frame(exit_warning_window)
            confirm_exit_buttons_frame.pack()

            yes_button = ttk.Button(confirm_exit_buttons_frame, text="Yes", command=quit)
            yes_button.grid(row=0, column=0)

            yes_button = ttk.Button(confirm_exit_buttons_frame, text="No", state='active',
                                    command=exit_warning_window.destroy)
            yes_button.grid(row=0, column=1)

            exit_warning_window.mainloop()

        header_frame = ttk.Frame(self)
        header_frame.grid()

        header_text = ttk.Label(header_frame, text=kwargs['header_line'], padding=20, font=("System Bold", 20))
        header_text.pack()

        body_frame = ttk.Frame(self)
        body_frame.grid(row=1)

        body_text = ttk.Label(body_frame, text=kwargs['body_line'], padding=20)
        body_text.pack()

        buttons = ttk.Frame(self)
        buttons.grid(row=2, column=1)

        Next_button = ttk.Button(buttons, text=kwargs['next_button'], state='active', command=kwargs['next_button_func'])
        Next_button.grid(column=1, row=0)

        Back_button = ttk.Button(buttons, text=kwargs['back_button'], command=exit_confirm)
        Back_button.grid(row=0, column=0)


def myfunc():
    print("Hello, World")

root = Installer_Window("Setup Wizard", 300, 700)
root.config(header_line="Welcome to setup", body_line="Click next to continue", next_button="next", back_button='back', next_button_func=myfunc)
root.mainloop()