from windows import dpi_awareness
import tkinter as tk
from tkinter import ttk
import tkinter.font as font

dpi_awareness()

class ConverterWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Distance Converter")
        self.frames=dict()

        container0=ttk.Frame(self)
        container0.grid(padx=60, pady=30, sticky='EW')

        feet_to_metres = FeetToMetres(container0, self)
        feet_to_metres.grid(row=0, column=0, sticky='NSEW')

        metres_to_feet = MetresToFeet(container0, self)
        metres_to_feet.grid(row=0, column=0, sticky='NSEW')

        self.frames[FeetToMetres] = feet_to_metres
        self.frames[MetresToFeet] = metres_to_feet

        # self.bind('<Return>', feet_to_metres.calc)
        # self.bind('<KP_Enter>', feet_to_metres.calc)
        # self.bind('<Alt-f>', feet_to_metres.calc)

        # self.bind('<Return>', metres_to_feet.calc)
        # self.bind('<KP_Enter>', metres_to_feet.calc)
        # self.bind('<Alt-f>', metres_to_feet.calc)


    def show_frame(self,container):
        frame = self.frames[container]
        self.bind('<Return>', container.calc)
        self.bind('<KP_Enter>', container.calc)
        # self.bind('<Alt-f>', container.calc)
        frame.tkraise()


class MetresToFeet(ttk.Frame):
    def __init__(self, container, controller):
        super().__init__(container)
        self.metres_value = tk.StringVar()
        self.feet_value=tk.StringVar(value="Start typing to see result")

        metre_label = ttk.Label(self, text="Metres: ")
        metre_input = ttk.Entry(self, width=20, textvariable=self.metres_value, font=('Comic Sans MS', 15))

        feet_label = ttk.Label(self, text="Feet: ")
        feet_display = tk.Label(self, textvariable=self.feet_value, font=('Comic Sans MS', 15))

        calc_button = ttk.Button(self, text="Convert", state='active', command=self.calc)

        switch_button = ttk.Button(self,
                                   text="Switch to feet conversion",
                                   command=lambda: controller.show_frame(FeetToMetres)
                                   )

        metre_label.grid(row=0, column=0, sticky='w', padx=15, pady=15)
        metre_input.grid(row=0, column=1, sticky='EW', padx=15, pady=15)
        metre_input.focus()
        feet_label.grid(row=1, column=0, sticky='w', padx=15, pady=15)
        feet_display.grid(row=1, column=1, padx=15, pady=15, sticky='w')
        calc_button.grid(row=2, column=0, columnspan=2, sticky='EW', padx=15, pady=15)
        switch_button.grid(row=3, column=0, columnspan=2, sticky='EW', padx=15, pady=15)

        for child in self.winfo_children():
            child.grid_configure(padx=15, pady=15)

    def calc(self, *args):
        try:
            global feet
            metres = float(self.metres_value.get())
            feet = metres * 3.281
            # print(f"Value in feet is {feet}")
            self.feet_value.set(f"{feet:.3f}")
        except ValueError:
            pass
        except:
            self.metres_value.set(0)


class FeetToMetres(ttk.Frame):
    def __init__(self, container, controller):
        super().__init__(container)
        self.feet_value = tk.StringVar()
        self.metres_value=tk.StringVar(value="Start typing to see result")

        feet_label = ttk.Label(self, text="Feet: ")
        feet_input = ttk.Entry(self, width=20, textvariable=self.feet_value, font=('Comic Sans MS', 15))

        metres_label = ttk.Label(self, text="Metres: ")
        metres_display = tk.Label(self, textvariable=self.metres_value, font=('Comic Sans MS', 15))

        calc_button = ttk.Button(self, text="Convert", state='active', command=self.calc)

        switch_button = ttk.Button(self,
                                   text="Switch to feet conversion",
                                   command=lambda: controller.show_frame(MetresToFeet)
                                   )

        feet_label.grid(row=0, column=0, sticky='w', padx=15, pady=15)
        feet_input.grid(row=0, column=1, sticky='EW', padx=15, pady=15)
        feet_input.focus()
        metres_label.grid(row=1, column=0, sticky='w', padx=15, pady=15)
        metres_display.grid(row=1, column=1, padx=15, pady=15, sticky='w')
        calc_button.grid(row=2, column=0, columnspan=2, sticky='EW', padx=15, pady=15)
        switch_button.grid(row=3, column=0, columnspan=2, sticky='EW', padx=15, pady=15)

        for child in self.winfo_children():
            child.grid_configure(padx=15, pady=15)

    def calc(self, *args):
        try:
            global metres
            feet = float(self.feet_value.get())
            metres = feet / 3.281
            # print(f"Value in feet is {feet}")
            self.metres_value.set(f"{metres:.3f}")
        except ValueError:
            pass
        except:
            self.feet_value.set(0)


root = ConverterWindow()
height = root.winfo_screenheight()
width = root.winfo_screenwidth()
center_x = (width-600) // 2
center_y = (height-600) // 2
root.geometry(f'600x500+{center_x}+{center_y}')
root.resizable(False,False)
root.title("Distance Converter")
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

font.nametofont('TkDefaultFont').configure(size=13)

root.mainloop()
