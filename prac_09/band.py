"""
CP1404 2022 Prac 09
Erica Finlay

The following sources were consulted in the writing of this program:
    1. Program provided by student Kath Paton during Online Collab Session 21.11.22.
    2. Discussion provided by Lindsay Ward during Online Collab Session 21.11.22
"""


class Band:
    """Represent a Band object."""

    def __init__(self, name):
        """Initialise a Band."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of a Band."""
        return f"{self.name} ({' ,'.join([str(musician) for musician in self.musicians])})"

    def __repr__(self):
        """Return a string representation of a Band, showing the variables."""
        return str(vars(self))

    def play(self):
        """Return a string showing the musician playing their first (or no) instrument."""
        for musician in self.musicians:
            print(musician.play())
        return ""

    def add(self, musician):
        """Add a musician to the Musicians list."""
        self.musicians.append(musician)
