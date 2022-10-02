"""
CP1404 2022 Prac 04
Erica Finlay

CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Print the output of an in_file using lists."""
    data = get_data()
    print(data)
    subject_details = get_subject_details()
    print(subject_details)

def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    famous_persons = []
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked
        print("----------")
        famous_persons.append(parts)
    print(famous_persons)
    input_file.close()


def get_subject_details():
    """Read data from in_file and split for formatting and printing."""
    input_file = open(FILENAME)
    for line in input_file:
        line = line.strip()
        parts = line.split(',')
        print(f"{parts[0]:6} is taught by {parts[1]:12} and has {parts[2]:>3} students")
    input_file.close()


main()
