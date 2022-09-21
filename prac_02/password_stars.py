"""
CP1404 2022 Prac 02
Erica Finlay

Walkthrough Example
Password Stars

Pseudocode:
minimum_length_of_password = 5
get password
while length of password < minimum_length_of_password
    display error message
    get password
for count in range of length of password
    display *
"""

def main():
    minimum_length_of_password = 5
    password = get_password(minimum_length_of_password)
    print_line_of_stars(password)


def print_line_of_stars(password):
    for i in range(len(password)):
        print("*", end=" ")


def get_password(minimum_length_of_password):
    password = input("Enter your password: ")
    while len(password) < minimum_length_of_password:
        print(f"This password is too short.  It must be at least {minimum_length_of_password} characters.")
        password = input("Enter your password: ")
    return password


main()
