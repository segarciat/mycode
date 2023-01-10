#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   Conditionals - Life of Brian guessing game using a while True loop."""


def main():
    """Movie guessing game"""
    game_round = 0
    while True:
        game_round += 1
        print('Finish the movie title: "Monty Python\'s The Life of ______"')
        answer = input("Your guess--> ")
        if answer == 'Brian':
            print('Correct')
            break
        elif game_round == 3:
            print('Sorry, the answer was Brian.')
            break
        else:
            print('Sorry! Try again!')

if __name__== '__main__':
    main()
