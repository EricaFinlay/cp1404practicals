"""
CP1404 2022 Prac 02
Erica Finlay

Do From Scratch Exercises
Menu

Pseudocode:
MENU = (R)esult (S)tars (Q)uit

function main()
    get_valid_score()
    display MENU
    get user choice
    while choice != Q
        if choice == R
            determine_category(user_score)
            print(f"Your score is {category}.")
        else if choice == S
            print_line_of_stars(user_score)
        else
            display error message
        display MENU
        get user choice
    display farewell message


function get_valid_score()
    get user_score
    while user_score < 0 or user_score > 100
        display error message
        get user_score
    return user_score


function determine_category(user_score)
    if user_score >= 90
        category = excellent
    else if user_score >= 50
        category = passable
    else
        category = bad
    return category


function print_line_of_stars(user_score)
    number_of_rows = user_score // 10
    number_of_stars_in_final_row = user_score % 10
    for count in range of number_of_rows
        display 10 x stars
    display remainder of stars
"""

MENU = "(R)esult\n(S)tars\n(Q)uit"


def main():
    """Provide the category of a score and print that number of stars."""
    user_score = get_valid_score()
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "R":
            category = determine_category(user_score)
            print(f"Your score is {category}.")
        elif choice == "S":
            print_line_of_stars(user_score)
        else:  # Error message for invalid input
            print("Invalid input.  Please re-enter choice.")
        print(MENU)
        choice = input(">>> ").upper()
    print("Goodbye!")


def get_valid_score():
    """Ensure user input is valid."""
    user_score = int(input("What is your score: "))
    while user_score < 0 or user_score > 100:
        print("Invalid score.  Please try again.")
        user_score = int(input("What is your score: "))
    return user_score


def determine_category(user_score):
    """Determine the category of a score."""
    if user_score >= 90:
        category = "excellent"
    elif user_score >= 50:
        category = "passable"
    else:
        category = "bad"
    return category


def print_line_of_stars(user_score):
    """Print the number of stars of the user score in rows of 10."""
    number_of_rows = user_score // 10
    number_of_stars_in_final_row = user_score % 10
    for i in range(number_of_rows):
        print("* " * 10)
    print("* " * number_of_stars_in_final_row)
    print()


main()
