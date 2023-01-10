"""Author: Sergio Garcia"""

import mtgsdk
import crayons

def main():
    """Exprimenting with MTG SDK"""
    cards_4ed = mtgsdk.Card.where(set='4ed').all()
    print(len(cards_4ed))

    # Display card names and URLs.
    for card in cards_4ed[:5]:
        print(f"{card.name}\n\t{crayons.cyan(card.image_url)}\n")

if __name__ == '__main__':
    main()
