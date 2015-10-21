__author__ = 'frankie'

# Write a program that inputs two strings from the user and
# outputs the strings with the first two characters have
# been swapped. You may assume that the words entered are at
# least two letters long.

w_one = raw_input("Enter first word to swap: ")
w_two = raw_input("Enter second word to swap: ")

w_one_chars = w_one[:2]
w_one_rest = w_one[2:]
w_two_chars = w_two[:2]
w_two_rest = w_two[2:]

print(w_two_chars + w_one_rest + " " + w_one_chars + w_two_rest )