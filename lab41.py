#!/usr/bin/env python3

CHARACTER_QUESTION = "Which character do you want to know about?"
STAT_QUESTION = "Which statistic do you want to know about?"
MARVELCHARS = {
    "Starlord": {
        "real name": 
        "peter quill",
        "powers": "dance moves",
        "archenemy": "Thanos"
    },
    "Mystique": {
        "real name": 
        "raven darkholme","powers": 
        "shape shifter",
        "archenemy": "Professor X"
    },
    "Hulk": {
        "real name": "bruce banner",  
        "powers": "super strength", 
        "archenemy": "adrenaline"
    }
}

def prompt_user(question, options):
    """Prompt user to select a name from the given options"""
    while True:
        o = input_graceful(question + f" ({', '.join(options)}) ").upper()
        for valid_option in options:
            if o == valid_option.upper():
                return valid_option

def display_char_info(char_name, char_stat):
    char_stat_value = MARVELCHARS[char_name][char_stat]
    print(f"{char_name}'s {char_stat} is: {char_stat_value}")

def prompt_again():
    while True:
        option = input_graceful("Do you wish to try again? (y/n)").upper()
        if option in {"Y", "N"}:
            return option == "Y"

def input_graceful(message):
    try:
        user_input = input(message)
        return user_input
    except EOFError:
        print("\nThanks for coming!\n")
        exit()

def main():
    running = True
    while running:
        valid_characters = MARVELCHARS.keys()
        char_name = prompt_user(CHARACTER_QUESTION, valid_characters)

        valid_stats = MARVELCHARS[char_name].keys()
        char_stat = prompt_user(STAT_QUESTION, valid_stats)

        display_char_info(char_name, char_stat)

        running = prompt_again()
    print("Ok, bye!")

if __name__ == '__main__':
    main()
