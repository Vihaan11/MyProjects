import random
import time
t1 = input("Enter person 1: ")
t2 = input("Enter person 2: ")
tp = input("Total points(5 or 10): ")
p1 = 0
p2 = 0

str(t1)
str(t2)
int(tp)
int(p1)
int(p2)


while True:
    value = ["Rock", "Paper", "Scissors"]
    value2 = random.sample(value, k=1)
    value3 = random.sample(value, k=1)
    
    if int(tp) == 5:
        print("Shuffling...")
        time.sleep(4)
        print(str(t1) + " = " + str(value2))
        print(str(t2) + " = " + str(value3))
    
        if str(value2) == "['Rock']" and str(value3) == "['Scissors']" or str(value2) == "['Paper']" and str(value3) == "['Rock']" or str(value2) == "['Scissors']" and str(value3) == "['Paper']":
            print(t1 + " got 1 point")
            p1 += 1
    
            if p1 == 5:
                print(str(t1) + " team won the game")
                break

            elif p2 == 5:
                print(str(t2) + " team won the game")
                break

        elif str(value3) == "['Rock']" and str(value2) == "['Scissors']" or str(value3) == "['Paper']" and str(value2) == "['Rock']" or str(value3) == "['Scissors']" and str(value2) == "['Paper']":
            print(t2 + " got 1 point")
            p2 += 1

            if p1 == 5:
                print(t1 + " team won the game")
                break

            elif p2 == 5:
                print(t2 + " team won the game")
                break

    elif int(tp) == 10:
        print("Shuffling...")
        time.sleep(4)
        print(str(t1) + " = " + str(value2))
        print(str(t2) + " = " + str(value3))

        if str(value2) == "['Rock']" and str(value3) == "['Scissors']" or str(value2) == "['Paper']" and str(value3) == "['Rock']" or str(value2) == "['Scissors']" and str(value3) == "['Paper']":
            print(t1 + " got 1 point")
            p1 += 1

            if p1 == 10:
                print(str(t1) + " won the game")
                break

            elif p2 == 10:
                print(str(t2) + " won the game")
                break

        elif str(value3) == "['Rock']" and str(value2) == "['Scissors']" or str(value3) == "['Paper']" and str(value2) == "['Rock']" or str(value3) == "['Scissors']" and str(value2) == "['Paper']":
            print(t2 + " got 1 point")
            p2 += 1

            if p1 == 10:
                print(t1 + " won the game")
                break

            elif p2 == 10:
                print(t2 + " won the game")
                break
    else:
        print("5 or 10 only supported.")
        break
time.sleep(10.05)