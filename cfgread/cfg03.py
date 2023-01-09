#!/usr/bin/env python3
import os

def main():
    filename = input("Provide the name of a file you wish you load: ")
    if not os.path.exists(filename):
        print("The file you provided does not exist")
        exit(1)

    ## create file object in "r"ead mode
    with open(filename, "r") as configfile:
        ## readlines() creates a list by reading target
        ## file line by line
        configlist = configfile.readlines()
    
    ## file was just auto closed (no more indenting)
    
    ## each item of the list now has the "\n" characters back
    print(configlist)
    print(f"Number of lines: {len(configlist)}")

if __name__ == '__main__':
    main()
