"""
Erica Finlay
CP1404 2022 Prac 09

Test Taxi

The solutions branch in GitHub was consulted when completing this activity:
https://github.com/CP1404/Practicals/tree/solutions/prac_09
"""

from prac_09.taxi import Taxi


def main():
    """Test a taxi."""
    my_taxi = Taxi("Prius 1", 100)
    my_taxi.drive(40)
    print(my_taxi)
    my_taxi.start_fare()
    my_taxi.drive(100)
    print(my_taxi)


main()
