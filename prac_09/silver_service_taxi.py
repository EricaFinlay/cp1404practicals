"""
CP1404 2022 Prac 09
Erica Finlay

Silver Service Taxi

The solutions branch in GitHub was consulted when completing this activity:
https://github.com/CP1404/Practicals/tree/solutions/prac_09
"""

from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised version of a Silver Service Taxi."""
    flagfall = 4.5

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi instance, based on parent class Taxi."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = self.price_per_km * fanciness

    def ___str___(self):
        """Return a string representation of a Silver Service Taxi."""
        return f"{super().__str__()}, {self.current_fare_distance}km on current fare, ${self.price_per_km:.2f}/km" \
               f"plus flagfall of ${self.flagfall}"

    def get_fare(self):
        """Calculate fare of a Silver Service Taxi."""
        return self.flagfall + super().get_fare()
