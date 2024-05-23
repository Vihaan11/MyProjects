from random import randint as rnum
import time

rand_number = rnum(1, 100)

if True:
    plus_ten=rand_number+5
    minus_ten=rand_number-5
    plus_fiftn=rand_number+15
    minus_fiftn=rand_number-15

if True:
    lv_easy_a=rnum(rand_number-15, rand_number-10)
    lv_easy_b=rnum(rand_number+10, rand_number+15)
    lv_medium_a=rnum(rand_number-20, rand_number-15)
    lv_medium_b=rnum(rand_number+15, rand_number+20)
    lv_hard_a=rnum(rand_number-25, rand_number-20)
    lv_hard_b=rnum(rand_number+20, rand_number+25)
if True:
    if lv_easy_a<1:
        lv_easy_a=1
    if lv_easy_b>100:
        lv_easy_b=100
    if lv_medium_a<1:
        lv_medium_a=1
    if lv_medium_b>100:
        lv_medium_b=100
    if lv_hard_a<1:
        lv_hard_a=1

    if lv_hard_b>100:
        lv_hard_b=100
print("\nWelcome to number guessing game!\nYou have to guess a number between 1 and 100\n\n")
lvl=input("Choose Difficulty('Easy', 'Medium', 'Hard', 'Impossible') : ")

def easy(random_number, lv_a, lv_b):
    print(f"The number is between {lv_a} and {lv_b}")
    for i in range(8):
        user_input = int(input(f"Your {i+1} (out of 8) guess:"))


        if user_input > random_number:
            o = "less than"
        if user_input < random_number:
            o = "more than"
        

        if user_input==random_number:
            print(f"Hurrah!! You guessed the number, it was {random_number}")
            time.sleep(10)
            exit()
        elif (user_input < plus_ten and user_input > random_number) or (user_input > minus_ten and user_input < random_number):
            if i != 7:
                print(f"\nThat was a miss, but you are very near. Come on, you can do this. The number is {o} your guess\n")
        elif (user_input < plus_ten and user_input > random_number) or (user_input > minus_ten and user_input < random_number):
            if i != 7:
                print(f"\nThat was a miss, but you are very near. Come on, you can do this. The number is {o} your guess\n")
        # elif (user_input < plus_fiftn and user_input > random_number) or (user_input > minus_fiftn and user_input < random_number):
        #     if i != 7:
        #         print(f"\nThat was a miss but you are kinda close. The number is {o} your guess\n")
        # elif (user_input < plus_fiftn and user_input > random_number) or (user_input > minus_fiftn and user_input < random_number):
        #     if i != 7:
        #         print(f"\nThat was a miss but you are kinda close. The number is {o} your guess\n")
        elif i != 7:
            print(f"\nThat was a miss. The number is {o} your guess\n")
def medium(random_number, lv_a, lv_b):
    print(f"The number is between {lv_a} and {lv_b}")
    for i in range(5):
        user_input = int(input(f"Your {i+1} (out of 5) guess:"))


        if user_input > random_number:
            o = "less than"
        if user_input < random_number:
            o = "more than"
        

        if user_input==random_number:
            print(f"Hurrah!! You guessed the number, it was {random_number}")
            time.sleep(10)
            exit()
        elif (user_input < plus_ten and user_input > random_number) or (user_input > minus_ten and user_input < random_number):
            if i != 4:
                print(f"\nThat was a miss, but you are very near. Come on, you can do this. The number is {o} your guess\n")
        elif (user_input < plus_ten and user_input > random_number) or (user_input > minus_ten and user_input < random_number):
            if i != 4:
                print(f"\nThat was a miss, but you are very near. Come on, you can do this. The number is {o} your guess\n")
        elif (user_input < plus_fiftn and user_input > random_number) or (user_input > minus_fiftn and user_input < random_number):
            if i != 4:
                print(f"\nThat was a miss but you are kinda close. The number is {o} your guess\n")
        elif (user_input < plus_fiftn and user_input > random_number) or (user_input > minus_fiftn and user_input < random_number):
            if i != 4:
                print(f"\nThat was a miss but you are kinda close. The number is {o} your guess\n")
        elif i != 4:
            print(f"\nThat was a miss and you don't seem to be close to the number. The number is {o} your guess\n")
