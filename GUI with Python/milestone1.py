from windows import dpi_awareness
import tkinter as tk
from tkinter import ttk
import tkinter.font as font

dpi_awareness()

class ConverterWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Distance Converter")
        self.main = ttk.Frame(self,padding=(30,15))
        self.main.grid()

class MetresToFeet(object):
    """docstring for MetresToFeet."""

    def __init__(self, arg):
        super(MetresToFeet, self).__init__()
        self.arg = arg


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

metres_value = tk.StringVar()
feet_value=tk.StringVar(value="Start typing to see result")

def calc_feet(*args):
    try:
        global feet
        metres = float(metres_value.get())
        feet = metres * 3.281
        # print(f"Value in feet is {feet}")
        feet_value.set(f"{feet:.3f}")
    except ValueError:
        pass
    except:
        metres_value.set(0)



metre_label = ttk.Label(root.main, text="Metres: ")
metre_input = ttk.Entry(root.main, width=20, textvariable=metres_value, font=('Comic Sans MS', 15))
# metre_input =spin_box = ttk.Spinbox(root.main,
#                                     from_=0,
#                                     to=999,
#                                     textvariable=metres_value,
#                                     wrap=True)

feet_label = ttk.Label(root.main, text="Feet: ")
feet_display = tk.Label(root.main, textvariable=feet_value, font=('Comic Sans MS', 15))

calc_button = ttk.Button(root.main, text="Convert", command=calc_feet)

metre_label.grid(row=0, column=0, sticky='w', padx=15, pady=15)
metre_input.grid(row=0, column=1, sticky='EW', padx=15, pady=15)
metre_input.focus()
feet_label.grid(row=1, column=0, sticky='w', padx=15, pady=15)
feet_display.grid(row=1, column=1, padx=15, pady=15, sticky='w')
calc_button.grid(row=2, column=0, columnspan=2, sticky='EW', padx=15, pady=15)

for child in root.main.winfo_children():
    child.grid_configure(padx=15, pady=15)


metre_input.bind('<Return>', calc_feet)
metre_input.bind('<KP_Enter>', calc_feet)
metre_input.bind('<Alt-f>', calc_feet)

# Starting the loop
root.mainloop()
