#!/usr/bin/env python3

import requests
import html
import random
import crayons
import os
import time
import pprint

# https://opentdb.com/api.php?amount=10&category=25&difficulty=medium&type=multiple
QUESTIONS_URL = "https://opentdb.com/api.php"
CATEGORY_URL = "https://opentdb.com/api_category.php"
NUMBER_OF_QUESTIONS = 3
VALID_QUESTION_TYPES = {
    "Multiple Choice": "multiple",
    "True/False": "boolean"
}

def clear():
    os.system("clear")

def pause():
    """Pause for a bit"""
    time.sleep(3)

def get_questions(category_id, difficulty, question_type):
    print("Loading questions...")
    url = f"{QUESTIONS_URL}?amount={NUMBER_OF_QUESTIONS}"
    if category_id:
        url += f"&category={category_id}"
    if difficulty:
        url += f"&difficulty={difficulty}"
    if question_type:
        url += f"&type={question_type}"
    
    response = requests.get(url)
    if response.status_code != 200:
        print("Unable to get trivia questions")
        exit(1)

    data = response.json()
    if data['response_code'] == 1:
        print("Database was reached, but API did not have enough questions")
        exit(1)
    elif data['response_code'] != 0:
        print("Something else went wrong while getting trivia questions...")
        exit(1)
    return data["results"]

def get_categories():
    response = requests.get(CATEGORY_URL)
    data = response.json()
    categories = {category["name"]: category["id"] for category in data["trivia_categories"]}
    return categories

def prompt_user(question, choices, alternate=None):
    """Prompts a user with a question, and validates their answer against the choices"""
    while True:
        try:
            if alternate:
                choices_text = '\n'.join([f"({crayons.yellow(alt)}) {choice}" for alt, choice in zip(alternate, choices)])
            else:
                choices_text = '\n'.join(choices)
            answer = input(f"{crayons.cyan(question)}{choices_text}\n>").strip()
        except EOFError:
            print("Thanks for playing!")
            exit()

        if alternate and answer in alternate:
            answer = choices[alternate.index(answer)]

        if not answer or answer in choices:
            return answer

def pose_question(question):
    correct = html.unescape(question["correct_answer"])
    choices = [html.unescape(choice) for choice in (correct, *question["incorrect_answers"])]
    random.shuffle(choices)
        
    alternate = ('A', 'B', 'C', 'D')
    question = html.unescape(question["question"])
    answer = prompt_user(question + "\n", choices, alternate)

    if answer == correct:
        print(crayons.green("You got it!"))
    else:
        correct_letter = alternate[choices.index(correct)]
        print(crayons.yellow(f"Wrong. The correct answer is {correct_letter}: {correct}"))
    return answer == correct
        

def main():
    """Trivia application"""

    # Customization choices from user.
    valid_categories = get_categories()
    valid_types = ("Multiple Choice", "True/False")
    valid_difficulties = ("Easy", "Medium", "Hard")

    # Prompt user for optional customization
    clear()
    category = prompt_user("What category do you prefer?\n", list(valid_categories.keys()))
    clear()
    question_type = prompt_user("What question type would you like?\n", VALID_QUESTION_TYPES.keys())
    clear()
    difficulty = prompt_user("What difficulty do you prefer?\n", valid_difficulties).lower()

    # Convert to what API will expect
    category_id = valid_categories.get(category)
    question_type = VALID_QUESTION_TYPES.get(question_type)

    # Get all questions
    questions = get_questions(category_id, difficulty, question_type)

    # Begin trivia, keep track of score.
    score = 0
    for q in questions:
        #clear()
        got = pose_question(q)
        if got:
            score += 1
        #pause()
    print(f"You got {score} out of {len(questions)} questions correct")

if __name__ == '__main__':
    main()
