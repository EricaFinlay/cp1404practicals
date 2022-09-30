"""
CP1404 2022 Prac 03
Erica Finlay

Practice & Extension Work
"""

# Practice - Random Things
# Version 1:
import random

random_number = random.randint(1, 3)
if random_number == 1:
    random_boolean = True
else:
    random_boolean = False
if random_boolean:
    print("It's True!")
else:
    print("Oh no, it's False!")

# Version 2:
import random

if random.randint(1, 10) < 5:
    random_boolean = True
else:
    random_boolean = False
if random_boolean:
    print("It's True!")
else:
    print("Oh no, it's False!")

# Version 3:
import random

random_number = random.randint(1, 100)
if random_number < 50:
    random_boolean = True
else:
    random_boolean = False
if random_boolean:
    print("It's True!")
else:
    print("Oh no, it's False!")

# Practice - More Random Conrad
import random

MAX_INCREASE = random.uniform(0.0, 0.5)
MAX_DECREASE = random.uniform(0.5, 0.99)
MIN_PRICE = random.randint(1, 10)
MAX_PRICE = random.randint(100, 150)
INITIAL_PRICE = random.randint(20, 30)
OUTPUT_FILE = "conrads_file.txt"

out_file = open(OUTPUT_FILE, 'w')
price = INITIAL_PRICE
print(f"Starting price: ${price:,.2f}", file=out_file)
day = 0

while price >= MIN_PRICE and price <= MAX_PRICE:
    price_change = 0
    # generate a random integer of 1 or 2
    # if it's 1, the price increases, otherwise it decreases
    if random.randint(1, 2) == 1:
        # generate a random floating-point number
        # between 0 and MAX_INCREASE
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        # generate a random floating-point number
        # between negative MAX_DECREASE and 0
        price_change = random.uniform(-MAX_DECREASE, 0)

    price *= (1 + price_change)
    day += 1
    print(f"On day {day} price is ${price:,.2f}", file=out_file)
out_file.close()
