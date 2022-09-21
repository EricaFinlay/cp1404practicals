"""
CP1404 2022 Prac 01
Erica Finlay

Extension
1. Menu-driven number sequence generator

Pseudocode:
MENU = (E)ven numbers (O)dd numbers (S)quare roots (Q)uit"
function main()
    get_valid_input()
    display MENU
    get menu choice
    while user_choice != Q
        if user_choice == E
            if x_value < y_value
                if x_value % 2 == 0
                    for count from x_value to y_value + 1 in 2's
                        display count
                else
                    for count from x_value + 1 to y_value + 1 in 2's
                        display count
            else
                if x_value % 2 == 0
                    for count from x_value to y_value - 1 in -2's
                        display count
                else
                    for count from x_value -1 to y_value - 1 in -2's
                        display count
        else if user_choice == O
            if x_value < y_value
                if x_value % 2 == 0
                    for count from x_value + 1 to y_value in 2's
                        display count
                else
                    for count from x_value to y_value in 2's
                        display count
            else
                if x_value % 2 == 0
                    for count from x_value - 1 to y_value in -2's
                        display count
                else
                    for count from x_value to y_value in -2's
                        display count
        elif user_choice == S
            if x_value < y_value
                for count from x_value to y_value + 1
                    square_root_value = i ** 2
                    display square root
            else
                for count from x_value to y_value - 1 in -1's
                    square_root_value = i ** 2
                    display square root
        else
            display error message
        display MENU
        get menu choice
    display quit message


function get_valid_input()
    get x_value
    get y_value
    while x_value == y_value
        display error message
            get x_value
            get y_value
    return x_value, y_value
"""

MENU = "(E)ven numbers\n(O)dd numbers\n(S)quare roots\n(Q)uit"


def main():
    x_value, y_value = get_valid_input()
    print(MENU)
    user_choice = input("Please choose a Menu option: ").upper()
    while user_choice != "Q":
        if user_choice == "E":
            if x_value < y_value:
                if x_value % 2 == 0:
                    for i in range(x_value, y_value + 1, 2):
                        print(i, end=", ")
                    print()
                else:
                    for i in range(x_value + 1, y_value + 1, 2):
                        print(i, end=", ")
                    print()
            else:
                if x_value % 2 == 0:
                    for i in range(x_value, y_value - 1, -2):
                        print(i, end=", ")
                    print()
                else:
                    for i in range(x_value - 1, y_value - 1, -2):
                        print(i, end=", ")
                    print()
        elif user_choice == "O":
            if x_value < y_value:
                if x_value % 2 == 0:
                    for i in range(x_value + 1, y_value, 2):
                        print(i, end=", ")
                    print()
                else:
                    for i in range(x_value, y_value, 2):
                        print(i, end=", ")
                    print()
            else:
                if x_value % 2 == 0:
                    for i in range(x_value - 1, y_value, -2):
                        print(i, end=", ")
                    print()
                else:
                    for i in range(x_value, y_value, -2):
                        print(i, end=", ")
                    print()
        elif user_choice == "S":
            if x_value < y_value:
                for i in range(x_value, y_value + 1):
                    square_root_value = i ** 2
                    print(square_root_value, end=", ")
                print()
            else:
                for i in range(x_value, y_value - 1, -1):
                    square_root_value = i ** 2
                    print(square_root_value, end=", ")
                print()
        else:
            print("That's an invalid Menu choice.")
        print(MENU)
        user_choice = input("Please choose a Menu option: ").upper()
    print("Goodbye!")


def get_valid_input():
    x_value = int(input("Please choose your first number: "))
    y_value = int(input("Please choose your second number: "))
    while x_value == y_value:
        print("Your numbers are equal.  Please choose separate numbers.")
        x_value = int(input("Please choose your first number: "))
        y_value = int(input("Please choose your second number: "))
    return x_value, y_value


main()
