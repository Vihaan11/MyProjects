encrypter_engine = {" ": " ",
                    "a": "z",
                    "b": "y",
                    "c": "x",
                    "d": "w",
                    "e": "v",
                    "f": "u",
                    "g": "t",
                    "h": "s",
                    "i": "r",
                    "j": "q",
                    "k": "p",
                    "l": "o",
                    "m": "n",
                    "n": "m",
                    "o": "l",
                    "p": "k",
                    "q": "j",
                    "r": "i",
                    "s": "h",
                    "t": "g",
                    "u": "f",
                    "v": "e",
                    "w": "d",
                    "x": "c",
                    "y": "b",
                    "z": "a",
                    ".": ".",
                    ",": ",",
                    "": ""}
import time
loop = 0
em = ""
print("No special characters are allowed")
while loop < 2:
    ltr = input("Enter the letter of your message. Type 'print' if done: ")
    if ltr == "print":
        loop = 5
        print(em)
    else:
        try:
            el = encrypter_engine[ltr.lower()]
            em += el
        except:
            print("An error occoured while encrypting the message")
            time.sleep(10.5)
            exit()
time.sleep(10.5)