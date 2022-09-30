"""
CP1404 2022 Prac 03
Erica Finlay

Practice & Extension Work
Practice - ASCII Table

Plus - Extensions(ASCII Columns Challenge)

Pseudocode:
LOWER = 33
UPPER = 127

function main()
    get character
    convert_ascii_to_number(character)
    display character, ascii_code
    is_valid_input = False
    while not is_valid_input
        try
            get number between LOWER and UPPER
            if number < LOWER or number > UPPER
                display error message
            else
                is_valid_input = True
        except ValueError
            display error message
    convert_number_to_ascii(number)
    display number, letter
    # Version 1
    for count between LOWER and UPPER
        convert_number_to_ascii(number)
        display number, letter
    # Version 2
    get number_of_columns
    columns = 0
    for count of number  between LOWER and UPPER
        convert_number_to_ascii(number)
        display number, letter end = "     "
        columns += 1
        if columns == number_of_columns
            print()
            columns = 0


function convert_ascii_to_number(character)
    return ord(character)


function convert_number_to_ascii(number)
    return chr(number)
"""

LOWER = 33
UPPER = 127


def main():
    """Program to convert between characters and ASCII values and print a table showing values."""
    character = input("Enter a character: ")
    ascii_code = convert_ascii_to_number(character)
    print(f"The ASCII code for {character} is {ascii_code}.")
    is_valid_input = False
    while not is_valid_input:
        try:
            number = int(input(f"Enter a number between {LOWER} and {UPPER}: "))
            if number < LOWER or number > UPPER:
                print("This number is outside the required range.")
            else:
                is_valid_input = True
        except ValueError:
            print("Invalid (not an integer)")
    letter = convert_number_to_ascii(number)
    print(f"The character for {number} is {letter}.")
    number_of_columns = int(input("How many columns do you want the ASCII table to display in: "))
    columns = 0  # Prints ASCII table in columns (Extension Exercise)
    for number in range(LOWER, UPPER):
        letter = convert_number_to_ascii(number)
        print(f"{number:3}  -  {letter}", end="     ")
        columns += 1
        if columns == number_of_columns:
            print()
            columns = 0


def convert_ascii_to_number(character):
    """Convert an ASCII value to a number."""
    return ord(character)


def convert_number_to_ascii(number):
    """Convert a number to an ASCII value."""
    return chr(number)


main()
