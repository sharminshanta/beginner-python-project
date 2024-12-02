# Issue Reference: https://github.com/sharminshanta/beginner-python-project/issues/2

import random

def computer_guess(x):
    random_number = random.randrange(1, x)
    guess = 0

    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))

        if guess > random_number:
            print("Sorry, the number is high!")
        elif guess < random_number:
            print("Sorry, the number is low!")

    print(f"Yeap, computer guessed the number {guess}!")

print(computer_guess(5))