# Write a program that requests a sentence,
# then print out the first and last words of the sentence,
# and finally, the number of words in the sentence.

def wordalyze(sentence_in):
    count = len(sentence.lower().split())
    list = (sentence.lower().split())
    first = list[0]
    last = list[count - 1]
    return first,last,count


if __name__ == '__main__':
    sentence = raw_input("Enter a sentence: ")
    output = wordalyze(sentence)
    print(output)


