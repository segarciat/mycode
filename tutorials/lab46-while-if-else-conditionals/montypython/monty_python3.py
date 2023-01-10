#!/usr/bin/python3
"""Alta3 Research | RZFeeser
  Conditionals - Life of Brian guessing game without a while True loop."""

game_round = 0
answer = " "

while game_round < 3 and answer != "Brian" and answer != "shrubbery":
    game_round += 1     # increase the game_round counter by 1
    answer = input('Finish the movie title, "Monty Python\'s The Life of ______": ').strip()
    if answer.lower() == "Brian".lower(): # logic to check if user gave correct answer
        print("Correct!")
    elif answer.lower() == "shrubbery":
        print("You gave the super secret answer!")
    elif game_round == 3:    # logic to ensure game_round has not yet reached 3
        print("Sorry, the answer was Brian.")
    else:                 # if answer was wrong
        print("Sorry. Try again!")

