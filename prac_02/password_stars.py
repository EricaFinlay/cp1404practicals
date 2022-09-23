"""
CP1404 2022 Prac 02
Erica Finlay

Walkthrough Example
Password Stars

Pseudocode:
function main()
    minimum_length_of_password = 5
    get_password(minimum_length_of_password)
    print_line_of_stars(password)

function print_line_of_stars(password)
    for count in range length of password
        print *'s

function get_password(minimum_length_of_password)
    get password
    while length of password < minimum_length_of_password
        display error message
        get password
    return password
"""


def main():
    """Print a line of stars of length of a password of minimum number of characters."""
    minimum_length_of_password = 5
    password = get_password(minimum_length_of_password)
    print_line_of_stars(password)


def print_line_of_stars(password):
    """Print a line of stars of length of a password."""
    for i in range(len(password)):
        print("*", end=" ")


def get_password(minimum_length_of_password):
    """Ensure a password is of minimum length."""
    password = input("Enter your password: ")
    while len(password) < minimum_length_of_password:
        print(f"This password is too short.  It must be at least {minimum_length_of_password} characters.")
        password = input("Enter your password: ")
    return password


main()
