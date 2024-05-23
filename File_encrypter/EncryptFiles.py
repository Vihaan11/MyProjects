from cryptography.fernet import Fernet
from time import sleep as wait
from tkinter import filedialog


with open("C://EncryptFiles//sysfiles//pwd.key", "r") as fkey:
    key = fkey.read()
f2 = Fernet(key)


fileopen = filedialog.askopenfilename(initialdir="C://EncryptFiles//LockFolder",
                                      title="Select file to encrypt",
                                      filetypes=(("Text Documents", "*.txt"),
                                                 ("Text Documents encrypted",
                                                  "*.txt_encrypted")))


with open("C://EncryptFiles//sysfiles//pwd.key", "rb") as pwd:
    f = pwd.read()
with open(fileopen, "rb") as of:
    origin = of.read()

encrypter = f2.encrypt(origin)

with open(fileopen+"_encrypted", "wb") as of:
    of.write(encrypter)
print("Done!")
wait(15)
