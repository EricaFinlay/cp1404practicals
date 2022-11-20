"""
Erica Finlay
CP1404 2022 Prac 08

Test Taxi

The solutions branch in GitHub was consulted when completing this activity:
https://github.com/CP1404/Practicals/tree/solutions/prac_09
"""

from prac_09.unreliable_car import UnreliableCar


def main():
    """Test UnreliableCar class."""
    reliability_test_car = UnreliableCar("mini_van", 100, 50)
    reliability_test_car.drive(25)
    print(reliability_test_car)


main()
