import math

r = float(input("Enter the radius of the cylinder: "))
h = float(input("Enter the height of the cylinder: "))

sa = 2 * math.pi * r**2 + 2 * math.pi * r * h
v = math.pi * h * r**2

print("Volume = {0:.2f}\nSurface Area = {1:.2f}".format(v,sa))
