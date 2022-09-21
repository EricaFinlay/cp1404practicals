"""
CP1404 2022 Prac 01
Erica Finlay

Intermediate Exercises
2. Debugging - Broken program to determine score status

Pseudocode:
get score
while score < 0 or score > 100
    display error message
    get score
if score >= 90
    category = "excellent"
else if score >= 50
    category = "passable"
else
    category = "bad"
display message, category
"""

score = float(input("Enter score: "))
while score < 0 or score > 100:
    print("Invalid score.  Please try again.")
    score = float(input("Enter score: "))
if score >= 90:
    category = "excellent"
elif score >= 50:
    category = "passable"
else:
    category = "bad"
print(f"Your score is {category}.")
