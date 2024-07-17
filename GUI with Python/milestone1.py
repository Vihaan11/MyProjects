from windows import dpi_awareness
import tkinter as tk
from tkinter import ttk
import tkinter.font as font

dpi_awareness()

class ConverterWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Distance Converter")
        main = MetresToFeet(self,padding=(30,15))
        self.bind('<Return>', main.calc_feet)
        self.bind('<KP_Enter>', main.calc_feet)
        self.bind('<Alt-f>', main.calc_feet)
        main.grid()


class MetresToFeet(ttk.Frame):
    def __init__(self, container, **kwargs):
        super().__init__(container, *kwargs)
        self.metres_value = tk.StringVar()
        self.feet_value=tk.StringVar(value="Start typing to see result")

        metre_label = ttk.Label(self, text="Metres: ")
        metre_input = ttk.Entry(self, width=20, textvariable=self.metres_value, font=('Comic Sans MS', 15))

        feet_label = ttk.Label(self, text="Feet: ")
        feet_display = tk.Label(self, textvariable=self.feet_value, font=('Comic Sans MS', 15))

        calc_button = ttk.Button(self, text="Convert", command=calc_feet)

        for child in self.winfo_children():
            child.grid_configure(padx=15, pady=15)

    def calc_feet(self, *args):
        try:
            global feet
            metres = float(self.metres_value.get())
            feet = metres * 3.281
            # print(f"Value in feet is {feet}")
            self.feet_value.set(f"{feet:.3f}")
        except ValueError:
            pass
        except:
            metres_value.set(0)



root = ConverterWindow()
height = root.winfo_screenheight()
width = root.winfo_screenwidth()
center_x = (width-600) // 2
center_y = (height-400) // 2
root.geometry(f'600x300+{center_x}+{center_y}')
root.resizable(False,False)
root.title("Distance Converter")
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

font.nametofont('TkDefaultFont').configure(size=13)

# Code goes here👇


metre_label.grid(row=0, column=0, sticky='w', padx=15, pady=15)
metre_input.grid(row=0, column=1, sticky='EW', padx=15, pady=15)
metre_input.focus()
feet_label.grid(row=1, column=0, sticky='w', padx=15, pady=15)
feet_display.grid(row=1, column=1, padx=15, pady=15, sticky='w')
calc_button.grid(row=2, column=0, columnspan=2, sticky='EW', padx=15, pady=15)





# Starting the loop
root.mainloop()
