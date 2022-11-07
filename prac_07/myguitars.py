"""
CP1404 2022 Prac 07
Erica Finlay

Intermediate Exercises
More Guitars!
"""


class Guitar:
    """Guitar class for storing details of a guitar."""

    def __init__(self, name="", year=0, cost=0.0):
        """Initialise a Guitar."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of a Guitar."""
        return f"{self.name} ({self.year}) : ${self.cost}"

    def __lt__(self, other):
        """Sort guitars based on year of release."""
        return self.year < other.year

    def __repr__(self):
        return f"{self.name},{self.year},{self.cost}"


def main():
    """Display sorted list of guitars and allow user input of new purchases."""
    guitars = []
    in_file = open('guitars.csv', 'r')
    in_file.readline()
    for line in in_file:
        parts = line.strip().split(',')
        guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
        guitars.append(guitar)
    in_file.close()
    guitars.sort()
    print("This is your list of guitars:")
    for guitar in guitars:
        print(guitar)
    print()
    print("It's time to add your new purchases!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)
        print(new_guitar, "added to file.")
        name = input("Name: ")
    guitars.sort()
    print()
    print("This is your updated list of guitars:")
    for guitar in guitars:
        print(guitar)
    out_file = open('guitars.csv', "w")
    for guitar in guitars:
        print(repr(guitar), file=out_file)
    out_file.close()


main()
