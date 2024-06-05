from random import choice

list = ["a","B","c","D","e","F","g","H","i","J","k","l","m","n","o","p","q","?","@","#","1","2","3","4","5","6","7","8","9"]

print("Welcome to password generator")
lmt = input("Password limit (Numbers only): ")

pwd = ""

strings = 0

while strings < int(lmt):
    letter = choice(list)
    pwd += letter
    strings += 1

print(pwd)