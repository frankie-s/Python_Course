import sys
from num2words import num2words
__author__ = "Frankie S."


def sing(beer_num):
    while beer_num >= 2:
        print(num2words(beer_num).title() +
              " bottles of beer on the wall!\n" +
              num2words(beer_num).title() + " bottles "
              "of beer!\nTake one down\nAnd pass it around\n" +
              num2words(beer_num - 1).title() +
              " bottles of beer on the wall!\n")
        beer_num = beer_num - 1
    print("One bottle of beer on the wall!\nOne bottle of beer!\n"
          "Take one down\nAnd pass it around\n"
          "No more bottles of beer on the wall!\n")


def main(*argv):
    arg = sys.argv[0:]
    if len(arg) == 1:
        beer_num = 99
        sing(beer_num)
    else:
        # input validation/error handling
        if str.isdigit(sys.argv[1]) == True and \
         int(sys.argv[1]) <= 99 and int(sys.argv[1]) >= 1:
            beer_num = int(sys.argv[1])
            sing(int(beer_num))
        else:
            print("Enter a valid number[1-99]\n")


main(sys.argv[0:])
