"""
CP1404 2022 Prac 05
Erica Finlay

Do-From_Scratch Exercises
Emails

Estimate:   2 hours
Actual:     1 hour 10 min

The solution to this program was consulted on GitHub.

Pseudocode:
function main()
    email_and_user = empty dictionary
    length_of_name = 0
    get email
    while email != ""
        get_name_from_email(email)
        get confirmation
        if confirmation != "Y" and confirmation != ""
            get name
        add name as value
        for email in email_and_user
            if length of name > length_of_name
                length_of_name = length of name
        get email
    for email, name in email_and_user
        display name, email


function get_name_from_email(email)
    initial_string = split email at '@' [0]
    names = split initial_string at '.'
    name = join names with space between
    return name
"""


def main():
    """Ask the user for their email and name and print this information."""
    email_and_user = {}
    length_of_name = 0
    email = input("Email: ")
    while email != "":
        name = get_name_from_email(email)
        confirmation = input(f"Is your name {name}? (Y/n) ")
        if confirmation.upper() != "Y" and confirmation != "":
            name = input("Name: ")
        email_and_user[email] = name
        for email in email_and_user:
            if len(name) > length_of_name:
                length_of_name = len(name)
        email = input("Email: ")
    for email, name in email_and_user.items():
        print(f"{name:{length_of_name}} - ({email})")


def get_name_from_email(email):
    """Splits an email address to retrieve first and last names separately."""
    initial_string = email.split('@')[0]
    names = initial_string.split('.')
    name = " ".join(names).title()
    return name


main()
