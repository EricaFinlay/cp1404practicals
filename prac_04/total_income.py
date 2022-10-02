"""
CP1404 2022 Prac 04
Erica Finlay

Walkthrough Example
Calculating a List of Cumulative Totals

CP1404/CP5632 Practical
Starter code for cumulative total income program

N.B:  GitHub solution consulted and used when trying to get the enumerate function to work.
"""


def main():
    """Display income report for incomes over a given number of number_of_months."""
    incomes = []
    number_of_months = int(input("How many number_of_months? "))

    for month in range(1, number_of_months + 1):
        income = float(input("Enter income for month {}: ".format(month)))
        incomes.append(income)

    print_report(incomes)


# Version 1:
# def print_report(incomes, number_of_months):
#     """Print a table of month, income and total."""
#     print("\nIncome Report\n-------------")
#     total = 0
#     for month in range(1, number_of_months + 1):
#         income = incomes[month - 1]
#         total += income
#         print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


# Version 2:
def print_report(incomes):
    """Print a table of month, income and total."""
    print("\nIncome Report\n-------------")
    total = 0
    for month, income in enumerate(incomes):
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month + 1, income, total))


main()
