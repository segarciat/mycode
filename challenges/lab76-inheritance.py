#!/usr/bin/env python3
"""Author: Sergio Garcia"""

class D6Die:
    def roll(self):
        return random.randint(1, 6)


class FlipCheatD6:
    def roll(self):
        result = super.roll()
        return result if result > 3 else 7 - result
