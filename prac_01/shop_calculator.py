"""
CP1404 2022 Prac 01
Erica Finlay

Do-From-Scratch Exercises
Shop Calculator

Pseudocode:
get number_of_items
total_price = 0
for count in number_of_items
    get price_of_item
    total_price += price_of_item
if total_price > 100
    total_price = total_price - (total_price * discount)
display number_of_items, total_price
"""

DISCOUNT = .1

number_of_items = int(input("Number of items: "))
total_price = 0
for i in range(number_of_items):
    price_of_item = float(input("Price of item: "))
    total_price += price_of_item
if total_price > 100:
    total_price = total_price - (total_price * DISCOUNT)
print(f"Total price for {number_of_items} items is ${total_price:.2f}")

# With Error Checking
DISCOUNT = .1

number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))
total_price = 0
for i in range(number_of_items):
    price_of_item = float(input("Price of item: "))
    total_price += price_of_item
if total_price > 100:
    total_price = total_price - (total_price * DISCOUNT)
print(f"Total price for {number_of_items} items is ${total_price:.2f}")
