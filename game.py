import random 

def game(user,computer):
      if computer == user:
            print("ooo its a tie")
      elif(user == 'rock'and computer=='scissor') or (user == 'scissor'and computer=='paper') or (user == 'paper'and computer=='rock'):
            print("you win!!!!!!!")
      else:
           print("computer win")


print("Welcome to Rock-Paper-Scissors!")
print("Rules: Rock beats Scissors, Scissors beat Paper, Paper beats Rock")
print("game begins")

choices=['rock','paper','scissor']


while True:
    user_choice = input("plese choose rock,paper,scissor: ").lower()
    if user_choice not in choices:
        print("invalid input")
        continue
    computer_choice= random.choice(choices)
    print(f"you choice:{user_choice}")
    print(f"computer choice:{computer_choice}")

    result=game(user_choice,computer_choice)
    print(result)

    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again == "n":
        print("Thanks for playing!")
        break
    


