#!/usr/bin/env python3
"""
segarciat | Prompt for a number from user
"""
import random

def prompt_for_number(max):
    """
    Prompts for number between 1 and max.
    Converts to 0-base index.
    """
    while True:
        num = input(f"Please provide a number between 1 and {max}: ")
        if num.isnumeric() and 1 <= int(num) <= max:
            break
    return int(num) - 1

def main():
    """runtime"""
    wordbank = ['indentation', 'spaces']
    tlgstudents= ['Albert', 'Anthony', 'Brenden', 'Craig', 'Deja', 'Elihu', 'Eric', 'Giovanni', 'James', 'Joshua', 
            'Maria', 'Mohamed', 'PJ', 'Philip', 'Sagan', 'Suchit', 'Meka', 'Trey', 'Winton', 'Xiuxiang', 'Yaping']

    # add the integer 4 to the wordbank list
    wordbank.append(4)

    # request a number between 0 and 20 from the user.
    num = prompt_for_number(len(tlgstudents))

    # Get student name base on user's input.
    student_name = tlgstudents[num]
    # student_name = random.choice(tlgstudents)

    print(f"{student_name} always uses {wordbank[2]} {wordbank[1]} to indent.")

if __name__ == '__main__':
    main()
