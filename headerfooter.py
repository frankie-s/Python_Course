__author__ = 'frankie'

# Write a program that takes a string and outputs a new string
# represented by the first two and last two characters in the original string.

my_str = raw_input("Enter a string to mangle: ")
print("{}{}".format(my_str[:2], my_str[-2:]))