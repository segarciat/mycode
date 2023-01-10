#!/usr/bin/env python3

import requests

MIN_DEX_NO = 1
MAX_DEX_NO = 151

def get_pokenum():
    """Prompts user for a valid pokedex number"""
    while True:
        dex_no = input(f"Pick a number between {MIN_DEX_NO} and {MAX_DEX_NO}: ").strip()
        if dex_no.isnumeric() and MIN_DEX_NO <= dex_no <= MAX_DEX_NO:
            return dex_no

def main():
    pokenum = input("Pick a number between 1 and 151!\n>")
    pokemon = requests.get("https://pokeapi.co/api/v2/pokemon/" + pokenum).json()

    print(pokemon["name"])

    # Image of the pokemon found.
    image_url = pokemon["sprites"]["front_default"]
    image_name = image_url.split('/')[-1]
    print(image_url)
    
    # Download the image
    image_data = requests.get(image_url)
    with open(f"/home/student/static/{image_name}", mode="wb") as f:
        f.write(image_data.content)

    # Move names.
    for move in pokemon["moves"]:
        print(move["move"]["name"])

    # Number of games the Pokemon has appeared in
    print(f"Appeared in {len(pokemon['game_indices'])} games")



main()

