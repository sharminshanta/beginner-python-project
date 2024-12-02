# Issue Reference: https://github.com/sharminshanta/beginner-python-project/issues/3

import random

def play():
    user_choice = input("'R' for Rock, 'P' for Paper, 'S' for Scissor: ")
    computer_choice = random.choice(["R", "P", "S"])

    if user_choice == computer_choice:
        return "It\'s a tie!"

    if is_win(user_choice, computer_choice):
        return "You win!"

    return "You lost!"

def is_win(user, computer):
    if (user == 'R' and computer == 'S') \
            or (user == 'P' and computer == 'R') \
            or (user == 'S' and computer == 'P'):
        return True

print(play())