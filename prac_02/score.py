"""
CP1404 2022 Prac 02
Erica Finlay

Refactoring
Scores

Pseudocode:
import random module

function main()
    get score
    while score < 0 or score > 100
        display error message
        get score
    category = determine_category(score)
    display message, category
    random_score = determine_category(random integer between 0 and 100)
    display random_score

function determine_category(score)
    if score >= 90
        category = "excellent"
    else if score >= 50
        category = "passable"
    else
        category = "bad"
    return category
"""

import random


def main():
    """Take a valid user score, check its category and print it, plus generate a random score."""
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score.  Please try again.")
        score = float(input("Enter score: "))
    category = determine_category(score)
    print(f"Your score is {category}.")
    random_score = determine_category(random.randint(0, 100))
    print(f"Your random score category is {random_score}.")


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
