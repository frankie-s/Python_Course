from __future__ import print_function


my_char = raw_input("Enter a character: ")
num = input("Enter a number: ")

def repeat(string, length):
    cur, old = 1, string
    while len(string) < length:
        string += old[cur-1]
        cur = (cur+1)%len(old)
    return string

print(repeat(my_char,num))
