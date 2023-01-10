#!/usr/bin/env python3
"""Author: Sergio Garcia

RPG where a player navigates through scary rooms
"""

import crayons
import json
import os

ROOMS_FILE = "rooms.json"

def clear():
    """Clears the screen."""
    command = 'cls' if os.name == 'nt' else 'clear'
    os.system(command)

def display_instructions():
    """Show instructions upon starting the game"""
    print(f'''
    {crayons.green("Welcome to SG-RPG")}
    =================
    {crayons.cyan("Objective")}:
    \t Get to the Garden with the key and potion on hand.
    
    {crayons.cyan("Commands")}:
    \t go  <direction>: Each room will show valid directions to navigate.
    \t get <item>     : Each room will show valid items that can be picked up.

    {crayons.red("Losing Condition")}:
    \t Careful! If you encounter the monster, you will {crayons.yellow("lose")}!
    ''')

def load_rooms():
    """Loads the rooms that player can navigate through as a dictionary"""
    try:
        with open(ROOMS_FILE, 'r', encoding="utf8") as f:
            return json.load(f)
    except json.decoder.JSONDecodeError as e:
        print("Room file formatting is invalid")
        print(e)
    except Exception as e:
        print("Something went wrong")
    exit(1)

def main():
    """Drives the game application"""
    clear()
    display_instructions()
    rooms = load_rooms()
    print(rooms)
    won = True
    while not won:
        # Display current room and options
        # Match option to an action
        # Determine results
        pass

if __name__ == '__main__':
    main()
