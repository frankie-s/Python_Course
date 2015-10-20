import math

a = input("Enter side a length: ")
b = input("Enter side b length: ")
c = input("Enter side c length: ")

p = a + b + c
s = p / 2
a = s * (s - a) * (s - b) * (s - c)
a = math.sqrt(a)

print("Perimeter = {0}\nArea = {1}".format(p,a))
