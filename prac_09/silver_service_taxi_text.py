"""
CP1404 2022 Prac 09
Erica Finlay

Silver Service Taxi Test

The solutions branch in GitHub was consulted when completing this activity:
https://github.com/CP1404/Practicals/tree/solutions/prac_09
"""

from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    """Test the SilverServiceTaxi class."""
    new_taxi = SilverServiceTaxi("Test Taxi", 50, 2)
    new_taxi.drive(18)
    print(new_taxi)
    print(new_taxi.get_fare())


main()
