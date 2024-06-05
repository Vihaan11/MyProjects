# (1/2) * b * h

class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return f"Area of triangle is {(1/2) * self.base * self.height}"

h=float(input("height: "))
b=float(input("base: "))

Triang=Triangle(b,h)

print(Triang.area())

