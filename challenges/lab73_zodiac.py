#!/usr/bin/env python3
"""Author: Sergio Garcia"""

BASE_YEAR = 1960
ZODIAC = [
        ("Rat", "you are artistic, sociable, industrious, charming, and intelligent."),
        ("Ox", "you are strong, thorough, determined, loyal, and reliable."),
        ("Tiger", "you are courageous, enthusiastic, confident, charismatic, and a leader."),
        ("Rabbit", "you are vigilant, witty, quick-minded, and ingenious."),
        ("Dragon", "you are talented, powerful, lucky, and successfull."),
        ("Snake", "you are wise, like to work alone, and determined."),
        ("Horse", "you are animated, active, and energetic."),
        ("Sheep", "you are creative, resilient, gentle, mild-mannered, and shy."),
        ("Monkey", "you are sharp, smart, curious, and mischievious."),
        ("Rooster", "you are hardworking, resourceful, courageous, and talented."),
        ("Dog", "you are loyal, honest, cautious, and kind."),
        ("Pig", "you are a symbol of wealth, honesty, and practicality.")
]

def prompt_birthyear():
    """Get a birth year from the year in the YYYY format."""
    while True:
        try:
            year = input("Please enter your birth year in YYYY format, e.g. 2010:\n>").strip()
            if year.isnumeric() and int(year) > 0:
                return int(year)
        except EOFError:
            print("Please come back!")
            exit()

def get_zodiac(birth_year):
    """Returns a tuple containing the zodiac sign and description."""
    return ZODIAC[(birth_year - BASE_YEAR) % 12]

def main():
    """Collects a user's name and birthdate to display their zodiac."""
    usr_name = input("Please enter your name:\n>").strip().title()
    usr_date = prompt_birthyear()

    zodiac_sign, zodiac_description = get_zodiac(usr_date)
    print(f"{usr_name} your zodiac sign is {zodiac_sign}, {zodiac_description}")

if __name__ == '__main__':
    main()
