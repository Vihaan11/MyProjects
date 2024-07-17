# Installer Template Documentation

## Overview
This documentation provides instructions on how to use the provided installer template to create a setup wizard for your application.

## Prerequisites
- Python 3.7+
- `tkinter` library (included with Python standard library)

## How to Use

1. **Import Necessary Libraries**

   Import the necessary libraries:
    ```Python
   from windows_installer import Installer_Window
   import tkinter as tk
   from tkinter import ttk
   ```

2. **Define the Next Button Function**

   Define the function to be executed when the 'Next' button is clicked. For example:
   ```python
   def myfunc():
       print("Hello, World")
   ```

3. **Initialize and Configure the Installer Window**

   Create an instance of `Installer_Window` and configure it with the desired parameters:
   ```python
   root = Installer_Window("Setup Wizard", 300, 700)
   root.config(
       header_line="Welcome to setup", 
       body_line="Click next to continue", 
       next_button="Next", 
       back_button="Back", 
       next_button_func=myfunc
   )
   root.mainloop()
   ```

## Parameters

### **For self:**
- `title`: Title of the installer window.
- `height`: Height of the installer window.
- `width`: Width of the installer window.

### **For self.config:**

- `header_line`: Text to be displayed in the header.
- `body_line`: Text to be displayed in the body.
- `next_button`: Text for the 'Next' button.
- `back_button`: Text for the 'Back' button.
- `next_button_func`: Function to be called when the 'Next' button is clicked.

## Example

Here is a complete example using the template:

```Python
from windows_installer import Installer_Window
import tkinter as tk
from tkinter import ttk

def dpi_awareness():
    try:
        from ctypes import windll
        windll.shcore.SetProcessDpiAwareness(1)
    except:
        pass

dpi_awareness()

def myfunc():
    print("Hello, World")

root = Installer_Window("Setup Wizard", 300, 700)
root.config(
    header_line="Welcome to setup", 
    body_line="Click next to continue", 
    next_button="Next", 
    back_button="Back", 
    next_button_func=myfunc
)
root.mainloop()
```

## License
This template is free to use and modify for personal and commercial purposes.