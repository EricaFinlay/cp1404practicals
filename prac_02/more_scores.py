"""
CP1404 2022 Prac 02
Erica Finlay

Practice and Extension Work
More Scores

Pseudocode:
import random

function main()
    get number of scores
    open outfile
    for count in range of number_of_scores
        get random score
        determine_category(score)
        display score, category in outfile
    close outfile

function determine_category(score)
    if score >= 90
        category = excellent
    else if score >= 50
        category = passable
    else
        category = bad
    return category
"""

import random


def main():
    """Print  a user chosen number of random scores and their categories to an outfile."""
    number_of_scores = int(input("Enter number of scores: "))
    out_file = open("results.txt", "w")
    for i in range(number_of_scores):
        score = random.randint(0, 100)
        category = determine_category(score)
        print(f"{score} is {category.title()}", file=out_file)
    out_file.close()


def determine_category(score):
    """Determine the category of a score."""
    if score >= 90:
        category = "excellent"
    elif score >= 50:
        category = "passable"
    else:
        category = "bad"
    return category


main()
