import random

def guessing_game(lw_num, mx_num):
    print("Guessing game, Guess any number between", lw_num , " - ", mx_num)
    ink = 's'
    num_Of_Tries = 1
    ran_Num = random.randrange(lw_num, mx_num)
    while ink =='s':
        user = int(input("guess the number"))
        print(ran_Num)
        if user == ran_Num:
            print("congrat's " ,num_Of_Tries, ", is all the tries it took")
            ink = 'q'
        else:
            ink = str(input(' try again with s or quit with q'))
            num_Of_Tries = num_Of_Tries+1

min_num = int(input("Give me a range of numbers first input the lowest number: "))
max_num = int(input("Now input the max number: "))

guessing_game(min_num, max_num)
