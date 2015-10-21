__author__ = 'frankie'
import string

# Write a program that removes all duplicate words from a
# sentence entered by the user. Note: The words do not need to
# be in the same order as they were entered.

sentence = raw_input("Enter a string to deduplicate: ").lower()

my_list = (sentence.lower().split())
my_list2 = []

for i in my_list:
    if i not in my_list2:
        my_list2.append(i)
print(my_list2)

#sentence = ' '.join(set(sentence.split()))
#print(sentence)
