"""
CP1404 2022 Prac 06
Erica Finlay

Intermediate Exercises
Programming Language

Estimate:  1 hour
Actual:    1 hour

The solutions branch in GitHub was consulted when completing this activity:
https://github.com/CP1404/Practicals/tree/solutions/prac_06
"""

from prac_06.programming_language import ProgrammingLanguage


def main():
    """Display name, typing, reflection & year of programming languages."""
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(python)

    languages = [python, ruby, visual_basic]
    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


main()
