import random

print("******************************")
print("**Welcome to Guessing Number**")
print("******************************")

lowest = 0
highest = 100
answer = random.randint(lowest, highest)
guesses = 0
max_attempts = 10

print("Welcome to the Guessing Game!")
print(f"Guess a number between {lowest} and {highest}.")
print("You have 10 attempts to guess the correct number.")
print("If you want to quit, type 'exit' at any time.")
print("Good luck!")

while guesses < max_attempts:
    user_input = input(f"Attempt {guesses + 1}: Enter your guess: ")
    if user_input.lower() == 'exit':
        print("\nYou exited the game. Thanks for playing!")
        break
    try:
        guess = int(user_input)
    except ValueError:
        print("Invalid input. Please enter a number.\n")
        continue
    if guess < lowest or guess > highest:
        print(f"Out of bounds! Guess a number between {lowest} and {highest}.\n")
        continue
    
    guesses += 1

    if guess < lowest or guess > highest:
        print(f"Your guess is out of bounds! Please guess a number between {lowest} and {highest}.")
    elif guess < answer:
        print("Too low! Try again.")
    elif guess > answer:
        print("Too high! Try again.")
    else:
        print(f"\n🎉 Congratulations! You guessed the number {answer} in {guesses} attempts.")
        break

else:
    print("\n🚫 Game over!")
    print(f"The correct number was {answer}.")
print("Goodbye!")