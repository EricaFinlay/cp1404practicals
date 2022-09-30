"""
CP1404 2022 Prac 03
Erica Finlay

CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?

A ValueError will occur when anything other than an integer is entered either as numerator or denominator.  Therefore,
if a string or a float is entered (including an empty string), this will be handled as a ValueError.

2. When will a ZeroDivisionError occur?

A ZeroDivisionError will occur if a zero is entered as the denominator.

3. Could you change the code to avoid the possibility of a ZeroDivisionError?

Yes, the code could be changed to avoid a ZeroDivisionError from occurring in the first place.  This would be best
achieved by placing a while loop that continues to ask for valid input until a number other than zero is entered.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Please enter a number other than zero.")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
# except ZeroDivisionError:  # This line is no longer required due to the while loop
#     print("Cannot divide by zero!")  # This line is no longer required due to the while loop
print("Finished.")
