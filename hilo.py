__author__ = 'frankie'
import math

# Write a program that prompts the user for two numbers. The
# program should then print "Low/High" if the first number
# was less than the second number, "High/Low" if the second
# number was less than the first, and "Equal" if the two numbers are equal.

n1 = float(input("Enter first number: "))
n2 = float(input("Enter second number: "))

if n1 - n2 > 0:
    print("High/Low")
elif n1 - n2 == 0:
    print("Equal")
else:
    print("Low/High")



