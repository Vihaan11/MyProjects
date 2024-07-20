from windows import dpi_awareness
import tkinter as tk
from tkinter import ttk
import tkinter.font as font

dpi_awareness()

root = tk.Tk()
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
feet_value=tk.StringVar()

def calc_feet(*args):
    try:
        global feet
        metres = float(metres_value.get())
        feet = metres * 3.281
        # print(f"Value in feet is {feet}")
        feet_value.set(f"{feet:.9}")
    except ValueError:
        pass
    except:
        metres_value.set(0)


def calc_metre(*args):
    try:
        global metre
        feet = float(feet_value.get())
        metre = feet / 3.281
        # print(f"Value in feet is {feet}")
        metres_value.set(f"{metre:.9}")
    except ValueError:
        pass
    except:
        metres_value.set(0)

main = ttk.Frame(root,padding=(30,15))
main.grid()

metre_label = ttk.Label(main, text="Metres: ")
metre_input = ttk.Entry(main, width=20, textvariable=metres_value, font=('Comic Sans MS', 15))
# metre_input =spin_box = ttk.Spinbox(main,
#                                     from_=0,
#                                     to=999,
#                                     textvariable=metres_value,
#                                     wrap=True)

feet_label = ttk.Label(main, text="Feet: ")
feet_input = tk.Entry(main, width=20, textvariable=feet_value, font=('Comic Sans MS', 15))

# calc_button = ttk.Button(main, text="Convert", command=calc_metre)

metre_label.grid(row=0, column=0, sticky='w', padx=15, pady=15)
metre_input.grid(row=0, column=1, sticky='EW', padx=15, pady=15)
metre_input.focus()
feet_label.grid(row=1, column=0, sticky='w', padx=15, pady=15)
feet_input.grid(row=1, column=1, padx=15, pady=15, sticky='w')
# calc_button.grid(row=2, column=0, columnspan=2, sticky='EW', padx=15, pady=15)

for child in main.winfo_children():
    child.grid_configure(padx=15, pady=15)

feet_value.trace('w', calc_metre)
metres_value.trace('w', calc_feet)
# metre_input.bind('<Return>', calc_feet)
# metre_input.bind('<KP_Enter>', calc_feet)
# metre_input.bind('<Alt-f>', calc_feet)


# Starting the loop
root.mainloop()