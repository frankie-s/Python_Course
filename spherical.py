import math 

r = float(input("Enter the radius of the sphere: "))
v = 4/3 * math.pi * r**3
sa = 4 * math.pi * r**2

print("Volume       = {0:>10.3f}\nSurface Area = {1:>10.3f}".format(v,sa))
