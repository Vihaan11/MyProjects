import time
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
                    "": "",
                    "?": "?",
                    "-":"-",
                    ":":":"}
tgt=""
inp=input("Type your message: ")
l = len(inp)
for x in range(int(l)):
    a=inp[x]
    try:
        final = encrypter_engine[a.lower()]
    except:
        final = a
    tgt += final
print(tgt)
time.sleep(10.5)