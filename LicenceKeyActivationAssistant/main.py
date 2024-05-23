PK = input("Enter your licence key: ")
with open("keys.txt", "r") as kr:
    krr = kr.read()
    if PK in krr:
        with open("ListOfDoneKeys.txt", "r") as lodr:
            lrr = lodr.read()
            if PK in lrr:
                print("Sorry, your licence key has already been used")
            else:
                with open("ListOfDoneKeys.txt", "a") as la:
                    la.write('''
'''+PK)
                input("YOUR LICENCE KEY WORKS! Press enter when you're ready: ")
    else:
        print("Sorry, your licence key is invalid")
        exit()