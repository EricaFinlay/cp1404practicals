"""
CP1404 2022 Prac 07
Erica Finlay

Do-from-scratch Exercises
Project Management Program

Time estimate:     2 hours
Actual:              hours
"""

from prac_07.project import Project

FILENAME = "projects.txt"
MENU_PROMPT = "- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n" \
              "- (A)dd new project\n- (U)pdate project\n- (Q)uit"


def main():
    print(MENU_PROMPT)
    menu_choice = input(">>> ")
    # while choice != <quit option>
    #     if choice == <first option>
    #         <do first task>
    #     else if choice == <second option>
    #         <do second task>
    #     ...
    #     else if choice == <n-th option>
    #         <do n-th task>
    #     else
    #         display invalid input error message
    #     display menu
    #     get choice
    # <do final thing, if needed>


main()
