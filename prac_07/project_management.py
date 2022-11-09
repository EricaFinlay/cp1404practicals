"""
CP1404 2022 Prac 07
Erica Finlay

Do-from-scratch Exercises
Project Management Program

Time estimate:     2 hours
Actual:            6 hours
"""

from prac_07.project import Project
from operator import attrgetter
import datetime

DEFAULT_FILENAME = 'projects.txt'
CSV_FILE_HEADER = "Name\tStart\tDate\tPriority\tCost Estimate\tCompletion Percentage"
MENU_PROMPT = "- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n" \
              "- (A)dd new project\n- (U)pdate project\n- (Q)uit"


def main():
    """Display menu options to manage a list of projects."""
    projects = load_projects(DEFAULT_FILENAME)
    print(MENU_PROMPT)
    menu_choice = input(">>> ").upper()
    while menu_choice != "Q":
        if menu_choice == "L":
            filename = input("File name to load from: ")
            projects = load_projects(filename)
        elif menu_choice == "S":
            filename = input("File name to save to: ")
            save_projects(projects, filename)
        elif menu_choice == "D":
            projects.sort(key=attrgetter('priority'))
            filtered_projects = [project for project in projects if project.completion_percentage < 100]
            print("Incomplete projects:")
            for project in projects:
                if project in filtered_projects:
                    print(project)
            filtered_projects = [project for project in projects if project.completion_percentage == 100]
            print("Completed projects:")
            for project in projects:
                if project in filtered_projects:
                    print(project)
        elif menu_choice == "F":
            display_filtered(projects)
        elif menu_choice == "A":
            name = get_valid_project_name()
            date_string = get_valid_date("Start date (dd/mm/yyyy): ")
            start_date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
            priority = get_valid_integer("Priority: ")
            cost_estimate = float(input("Cost estimate: "))
            completion_percentage = get_valid_integer("Completion percentage: ")
            new_project = Project(name, start_date, priority, cost_estimate, float(completion_percentage))
            projects.append(new_project)
            print(new_project, "added to file.")
        elif menu_choice == "U":
            for i, project in enumerate(projects, 0):
                print(i, project)
            chosen_index = int(input("Project choice: "))
            print(projects[chosen_index])
            new_percentage = input("New Percentage: ")
            if new_percentage != "":
                projects[chosen_index].completion_percentage = int(new_percentage)
            new_priority = input("New Priority: ")
            if new_priority != "":
                projects[chosen_index].priority = int(new_priority)
        else:
            print("Invalid input")
        print(MENU_PROMPT)
        menu_choice = input(">>> ").upper()
    save_projects(projects, DEFAULT_FILENAME)
    print("Thank you for using custom-built project management software.")


def load_projects(filename):
    """Load projects from a selected file."""
    projects = []
    in_file = open(filename, 'r')
    in_file.readline()
    for line in in_file:
        parts = line.strip().split("\t")
        date = datetime.datetime.strptime(parts[1], "%d/%m/%Y").date()
        project = Project(parts[0], date, int(parts[2]), float(parts[3]),
                          int(parts[4]))
        projects.append(project)
    in_file.close()
    return projects


def display_filtered(projects):
    """Filter projects by date."""
    date_string = input("Show projects that start after date (dd/mm/yyyy): ")
    threshold_date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    filtered_projects = [project for project in projects if project.start_date > threshold_date]
    filtered_projects.sort(key=attrgetter('start_date'))
    for project in projects:
        if project in filtered_projects:
            print(project)


def get_valid_project_name():
    """Error check user input for project name."""
    name_input = input("Name: ").title()
    while name_input == "":
        print("Input can not be blank")
        name_input = input("Name: ").title()
    return name_input


def get_valid_integer(prompt):
    """Error check user input for valid integer."""
    is_valid_integer = False
    while not is_valid_integer:
        try:
            user_input = int(input(prompt))
            if user_input < 1:
                print("Number must be >= 1")
            else:
                is_valid_integer = True
        except ValueError:
            print("Invalid input; enter a valid number")
    return user_input


def get_valid_date(prompt):
    """Error check user input for valid date."""
    is_valid_date = False
    while not is_valid_date:
        try:
            date_string = input(prompt)
            datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
            if date_string == "":
                print("Blank date is not acceptable")
            else:
                is_valid_date = True
        except ValueError:
            print("Invalid input; enter a valid date")
    return date_string


def save_projects(projects, filename):
    """Save projects to a selected file."""
    out_file = open(filename, "w")
    print(CSV_FILE_HEADER, file=out_file)
    for project in projects:
        print(repr(project), file=out_file)
    out_file.close()


main()
