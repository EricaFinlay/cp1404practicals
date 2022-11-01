"""
CP1404 2022 Prac 06
Erica Finlay

Do-from-scratch Exercises
Guitars!

Estimate:  1.5 hours
Actual:    2 hours

The solutions branch in GitHub was consulted when completing this activity:
https://github.com/CP1404/Practicals/tree/solutions/prac_06
"""

PRESENT_YEAR = 2022
VINTAGE_AGE = 50


class Guitar:
    """Guitar class for storing details of a guitar."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of a Guitar."""
        return f"{self.name} ({self.year}) : ${self.cost}"

    def get_age(self):
        """Get the age of a guitar from the PRESENT_YEAR."""
        return PRESENT_YEAR - self.year

    def is_vintage(self):
        """Determine if a guitar is vintage based on age."""
        return self.get_age() >= VINTAGE_AGE

    def __lt__(self, other):
        """Sort guitars based on year of release."""
        return self.year < other.year
