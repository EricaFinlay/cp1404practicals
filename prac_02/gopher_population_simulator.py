"""
CP1404 2022 Prac 02
Erica Finlay

Extension
Gopher Population Simulator

Pseudocode:
import random module

function main()
    display welcome message
    display starting population
    display starting year
    population = 1000
    for i in range(2, 11)
        birth_rate_percentage = random integer between 10 and 20 inclusive
        new_births = (population * birth_rate_percentage) // 100
        death_rate_percentage = random integer  between 5 and 25 inclusive
        new_deaths = (population * death_rate_percentage) // 100
        population = population + new_births - new_deaths
        display birth_rate, death_rate
        display new population
        display year
    display farewell message
"""

import random


def main():
    """Simulate changes in a Gopher population over a ten year period."""
    print("Welcome to the Gopher Population Simulator!")
    print("Starting population: 1000")
    print("Year 1")
    print()
    population = 1000
    for i in range(2, 11):
        birth_rate_percentage = random.randint(10, 20)
        new_births = (population * birth_rate_percentage) // 100
        death_rate_percentage = random.randint(5, 25)
        new_deaths = (population * death_rate_percentage) // 100
        population = population + new_births - new_deaths
        print(f"{new_births} gophers were born.  {new_deaths} died.")
        print(f"Population: {population}")
        print(f"Year {i}")
        print()
    print("Thanks for using the Gopher Population Simulator!")


main()
