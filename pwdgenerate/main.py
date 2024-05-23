import random

list = ["a","B","c","D","e","F","g","H","i","J","k","l","m","n","o","p","q","?","@","#","1","2","3","4","5","6","7","8","9"]
print("Welcome to password generator")
LMT = input("Password limit (Numbers only): ")

strings = 0

pwd = ""

while int(LMT) > strings:
    letter = random.choice(list)
    pwd += letter
    strings += 1

print(pwd)