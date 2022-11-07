"""
CP1404 2022 Prac 07
Erica Finlay

Do-from-scratch Exercises
Project Management Program

Time estimate:     2 hours
Actual:              hours
"""

from prac_07.project import Project
from operator import attrgetter
import datetime

FILENAME = "projects.txt"
MENU_PROMPT = "- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n" \
              "- (A)dd new project\n- (U)pdate project\n- (Q)uit"


def main():
    projects = []
    in_file = open('projects.txt', 'r')
    in_file.readline()
    for line in in_file:
        parts = line.strip().split("\t")
        project = Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4]))  # TODO Type of start date is incorrect
        projects.append(project)
    in_file.close()
    print(MENU_PROMPT)
    menu_choice = input(">>> ").upper()
    while menu_choice != "Q":
        if menu_choice == "L":
            del projects
            projects = []
            user_file_for_loading = input("File name to load from: ")
            in_file = open(user_file_for_loading, 'r')
            in_file.readline()
            for line in in_file:
                parts = line.strip().split("\t")
                project = Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4]))  # TODO Type of start date is incorrect
                projects.append(project)
            in_file.close()
        elif menu_choice == "S":
            user_file_for_saving = input("File name to save to: ")
            out_file = open(user_file_for_saving, "w")
            for project in projects:
                print(repr(project), file=out_file)
            out_file.close()
        elif menu_choice == "D":
            projects.sort(key=attrgetter('priority'))  # TODO Need to sort by incomplete or complete first
            for project in projects:
                print(project)
        elif menu_choice == "F":
            print("Filter by date")  # TODO Not sure how to filter by date and display only after that date
        elif menu_choice == "A":
            name = input("Name: ")
            start_date = input("Start date (dd/mm/yyyy): ")
            priority = int(input("Priority: "))
            cost_estimate = float(input("Cost estimate: "))
            completion_percentage = int(input("Completion percentage: "))
            new_project = Project(name, start_date, priority, cost_estimate, completion_percentage)
            projects.append(new_project)
            print(new_project, "added to file.")
        elif menu_choice == "U":
            project_to_update = input("Choose a project to update: ")  # TODO Not sure how to select and modify project
        else:
            print("Invalid input")
        print(MENU_PROMPT)
        menu_choice = input(">>> ").upper()
    out_file = open(FILENAME, "w")
    for project in projects:
        print(repr(project), file=out_file)
    out_file.close()
    print("Thank you for using custom-built project management software.")


main()
