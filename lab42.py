#!/usr/bin/env python3

challenge= ["science", "turbo", ["goggles", "eyes"], "nothing"]


trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]


nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]

def print_from_challenge():
    goggles, eyes = challenge[2]
    nothing = challenge[-1]
    
    print(f"My {eyes}! The {goggles} do {nothing}!")

def print_from_trial():
    goggles, eyes = list(challenge[2])
    nothing = challenge[-1]

    print(f"My {eyes}! The {goggles} do {nothing}!")

def print_from_nightmare():
    goggles = nightmare[0]["kumquat"]
    eyes = nightmare[0]["user"]["name"]["first"]
    nothing = nightmare[0]["d"]

    print(f"My {eyes}! The {goggles} do {nothing}!")

if __name__ == '__main__':
    print_from_challenge()
    print_from_trial()
    print_from_nightmare()
