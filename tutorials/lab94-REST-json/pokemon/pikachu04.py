#!/usr/bin/python3

import requests
import pandas as pd

# define base URL
POKEURL = "http://pokeapi.co/api/v2/pokemon/"

def main():

    # Make HTTP GET request using requests, and decode
    # JSON attachment as pythonic data structure
    # Augment the base URL with a limit parameter to 1000 results
    pokemon = requests.get(f"{POKEURL}?limit=1000")
    pokemon = pokemon.json()

    # Loop through data, and print pokemon names
    for poke in pokemon["results"]:
        # Display the value associated with 'name'
        #print(poke["name"])
        print(poke.get("name"))

    all_pokemon = [p["name"] for p in pokemon["results"]]
    pokemon_df = pd.DataFrame({'pokemon': all_pokemon})
    print(pokemon_df)

    pokemon_df.to_excel('all_pokemon.xlsx', index=False)
    pokemon_df.to_json('all_pokemon.json', orient='records')
    pokemon_df.to_csv('all_pokemon.csv', index=False)

    print(f"Total number of Pokemon returned: {len(pokemon['results'])}")

if __name__ == "__main__":
    main()

