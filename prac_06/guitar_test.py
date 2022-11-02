"""
CP1404 2022 Prac 06
Erica Finlay

Do-from-scratch Exercises
Guitars!

The solutions branch in GitHub was consulted when completing this activity:
https://github.com/CP1404/Practicals/tree/solutions/prac_06
"""

from prac_06.guitar import Guitar

PRESENT_YEAR = 2022


def run_tests():
    """Test for Guitar class."""
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40

    guitar = Guitar(name, year, cost)
    another = Guitar("Another Guitar", 1990, 20000.00)

    print(f"{guitar.name} get_age() - Expected {100}. Got {guitar.get_age()}")
    print(f"{another.name} get_age() - Expected {32}. Got {another.get_age()}")
    print()
    print(f"{guitar.name} is_vintage() - Expected {True}. Got {guitar.is_vintage()}")
    print(f"{another.name} is_vintage() - Expected {False}. Got {another.is_vintage()}")


if __name__ == '__main__':
    run_tests()
