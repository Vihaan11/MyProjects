from time import sleep as wait

from cryptography.fernet import Fernet as fernet

with open("pwd.key", "rb") as secphr:
    mykey = secphr.read()

f = fernet(mykey)

with open("C://EncryptFiles//sysfiles//thepwdis.key","r") as thek:
    pwd=thek.read()
    usrpwd = input("Password?: ")

if usrpwd == pwd:
    with open("target.txt", "rb") as of:
        origin = of.read()

    encrypter = f.decrypt(origin)

    with open("target.txt", "wb") as of:
        of.write(encrypter)
    print("Decrypted!")
else:
    print("Wrong password! Rerun the decrypter.")


wait(7.5)