def hard(random_number, lv_a, lv_b):
    print(f"The number is between {lv_a} and {lv_b}")
    for i in range(5):
        user_input = int(input(f"Your {i+1} (out of 5) guess:"))


        if user_input > random_number:
            o = "less than"
        if user_input < random_number:
            o = "more than"
        

        if user_input==random_number:
            print(f"Hurrah!! You guessed the number, it was {random_number}")
            time.sleep(10)
            exit()
        # elif (user_input < plus_ten and user_input > random_number) or (user_input > minus_ten and user_input < random_number):
        #     if i != 4:
        #         print(f"\nThat was a miss, but you are very near. Come on, you can do this. The number is {o} your guess\n")
        # elif (user_input < plus_ten and user_input > random_number) or (user_input > minus_ten and user_input < random_number):
        #     if i != 4:
        #         print(f"\nThat was a miss, but you are very near. Come on, you can do this. The number is {o} your guess\n")
        # elif (user_input < plus_fiftn and user_input > random_number) or (user_input > minus_fiftn and user_input < random_number):
        #     if i != 4:
        #         print(f"\nThat was a miss but you are kinda close. The number is {o} your guess\n")
        # elif (user_input < plus_fiftn and user_input > random_number) or (user_input > minus_fiftn and user_input < random_number):
        #     if i != 4:
        #         print(f"\nThat was a miss but you are kinda close. The number is {o} your guess\n")
        elif i != 4:
            print(f"\nThat was a miss. The number is {o} your guess\n")
def impossible(random_number):
    for i in range(5):
        user_input = int(input(f"Your {i+1} (out of 5) guess:"))


        if user_input > random_number:
            o = "less than"
        if user_input < random_number:
            o = "more than"
        

        if user_input==random_number:
            print(f"Hurrah!! You guessed the number, it was {random_number}")
            time.sleep(10)
            exit()
        # elif (user_input < plus_ten and user_input > random_number) or (user_input > minus_ten and user_input < random_number):
        #     if i != 4:
        #         print(f"\nThat was a miss, but you are very near. Come on, you can do this. The number is {o} your guess\n")
        # elif (user_input < plus_ten and user_input > random_number) or (user_input > minus_ten and user_input < random_number):
        #     if i != 4:
        #         print(f"\nThat was a miss, but you are very near. Come on, you can do this. The number is {o} your guess\n")
        # elif (user_input < plus_fiftn and user_input > random_number) or (user_input > minus_fiftn and user_input < random_number):
        #     if i != 4:
        #         print(f"\nThat was a miss but you are kinda close. The number is {o} your guess\n")
        # elif (user_input < plus_fiftn and user_input > random_number) or (user_input > minus_fiftn and user_input < random_number):
        #     if i != 4:
        #         print(f"\nThat was a miss but you are kinda close. The number is {o} your guess\n")
        elif i != 4:
            print(f"\nThat was a miss. The number is {o} your guess\n")

if True:
    if lvl=="Easy" or lvl=="easy" or lvl == "EASY":
        easy(rand_number, lv_easy_a, lv_easy_b)
    elif lvl=="Medium" or lvl=="medium" or lvl=="MEDIUM":
        medium(rand_number, lv_medium_a, lv_medium_b)
    elif lvl=="Hard" or lvl=="hard" or lvl=="HARD":
        hard(rand_number, lv_hard_a, lv_hard_b)
    elif lvl=="Impossible" or lvl=="impossible" or lvl=="IMPOSSIBLE":
        impossible(rand_number)
    else:
        print("Sorry. An invalid input was entered in the level input field. Only enter the values given in the brackets")
        time.sleep(10)
        exit()

print(f"\n\nWhup!! Looks like you couldn't guess the number. The number was {rand_number}. Better luck next time!!")

time.sleep(10)
exit()
