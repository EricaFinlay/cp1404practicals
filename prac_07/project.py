"""
CP1404 2022 Prac 07
Erica Finlay

Do-from-scratch Exercises
Project Management Program
"""


class Project:

    def __init__(self, name="", start_date=None, priority=0, cost_estimate=0.0, completion_percentage=0):
        """Initialise a Project."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        """Return a string representation of a Project."""
        return f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, priority {self.priority}, estimate: ${self.cost_estimate}, " \
               f"completion: {self.completion_percentage}%"

    def __repr__(self):
        """Return a list of Project objects as a string."""
        return f"{self.name}\t{self.start_date.strftime('%d/%m/%Y')}\t{self.priority}\t{self.cost_estimate}\t{self.completion_percentage}"
