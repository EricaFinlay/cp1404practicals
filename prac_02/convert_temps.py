"""
CP1404 2022 Prac 02
Erica Finlay

Extension
More Temperatures

Pseudocode:
function main()
    get_valid_input()
    open file_in
    open file_out
    for line in file_in
        if user_choice == C
            celsius = line
            convert_celsius_to_fahrenheit(celsius)
            display fahrenheit in file_out
        else:
            fahrenheit = line
            convert_fahrenheit_to_celsius(fahrenheit)
            display celsius in file_out
    close file_in
    close file_out


function get_valid_input()
    get user_choice
    while user_choice != F and user_choice != C
        display error message
        get user_choice
    return user_choice


function convert_fahrenheit_to_celsius(fahrenheit)
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


function convert_celsius_to_fahrenheit(celsius)
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit
"""


def main():
    """Convert temperatures from fahrenheit to celsius and vice versa and print to an outfile."""
    user_choice = get_valid_input()
    in_file = open("temps_input.txt")
    out_file = open("temps_output.txt", "w")
    for line in in_file:
        if user_choice == "C":
            celsius = float(line.strip())
            fahrenheit = convert_celsius_to_fahrenheit(celsius)
            print(f"The Fahrenheit temperature of {line} is {fahrenheit}", file=out_file)
        else:
            fahrenheit = float(line.strip())
            celsius = convert_fahrenheit_to_celsius(fahrenheit)
            print(f"The Celsius temperature of {line} is {celsius}.", file=out_file)
    in_file.close()
    out_file.close()


def get_valid_input():
    """Ensure user input is valid."""
    user_choice = input("Is your input file fahrenheit or celsius?  (Please enter F or C): ").upper()
    while user_choice != "F" and user_choice != "C":
        print("Invalid input")
        user_choice = input("Is your input file fahrenheit or celsius?  (Please enter F or C): ").upper()
    return user_choice


def convert_fahrenheit_to_celsius(fahrenheit):
    """Convert temperatures from fahrenheit to celsius."""
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


def convert_celsius_to_fahrenheit(celsius):
    """Convert temperatures from celsius to fahrenheit."""
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


main()
