import random

lowest = 0
highest = 100
answer = random.randint(lowest, highest)
guesses = 0
is_guessing = True

print("Welcome to the Guessing Game!")
print(f"Guess a number between {lowest} and {highest}.")
print("You have 10 attempts to guess the correct number.")
print("If you want to quit, type 'exit' at any time.")
print("Good luck!")

while is_guessing and guesses < 10:
    guess = input(f"Attempt {guesses + 1}: Enter your guess: ")
    
    if guess.lower() == 'exit':
        print("Thanks for playing! Goodbye!")
        break
    try:
        guess = int(guess)
    except ValueError:
        print("Please enter a valid number.")
        continue
    
    guesses += 1

    if guess < lowest or guess > highest:
        print(f"Your guess is out of bounds! Please guess a number between {lowest} and {highest}.")
    elif guess < answer:
        print("Too low! Try again.")
    elif guess > answer:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You've guessed the correct number {answer} in {guesses} attempts.")
        print("Thanks for playing!")
        print("Goodbye!")
        is_guessing = False


if is_guessing:
    if guesses == 10:
        print("Game over!")
        print("Better luck next time!")
        print(f"The correct number was {answer}.")
        print("Thanks for playing!")
        print("Goodbye!")
    else:
        print("You quit the game.")
