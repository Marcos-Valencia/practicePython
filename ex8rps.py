print("WELCOME TO RPS")
user1 = str(input("who will be player 1?"))
user2 = str(input("who will be player 2?"))
user1_trn = str(user1) + ", Paper Rock or Scissors?"
user2_trn = str(user2) + ", Paper Rock or Scissors?"

print("This is RPS(Rock Paper Scissors)\n "
      "To quite Type out as soon as you get a winner\n"
      "Rock = 1\n"
      "Paper = 2\n"
      "Scissors = 3")

def prs_func(use1, use2):
    game_status = str("ongoing")
    while game_status !=str("out"):
        user1_move = int(input(user1_trn))
        user2_move = int(input(user2_trn))
        if user1_move == user2_move:
            print("draw")
        elif user1_move ==1 and user2_move == 3:
            print(user1, " is the winner Congrats")
        elif user2_move ==1 and user1_move == 3:
            print(user2, " is the winner Congrats")
        elif user1_move ==3 and user2_move ==2:
            print(user1, " is the winner Congrats")
        elif user2_move ==3 and user1_move ==2:
            print(user2, " is the winner Congrats")
        elif user1_move ==2 and user2_move ==1:
            print(user1, " is the winner Congrats")
        elif user2_move == 2 and user1_move == 1:
            print(user2, " is the winner Congrats")
        game_status = str(input("Do you want to quite? Type 'out' if so else type any other character/s \n "))
prs_func(user1, user2)
print("||     !!GAME OVER!!     ||")
