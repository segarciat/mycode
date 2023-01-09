#!/usr/bin/env python3
"""Author: Sergio Garcia

RPG where a player navigates through scary rooms
"""

import crayons

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

def main():
    """Drives the game application"""
    display_instructions()
    won = True
    while not won:
        # Display current room and options
        # Match option to an action
        # Determine results
        pass

if __name__ == '__main__':
    main()
