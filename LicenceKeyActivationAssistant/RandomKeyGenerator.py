import random
letters = ["a","b", "c",
                    "d",
                    "e",
                    "f",
                    "g",
                    "h",
                    "i",
                    "j",
                    "k",
                    "l",
                    "m",
                    "n",
                    "o",
                    "p",
                    "q",
                    "r",
                    "s",
                    "t",
                    "u",
                    "v",
                    "w",
                    "x",
                    "y",
                    "z","0", "1", "2", "3", "4","5","6","7","8","9"]
keys = []
try:
    while True:
        key = ""
        for i in range(25):
            if i == 5 or i == 10 or i == 15 or i == 20:
                key += "-"
            rndm = random.randint(0, 34)
            key += letters[rndm].upper()
        keys.append(key)
except KeyboardInterrupt:
    with open("keys.txt", "a") as listw:
        keylist = '\n'.join(keys)
        listw.writelines("\n"+keylist)
except:
    print("error")
