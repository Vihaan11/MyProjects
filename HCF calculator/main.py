# We would use the Euclid algorithm
li=[]
a = input("Num 1: ")
b = input("Num 2: ")
li.append(int(a)), li.append(int(b))
print(li)
li.sort()
c=li[0] % li[-1]
while True