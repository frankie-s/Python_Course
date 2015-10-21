sentence = raw_input("Enter a sentence to count: ")

def word_count(sentence):
    sentence = sentence.lower().split()
    print(sentence)
    print(len(sentence))

word_count(sentence)