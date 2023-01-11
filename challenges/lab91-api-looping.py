#!/usr/bin/env python3
"""Author: Sergio Garcia"""

import requests
import crayons

MIN_DEX_NO = 1
MAX_DEX_NO = 151
MAX_MOVES_SHOWN = 5
IMAGE_SAVE_PATH = "/home/student/static/{0}"

def get_pokenum():
    """Prompts user for a valid pokedex number"""
    while True:
        dex_no = input(f"Pick a number between {MIN_DEX_NO} and {MAX_DEX_NO}: ").strip()
        if dex_no.isnumeric() and MIN_DEX_NO <= dex_no <= MAX_DEX_NO:
            return dex_no

def capitalize(text, delimiter):
    """Capitalizes words in multi-word string separated by delimiter"""
    all_words = [word.capitalize() for word in text.split(delimiter)]
    return " ".join(all_words)

def download_image(url):
    """Saves image located at URl to a specified path"""
    save_path = IMAGE_SAVE_PATH.format(f"pokemon_{url.split('/')[-1]}") 
    print(f"Saving {crayons.cyan(url)} to {crayons.yellow(save_path)}")
    image_data = requests.get(url)
    with open(save_path, mode="wb") as f:
        f.write(image_data.content)

def display_moves(all_moves):
    """Displays up to a preconfigured number of moves"""
    print(crayons.yellow(f"Moves: {MAX_MOVES_SHOWN} of {len(all_moves)}"))
    for move in all_moves[:MAX_MOVES_SHOWN]:
        move_name = capitalize(move["move"]["name"], "-")
        print(f"\t{move_name}")

def main():
    """Prints information about a Pokemon"""
    pokenum = input("Pick a number between 1 and 151!\n>")
    pokemon = requests.get("https://pokeapi.co/api/v2/pokemon/" + pokenum).json()

    poke_name = capitalize(pokemon["name"], "-")
    print(crayons.green(poke_name))

    # Download the image.
    download_image(pokemon["sprites"]["front_default"])

    # Show up to 5 move names
    
    display_moves(pokemon["moves"])

    # Number of games the Pokemon has appeared in
    number_of_games = len(pokemon['game_indices'])
    print(crayons.yellow(f"Appeared in {number_of_games} games"))



if __name__ == '__main__':
    main()
