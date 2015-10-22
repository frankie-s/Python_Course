import sys
__author__ = "Frankie S."

words1 = {1:"One",2:"Two",3:"Three",4:"Four",5:"Five",6:"Six",7:"Seven",8:"Eight",9:"Nine"}
words2 = {0:"",1:"-One",2:"-Two",3:"-Three",4:"-Four",5:"-Five",6:"-Six",7:"-Seven",8:"-Eight",9:"-Nine"}
words3 = {10:"Ten",11:"Eleven",12:"Twelve",13:"Thirthteen",14:"Fourteen",15:"Fifthteen",16:"Sixteen",17:"Seventeen",18:"Eightteen",19:"Ninteen"}
words4 = {9:'Ninety',8:'Eighty',7:'Seventy',6:'Sixty',5:'Fifty',4:'Fourty',3:'Thirty',2:'Twenty'}

def sing(beer_num):
    while 20<= beer_num <=99:
        tens = beer_num / 10
        ones = beer_num % 10
        answer_str = words4[tens] + words2[ones]
        #next_answer_str = words4[tens] + words2[ones -1]
        print(answer_str + " bottles of beer on the wall!\n" + answer_str + " bottles of beer!\nTake one down\nAnd pass it around\n" + answer_str + " bottles of beer on the wall!\n")
        beer_num = beer_num - 1

    while 10 <= beer_num <= 19:
        tens = beer_num / 10
        ones = beer_num % 10
        answer_str = words4[tens] + words2[ones]
        #next_answer_str = words4[tens] + words2[ones -1]
        print(answer_str + " bottles of beer on the wall!\n" + answer_str + " bottles of beer!\nTake one down\nAnd pass it around\n" + answer_str + " bottles of beer on the wall!\n")
        beer_num = beer_num - 1

    while 2<= beer_num <= 10:
        for x in word_dic1:
            print(word_dic1.get(x) +" bottles of beer on the wall!\n" +word_dic1.get(x) + " bottles of beer!\nTake one down\nAnd pass it around\n" +word_dic1.get(x) +" bottles of beer on the wall!\n")
        beer_num = beer_num - 1
        print("One bottle of beer on the wall!\nOne bottle of beer!\nTake one down\nAnd pass it around\nNo more bottles of beer on the wall!\n")


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
