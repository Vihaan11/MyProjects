from tkinter import *
from tkinter import filedialog
from cryptography.fernet import Fernet

def encrypt_file():
    try:
        key = "GB1EuXazKy_JnCNpeGO4gLSHDsVLYphr0FVV2AUse4I="
        cipher = Fernet(key)

        file_path = filedialog.askopenfilename(initialdir="C://EncryptFiles//LockFolder",
                                               title="Select file to encrypt",
                                               filetypes=(("Text Documents", "*.txt"),
                                                          ("Text Documents encrypted",
                                                           "*.txt_encrypted")))
        with open(file_path, "rb") as file:
            file_data = file.read()
            encrypted_data = cipher.encrypt(file_data)

        encrypted_file_path = filedialog.asksaveasfilename(initialdir="C://EncryptFiles//LockFolder",
                                               title="Select file to encrypt",
                                               filetypes=(("Text Documents encrypted",
                                                           "*.txt_encrypted")))
        with open(encrypted_file_path, "wb") as encrypted_file:
            encrypted_file.write(encrypted_data)

        print("File successfully encrypted!")
    except:
        print("Error!!")

root = Tk()
encrypt_button = Button(root, text="Encrypt File", command=encrypt_file)
encrypt_button.pack()
root.mainloop()
