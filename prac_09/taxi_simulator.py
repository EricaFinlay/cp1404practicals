"""
CP1404 2022 Prac 09
Erica Finlay

Taxi Simulator

The solutions branch in GitHub was consulted for the writing of this program:
https://github.com/CP1404/Practicals/tree/solutions/prac_09

** Please note:  This program is still not working properly.
"""

from prac_09.car import Car
from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU_PROMPT = "q)uit, c)hoose taxi, d)rive"


def main():
    """Drive a selected taxi and receive calculated billing prices."""
    total_bill = 0
    taxi_being_driven = None
    taxis = [Taxi("White taxi", 50), SilverServiceTaxi("Red taxi", 50, 50)]
    print("Let's drive!")
    print(MENU_PROMPT)
    user_input = input(">>> ").lower()
    while user_input != "q":
        if user_input == "c":
            print("Taxi's available:")
            display_taxis(taxis)
            taxi_selection = int(input("Choose taxi: "))
        elif user_input == "d":
            if taxi_being_driven:
                taxi_being_driven.start_fare()
                drive_distance = float(input("Drive how far? "))
                taxi_being_driven.drive(drive_distance)
                cost = taxi_being_driven.get_fare()
                print(f"Your {taxi_being_driven.name} trip cost you ${cost:.2f}")
                total_bill += cost
            else:
                print("You need to choose a taxi before you can drive")
        else:
            print("Invalid option")
        print(f"Bill to date: ${total_bill:.2f}")
        print(MENU_PROMPT)
        user_input = input(">>>").lower()
    print(f"Total trip cost: ${total_bill:.2f}")
    print("Taxi's are now:")
    display_taxis(taxis)


def display_taxis(taxis):
    """Display available taxis."""
    for i, taxi in enumerate(taxis, 1):
        print(f"{i} - {taxi}")


main()
