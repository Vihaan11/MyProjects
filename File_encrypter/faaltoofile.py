from cryptography.fernet import Fernet
import time
target=input("Type the name of your file with file extension: ")
with open(target,"rb") as tgt:
    target2=tgt.read()
with open("C://EncryptFiles//sysfiles//pwd.key", "rb") as pwd4:
    pwd3 = pwd4.read()
decrypted = Fernet(pwd3).decrypt(target2)
with open("decrypted_file.txt", "wb") as tgt2:
    decrypt = tgt2.write(decrypted)
    print("Decrypted")