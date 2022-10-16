"""
CP1404 2022 Prac 05
Erica Finlay

Intermediate Exercises
Hex Colours

Pseudocode:
COLOUR_NAME_TO_CODE = {"Absolute Zero": "#0048ba", "Baby Blue": "#89cff0", "Cadet Grey": "#91a3b0", "Daffodil":
                       "#ffff31", "Earth Yellow": "#e1a95f", "Falu Red": "#801818", "Go Green": "#00ab66",
                       "Han Blue": "#446ccf", "Iceberg": "#71a6d2", "Jade": "#00a86b"}

function main()
    display COLOUR_NAME_TO_CODE
    get colour_name
    while colour_name != ""
        if colour_name in COLOUR_NAME_TO_CODE:
            display colour_name and code
        else
            display error message
        get colour_name
"""

COLOUR_NAME_TO_CODE = {"Absolute Zero": "#0048ba", "Baby Blue": "#89cff0", "Cadet Grey": "#91a3b0", "Daffodil":
    "#ffff31", "Earth Yellow": "#e1a95f", "Falu Red": "#801818", "Go Green": "#00ab66",
                       "Han Blue": "#446ccf", "Iceberg": "#71a6d2", "Jade": "#00a86b"}


def main():
    """Prints the colour code for a user inputted colour."""
    print(COLOUR_NAME_TO_CODE)
    colour_name = input("Enter a colour name: ").title()
    while colour_name != "":
        if colour_name in COLOUR_NAME_TO_CODE:
            print(colour_name, "is", COLOUR_NAME_TO_CODE[colour_name])
        else:
            print("This colour is not in this dictionary.")
        colour_name = input("Enter a colour name: ").title()


main()
