#!/usr/bin/python3
"""
segarciat - Lab 18
"""


def greeting():
    """
    Request user's name and day of the week to print a greeting.
    """
    user_name = input("What is your name? ")
    day_of_week = input("What day of the week is it? ")

    print("Hello, " + user_name + "! Happy " +  day_of_week + "!")

if __name__ == '__main__':
    greeting()
