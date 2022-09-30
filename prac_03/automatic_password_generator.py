"""
CP1404 2022 Prac 03
Erica Finlay

Extension
Automatic Password Generator

Pseudocode:
LOWER = abcdefghijklmnopqrstuvwxyz
UPPER = ABCDEFGHIJKLMNOPQRSTUVWXYZ
DIGITS = 1234567890
CHARACTERS = !@#$%^&*()_-=+`~,./'[]<>?{}|\\

function main()
    password_choices = []
    get length_of_password
    lower_case = get confirmation or refusal of use of lower case letters
    if lower_case == "Y"
        letter_to_add_to_password_choices = "L"
        append "L" to password_choices
    upper_case = get confirmation or refusal of use of upper case letters
    if upper_case == "Y"
        letter_to_add_to_password_choices = "U"
        append "U" to password_choices
    numeric = get confirmation or refusal of use of numeric digits
    if numeric == "Y"
        letter_to_add_to_password_choices = "D"
        append "D" to password_choices
    special_characters = get confirmation or refusal of use of special characters
    if special_characters == "Y"
        letter_to_add_to_password_choices = "C"
        append "C" to password_choices
    password_format = ""
    for the count of length_of_password
        select a random letter from password_choices
        password_format = password_format + random_choice
    password = ""
    for kind in password_format
        if kind == "L"
            select a random letter from LOWER and add to password
        else if kind == "U"
            select a random letter from UPPER and add to password
        else if kind == "D"
            select a random letter from DIGITS and add to password
        else
            select a random letter from CHARACTERS and add to password
    display password
"""

import random

LOWER = "abcdefghijklmnopqrstuvwxyz"
UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DIGITS = "1234567890"
CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    """Program will generate random password of selected length containing selected character groups."""
    password_choices = []
    length_of_password = int(input("Length of password: "))
    lower_case = input("Do you want it to contain lower case letters (Y or N)? ")
    if lower_case == "Y":
        letter_to_add_to_password_choices = "L"
        password_choices.append(letter_to_add_to_password_choices)
    upper_case = input("Do you want it to contain upper case letters (Y or N)? ")
    if upper_case == "Y":
        letter_to_add_to_password_choices = "U"
        password_choices.append(letter_to_add_to_password_choices)
    numeric = input("Do you want it to contain numeric digits (Y or N)? ")
    if numeric == "Y":
        letter_to_add_to_password_choices = "D"
        password_choices.append(letter_to_add_to_password_choices)
    special_characters = input("Do you want it to contain special characters (Y or N)? ")
    if special_characters == "Y":
        letter_to_add_to_password_choices = "C"
        password_choices.append(letter_to_add_to_password_choices)
    password_format = ""
    for i in range(length_of_password):
        random_choice = random.choice(password_choices)
        password_format += random_choice
    password = ""
    for kind in password_format:
        if kind == "L":
            password += random.choice(LOWER)
        elif kind == "U":
            password += random.choice(UPPER)
        elif kind == "D":
            password += random.choice(DIGITS)
        else:
            password += random.choice(CHARACTERS)
    print(password)


main()
