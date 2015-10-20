import math 

r = input("Enter the radius of the sphere: ")
v = math.pi * r**3
v = v * 4/3

sa = math.pi * r**2
sa = sa * 4

print("Volume       = {0}\nSurface Area = {1}".format(v,sa))
