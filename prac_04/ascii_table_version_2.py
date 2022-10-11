"""
CP1404 2022 Prac 04
Erica Finlay

Practice & Extension Work
Extension - get_number function
"""

LOWER = 10
UPPER = 50


def main():
    """Program to convert between characters and ASCII values and print a table showing values."""
    character = input("Enter a character: ")
    ascii_code = convert_ascii_to_number(character)
    print(f"The ASCII code for {character} is {ascii_code}.")
    number = get_number(LOWER, UPPER)
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


def get_number(LOWER, UPPER):
    """Check that a valid integer within range is entered."""
    is_valid_input = False
    while not is_valid_input:
        try:
            number = int(input(f"Enter a number ({LOWER} - {UPPER}): "))
            if number < LOWER or number > UPPER:
                print("This number is outside the required range.")
            else:
                is_valid_input = True
        except ValueError:
            print("Please enter a valid number!")
    return number


main()
