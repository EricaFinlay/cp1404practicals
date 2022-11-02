"""
CP1404 2022 Prac 06
Erica Finlay

Intermediate Exercises
Programming Language

Estimate:  1 hour
Actual:    1.5 hours

The solutions branch in GitHub was consulted when completing this activity:
https://github.com/CP1404/Practicals/tree/solutions/prac_06
"""


class ProgrammingLanguage:
    """Provide information about programming languages."""

    def __init__(self, name, typing, reflection, year):
        """Programming Language constructs for given values."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return string representation of a given language."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """Determine if language is dynamic."""
        return self.typing == "Dynamic"
