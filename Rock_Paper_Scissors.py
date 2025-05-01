import random

print("*************************************")
print("**Welcome to Rock, Paper, Scissors!**")
print("*************************************")

options = ["rock", "paper", "scissors"]
point = 0
rounds = 0
max_points = 5
min_points = -3

print(f"Reach {max_points} points to win, or drop to {min_points} to lose.\n")

while min_points < point < max_points:
    player = input("Enter rock, paper, or scissors: ").lower()
    while player not in options:
        print("Invalid input. Please try again.")
        player = input("Enter rock, paper, or scissors: ").lower()
    
    computer = random.choice(options)
    print(f"Computer chose {computer}.")

    if player == computer:
        print("It's a tie!\n")
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        point += 1
        print("You win this round!\n")
    else:
        point -= 1
        print("You lose this round!\n")
    
    print(f"Current score: {point}\n")

if point == max_points:
    print("🎉 You win the game!")
elif point <= min_points:
    print("💥 You lost the game. Better luck next time!")

