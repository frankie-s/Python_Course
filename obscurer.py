# Write a program that inputs a string from the user and
# outputs a string in which all occurrences of the first
# character of the input string are replaced with '?',
# except the first character itself. Assume the string is not empty.
from string import replace

word = raw_input("Enter a word to obscure: ")
one_char = word[0]
rest_char = replace(word[1:],one_char, "?")

print one_char+rest_char
