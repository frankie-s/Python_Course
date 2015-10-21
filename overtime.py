__author__ = 'frankie'
import re

# Write a program that prompts the user for an hourly wage, and then a number of hours worked.
# The program should then print the wages to be paid. If more than 40 hours were worked
# (i.e., overtime), the employee should get 1.5 times their usual rate for every hour over 40.

wage = raw_input("Enter hourly wage: ")
wage = float(wage.replace('$',''))
hours = float(input("Enter hours worked: "))

paycheck = wage * hours

if hours > 40:
    paycheck += 0.5 * wage * (hours - 40)

print("${:.2f}".format(paycheck))