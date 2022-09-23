"""
CP1404 2022 Prac 02
Erica Finlay

Extension
More Temperatures

Pseudocode:
import random
NUMBER_OF_TEMPERATURES = 15

function main()
    open outfile
    for count in NUMBER_OF_TEMPERATURES
        select random temperature(-200, 200)
        display temperature in outfile
    close outfile
"""

import random

NUMBER_OF_TEMPERATURES = 15


def main():
    """Generate random temperatures and write to an outfile."""
    out_file = open("temps_input.txt", "w")
    for i in range(NUMBER_OF_TEMPERATURES):
        temperature = random.uniform(-200, 200)
        print(temperature, file=out_file)
    out_file.close()


main()
