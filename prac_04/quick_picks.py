"""
CP1404 2022 Prac 04
Erica Finlay

Do-from-scratch Exercises
"Quick Pick" Lottery Ticket Generator

Pseudocode:
import random

MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 45
NUMBERS_PER_LINE = 6

function main()
    get number_of_quick_picks
    quick_picks = empty list
    while len(quick_picks) < (number_of_quick_picks * NUMBERS_PER_LINE)
        quick_pick = random integer between MINIMUM_NUMBER and MAXIMUM_NUMBER
        if quick_pick in quick_picks
            delete quick_pick
        else
            append quick_pick to quick_picks
    length_of_row = 0
    for quick_pick in quick_picks
        display quick_pick
        length_of_row = length_of_row + 1
        if length_of_row == NUMBERS_PER_LINE
            go to new line
            length_of_row = 0
"""

import random

MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 45
NUMBERS_PER_LINE = 6


def main():
    """Display quick pick numbers in table format."""
    number_of_quick_picks = int(input("How many quick picks? "))
    quick_picks = []
    while len(quick_picks) < (number_of_quick_picks * NUMBERS_PER_LINE):
        quick_pick = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
        if quick_pick in quick_picks:
            del quick_pick
        else:
            quick_picks.append(quick_pick)
    length_of_row = 0
    for quick_pick in quick_picks:
        print(f"{quick_pick:>2}", end="  ")
        length_of_row += 1
        if length_of_row == NUMBERS_PER_LINE:
            print()
            length_of_row = 0


main()
