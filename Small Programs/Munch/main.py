# Munch app MVP
# v1.0.1
# By Vihaan Vyas


import random, time
dish = ["Matar-paneer", "Koftae", "Rajma-chaval", "Ghea", "Chholay-bhature", "Chholay-kulche", "Kadi", "Dal makhani", "Aloo-pyaz"]

no_of_days = input("How many days do you want me to plan your dishes for? ")
doneitems = []
for i in range(int(no_of_days)):
    def choosingrandom():
        randomno = random.randint(0, 8)
        crdsh = str(dish[randomno])
        return crdsh
    loopint = 0
    while loopint < 2:
        crdsh2 = choosingrandom()
        if crdsh2 in doneitems:
            choosingrandom()
        else:
            loopint = 6
    print("Day " + str(int(i)+1) + "-" + crdsh2)
    doneitems.append(crdsh2)

time.sleep(600)