"""
CP1404 2022 Prac 09
Erica Finlay

CP1404/CP5632 Practical
Unreliable Car class

The solutions branch in GitHub was consulted when completing this activity:
https://github.com/CP1404/Practicals/tree/solutions/prac_09
"""
from prac_09.car import Car
from random import randint


class UnreliableCar(Car):
    """Unreliable version of a car."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar instance."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Assign random number that must be less than reliability to enable driving."""
        random_number = randint(0, 100)
        if random_number >= self.reliability:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven
