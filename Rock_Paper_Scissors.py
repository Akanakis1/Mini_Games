import random

options = ["rock", "paper", "scissors"]
player = None
computer = random.choice(options)
point= 0

while player not in options:
    player = input("Enter rock, paper, or scissors: ").lower()
    if player not in options:
        print("Invalid input. Please try again.")

while point < 5:
    if player == "rock" and computer == "scissors":
        point += 1
        print(f"Computer chose {computer}. You win!")
    elif player == "paper" and computer == "rock":
        point += 1
        print(f"Computer chose {computer}. You win!")
    elif player == "scissors" and computer == "paper":
        point += 1
        print(f"Computer chose {computer}. You win!")
    elif player == computer:
        point += 0
        print(f"Computer chose {computer}. It's a tie!")
    else:
        point -= 1
        print(f"Computer chose {computer}. You lose!")
    computer = random.choice(options)
    player = input("Enter rock, paper, or scissors: ").lower()
    
    while player not in options:
        print("Invalid input. Please try again.")
        player = input("Enter rock, paper, or scissors: ").lower()

if point == 5:
    print("You win the game!")
    print("You have 5 points!")
else:
    print("Game over!")
    print("The game is over!")
    print("You have 0 points!")

