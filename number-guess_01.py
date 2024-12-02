# Number Guess Game
# Issue Reference: https://github.com/sharminshanta/beginner-python-project/issues/2

import random

def number_guess(guess_counter=3, number_range=10):
    print(f"Hello, welcome to the game. This is a number guessing game. \n You have only {guess_counter} times chances to guess the number.")

    number_to_guess = random.randrange(1, number_range)
    chances_to_guess = 0

    while chances_to_guess < guess_counter:
        chances_to_guess += 1
        user_guess = int(input("Please, enter your guess: "))

        if user_guess == number_to_guess:
            print(f"Congrats! You have guessed the number {user_guess} with {chances_to_guess} attempts")
            break
        elif user_guess > number_to_guess:
            print(f"{user_guess} is very high!")
        elif user_guess < number_to_guess:
            print(f"{user_guess} is very low!")
        # elif chances_to_guess >= guess_counter and user_guess != number_to_guess:
        #     print(f" Opps sorry! user_guess is better to next time. ")
        #     break

print(number_guess())