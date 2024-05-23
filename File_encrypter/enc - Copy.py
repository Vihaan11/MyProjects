from cryptography.fernet import Fernet as fernet
from time import sleep as wait

file = input("File path to encrypt(Replace \ with //)")
try:
    with open(file, "r"):
        import time
except:
    print("Error!")
    wait(7.5)
    exit()

condition = True

while condition == True:
    thepwd = input("Password: ")
    thepwdconf = input("Confirm Password: ")
    if thepwdconf == thepwd:
        condition = False
        continue
    else:
        print("Passwords don't match. Try again")


with open("C://EncryptFiles//sysfiles//thepwdis.key", "w") as thek:
    pwd2=thek.write(thepwd)

with open("C://EncryptFiles//sysfiles//pwd.key", "wb") as pwd:
    f = fernet.generate_key()
    key = pwd.write(f)

with open(file, "rb") as of:
    origin = of.read()

encrypter = fernet(f).encrypt(origin)

with open(file, "wb") as of:
    of.write(encrypter)

wait(7.5)
