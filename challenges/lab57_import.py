#!/usr/bin/env python3
"""Author: Sergio Garcia"""

import html
import random

def prompt_user(message, options):
    """Prompts user to enter one of the given options"""
    while True:
        try:
            user_option = input(message).upper()
        except EOFError:
            print("Please come back!")
            exit()
        if user_option in options:
            return user_option

def main():
    """Unescape HTML to display trivia question, and prompt user for correct answer."""
    trivia= {
             "category": "Entertainment: Film",
             "type": "multiple",
             "question": "Which of the following is NOT a quote from the 1942 film Casablanca? ",
             "correct_answer": "&quot;Frankly, my dear, I don&#039;t give a damn.&quot;",
             "incorrect_answers": [
                 "&quot;Here&#039;s lookin&#039; at you, kid.&quot;",
                 "&ldquo;Of all the gin joints, in all the towns, in all the world, she walks into mine&hellip;&rdquo;",
                 "&quot;Round up the usual suspects.&quot;"
                ]
            }
    question = trivia["question"]

    # Create shuffled list of valid answers
    valid_answers = [trivia["correct_answer"], *trivia["incorrect_answers"]]
    random.shuffle(valid_answers)
    
    # Create corresponding letters for each of the choices
    option_letters = ("A", "B", "C", "D")

    # Display answer choices
    answer_choices = "\n".join([f"{letter}) {html.unescape(answer)}" for letter, answer in 
        zip(option_letters, valid_answers)])

    
    print(question)
    # print answers
    print(answer_choices)

    # Get choice from user
    letter_choice = prompt_user(f"Please choose one of: {' ,'.join(option_letters)} \n", option_letters)
    
    # Get answer corresponding to user's letter choice
    user_answer = valid_answers[option_letters.index(letter_choice)]
    if trivia["correct_answer"] == user_answer:
        print("Correct!")
    else:
        print("Unfortunately, your answer is incorrect")
        print(f"The correct choice was: {html.unescape(trivia['correct_answer'])}")

if __name__ == '__main__':
    main()
