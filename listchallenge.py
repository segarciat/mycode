#!/usr/bin/python3

def main():
    heroes= ["Spiderman", "Batman", "Black Panther", "Wonder Woman", "Storm"]
    # PART 1
    # Print out your favorite character from this list! The output would look something like:
    # My favorite character is Black Panther!
    favorite = heroes[0]
    print(f"My favorite character is {favorite}!")

    # PART 2
    # Ask the user to pick a number between 1 and 100.
    # Convert the input into an integer.
    while True:
        n = input("Pick a number between 1 and 100: ")
        if n.isnumeric() and 1 <= int(n) <= 100:
            n = int(n)
            break
    print(f"You inputted {n}")
    
    
    nums= [1, -5, 56, 987, 0]
    # PART 3
    # check out https://docs.python.org/3/library/functions.html or go to Google
    # use a built-in function to find which integer in nums is the biggest.
    # then, print out that number!
    print(max(nums))

