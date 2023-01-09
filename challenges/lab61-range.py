#!/usr/bin/env python3
"""Author: Sergio Garcia"""


LYRICS = """{0} bottles of beer on the wall!
{0} bottles of beer on the wall! {0} bottles of beer! You take one down, pass it around!"""
MAX = 100

def get_count():
    """Requests a positive integer from the user"""
    while True:
        try:
            n = input("Please provide a positive integer no greater than 100: ")
            if n.isnumeric() and 1 <= int(n) <= MAX:
                return int(n)
        except EOFError:
            print("Please come back again!")
            exit()

def sing_from(n):
    """Sing beer song starting at n"""
    for i in range(n, 0, -1):
        print(LYRICS.format(i))

def main():
    """Sing the beer song starting at the number provided by the user."""
    n = get_count()
    sing_from(n)

if __name__ == '__main__':
    main()

