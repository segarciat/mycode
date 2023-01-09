#!/usr/bin/env python3
"""Author: Sergio Garcia"""

def prompt_farm(valid_names):
    """Indefinitely ask user for a valid farm name"""
    while True:
        try:
            farm = input(f"Choose a farm: {', '.join(valid_names)}: ").upper()
            if farm in valid_names:
                return farm
        except EOFError: # User quit the problem while being prompted.
            print("\nPlease come back!")
            exit()

def main():
    """Display animals from a farm that the user chooses"""
    farms = [
        {"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
        {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
        {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}
    ]
    plants = {"carrots", "celery"}

    # Valid names are NE, W, SE, ...
    valid_names = tuple(farm["name"].split(" ")[0] for farm in farms)
    farm_name = prompt_farm(valid_names)

    # Find the farm with a matching name.
    for f in farms:
        if f["name"].upper().startswith(farm_name):
            farm = f

    # Display animals in that farm but not plants
    for animal in set(farm["agriculture"]) - plants:
        print(animal)

if __name__ == '__main__':
    main()
