#!/usr/bin/python3
"""
Author: Sergio Garcia
"""


def main():
    """Request user's name and day of the week to print a greeting."""
    user_name = input("What is your name? ").strip()
    day_of_week = input("What day of the week is it? ").strip()

    print("Hello, " + user_name + "! Happy " +  day_of_week + "!")

if __name__ == '__main__':
    main()
