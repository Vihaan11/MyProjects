from cryptography.fernet import Fernet
import time
print("You need to keep your file in C:/EncryptFiles/LockFolder to decrypt it!")
file=input("File name with extension: ")
with open("C:/EncryptFiles/sysfiles/pwd.key", "rb") as secphr:
    mykey = secphr.read()
with open(file, "rb") as tgt:
    decrypttgrt = tgt.read()
decrypted = Fernet(mykey).decrypt(decrypttgrt)
with open("decryptedfile.txt", "wb") as tgt2:
    decrypt = tgt2.write(decrypted)
    print("Done!")
time.sleep(7.25)
