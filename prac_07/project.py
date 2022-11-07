"""
CP1404 2022 Prac 07
Erica Finlay

Do-from-scratch Exercises
Project Management Program
"""

class Project:
    """Guitar class for storing details of a guitar."""

    def __init__(self, name="", start_date=0, priority=0, cost_estimate=0, completion_percentage=0):
        """Initialise a Project."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        """Return a string representation of a Project."""
        return f"{self.name} was started in {self.start_date} with a priority of {self.priority}, a cost estimate" \
               f"of {self.cost_estimate}, and is currently {self.completion_percentage} completed."
