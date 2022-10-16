"""
CP1404 2022 Prac 05
Erica Finlay

CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# TODO: Reformat this file so the dictionary code follows PEP 8 convention
CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}


def main():
    """Print the state code for a state name."""
    print(CODE_TO_NAME)
    for state in CODE_TO_NAME:
        print(f"{state:3} is {CODE_TO_NAME[state]}")
    state_code = valid_input()
    while state_code != "":
        print(state_code, "is", CODE_TO_NAME[state_code])
        state_code = valid_input()


def valid_input():
    """Perform error checking on user input."""
    is_valid_input = False
    while not is_valid_input:
        try:
            state_code = input("Enter short state: ").upper()
            if state_code == "":
                break
            elif state_code not in CODE_TO_NAME:
                print("Invalid short state")
            else:
                is_valid_input = True
        except ValueError:
            print("Invalid short state")
    return state_code


main()
