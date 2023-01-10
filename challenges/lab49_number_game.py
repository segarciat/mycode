#!/usr/bin/env python3
"""Number guessing game! User has 5 chances to guess a number between 1 and 100!"""

import random

MAX_ROUNDS = 5
MIN = 1
MAX = 100

def prompt_number():
    """Prompts a user for a number between 1 and 100"""
    while True:
        try:
            n = input(f"Guess a number between {MIN} and {MAX}\n>").strip()
            if n.isnumeric() and MIN <= int(n) <= MAX:
                return int(n)
        except EOFError:
            print("Thanks for playing!")
            exit()


def main():
    """Prompts a user to guess a number until 5 attempts have been made."""
    num = random.randint(MIN, MAX)
    rounds = 0

    print("Welcome to 'Guess the Number'. You've got 5 guesses.")
    while rounds < MAX_ROUNDS:
        guess = prompt_number()
        if guess > num:
            print("Too high!")
        elif guess < num:
            print("Too low!")
        else:
            print("Correct!")
            break
        rounds += 1

if __name__ == '__main__':
    main()
