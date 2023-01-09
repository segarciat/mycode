#!/usr/bin/env python3
"""Author: Sergio Garcia"""

import random

class Player:
    """A player that can roll a die"""
    def __init__(self):
        self._rolls = []

    def roll(self):
        """Rolls a D6."""
        result = random.randint(1, 6)
        self._rolls.append(result)
        return result

    def get_rolls(self):
        """Returns a copy of the rolls thus far"""
        return list(self._rolls)


class FlipCheatD6(Player):
    """A player who cheats by cheats by flipping a die"""
    def roll(self):
        """Rolls a D6, and flips the result if unfavorable."""
        result = super().roll()
        # Replace last roll with value after flip.
        self._rolls[-1] = self._flip_die(result)
        return self._rolls[-1]

    def _flip_die(self, result):
        """When rolling 3 or lower, fip the die"""
        return result if result > 3 else 7 - result

def main():
    """Display results of rolling a fair die vs a flipped die"""
    player1 = Player()
    player2 = FlipCheatD6()

    for i in range(10):
        player1.roll()
        player2.roll()

    print(player1.get_rolls())
    print(player2.get_rolls())

if __name__ == '__main__':
    main()
