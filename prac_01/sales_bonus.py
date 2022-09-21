"""
CP1404 2022 Prac 01
Erica Finlay

Intermediate Exercises
1. Sales Bonus

Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.

Pseudocode:
get sales
if sales < 1000:
    bonus_rate = .1
else
    bonus_rate = .15
bonus_amount = sales * bonus_rate
display bonus_amount
"""

# Program 1:
sales = float(input("Enter sales: $"))
if sales < 1000:
    bonus_rate = .1
else:
    bonus_rate = .15
bonus_amount = sales * bonus_rate
print(f"Your bonus amount is ${bonus_amount:.2f}")

# Program 2:
sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales < 1000:
        bonus_rate = .1
    else:
        bonus_rate = .15
    bonus_amount = sales * bonus_rate
    print(f"Your bonus amount is ${bonus_amount:.2f}")
    sales = float(input("Enter sales: $"))
print(f"Your sales amount of ${sales} is not valid.")
