#!/usr/bin/env python3
"""Author: Sergio Garcia"""

def print_from_challenge():
    """Slices a with a sublist"""
    challenge = ["science", "turbo", ["goggles", "eyes"], "nothing"]
    goggles,  eyes = challenge[2]
    nothing = challenge[-1]
    
    print(f"My {eyes}! The {goggles} do {nothing}!")

def print_from_trial():
    """Slices a list with a dictionary"""
    trial = ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]
    goggles, eyes = tuple(trial[2].values())
    nothing = trial[-1]

    print(f"My {eyes}! The {goggles} do {nothing}!")

def print_from_nightmare():
    """Slices a list with dictionaries and subdictionaries"""
    nightmare = [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]
    goggles = nightmare[0]["kumquat"]
    eyes = nightmare[0]["user"]["name"]["first"]
    nothing = nightmare[0]["d"]

    print(f"My {eyes}! The {goggles} do {nothing}!")

if __name__ == '__main__':
    print_from_challenge()
    print_from_trial()
    print_from_nightmare()
