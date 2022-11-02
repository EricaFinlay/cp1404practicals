"""
CP1404 2022 Prac 06
Erica Finlay

CP1404/CP5632 Practical - Client code to use the Car class.
Note that the import has a folder (module) in it.
This is why we name our folders with no spaces or capitals, as valid module names.

The solutions branch in GitHub was consulted when completing this activity:
https://github.com/CP1404/Practicals/tree/solutions/prac_06
"""

from prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car("My old red car:", 180)
    my_car.drive(30)
    print(f"Car fuel: {my_car.fuel}")
    print(my_car)

    limo = Car("My fancy black limo:", 100)
    limo.add_fuel(20)
    print(f"Limo fuel: {limo.fuel}")
    limo.drive(115)
    print(limo)


main()
