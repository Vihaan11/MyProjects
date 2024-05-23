from time import sleep as wait

from cryptography.fernet import Fernet as fernet

with open("pwd.key", "rb") as secphr:
    mykey = secphr.read()

f = fernet(mykey)

password = "VihaanIsSmart"
usrpwd = input("Password?: ")

if usrpwd == password:
    with open("target.txt", "rb") as of:
        origin = of.read()

    encrypter = f.decrypt(bytes(origin))

    with open("target.txt", "wb") as of:
        of.write(encrypter)
    print("Decrypted!")
else:
    print("Wrong password! Give me more bitcoin or try again.")


wait(7.5)
