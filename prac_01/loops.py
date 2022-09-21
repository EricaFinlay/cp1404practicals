"""
CP1404 2022 Prac 01
Erica Finlay

Intermediate Exercises
3. Loops

Pseudocode:
for count from 1 to 21 in 2's
    display count
"""

for i in range(1, 21, 2):
    print(i, end=' ')
print()

"""
Pseudocode:
for count from 0 to 101 in 10's
    display count
"""

for i in range(0, 101, 10):
    print(i, end=' ')
print()

"""
Pseudocode:
for count from 20 to 0 in -1's
    display count
"""

for i in range(20, 0, -1):
    print(i, end=' ')
print()

"""
Pseudocode:
get number_of_stars
for count of number_of_stars
    display "*"
"""

number_of_stars = int(input("Number of stars: "))
for i in range(number_of_stars):
    print("*", end=' ')
print()

"""
Pseudocode:
get number_of_stars
total = 1
for count of number_of_stars
    for count of total
        display "*"
    total += 1
"""

number_of_stars = int(input("Number of stars: "))
total = 1
for i in range(number_of_stars):
    for j in range(total):
        print("*", end=' ')
    total += 1
    print()
