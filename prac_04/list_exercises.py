"""
CP1404 2022 Prac 04
Erica Finlay

Intermediate Exercises
"""

# 1. Basic List Operations
# Pseudocode:
# numbers = empty list
# for count of 5
#     get number
#     add number to numbers
# display numbers[0]
# display numbers[-1]
# display minimum of numbers
# display maximum of numbers
# display average of numbers

# Version 1:
numbers = []
for i in range(5):
    number = int(input("Number: "))
    numbers.append(number)
print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[-1]}")
print(f"The smallest number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")
print(f"The average of the numbers is {float(sum(numbers)) / len(numbers)}")


# Version 2 (Practice & Extension Work):
# Pseudocode for changes:
# count = 1
# get number
# while number >= 0
#     append number to numbers
#     count += 1
#     get number
numbers = []
count = 1
number = int(input(f"Number {count}: "))
while number >= 0:
    numbers.append(number)
    count += 1
    number = int(input(f"Number {count}: "))
print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[-1]}")
print(f"The smallest number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")
print(f"The average of the numbers is {float(sum(numbers)) / len(numbers)}")

# 2. Woefully inadequate security checker
# Pseudocode:
# usernames = 'jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
#              'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob'
#
# get user_input
# if user_input in usernames
#     display "Access granted"
# else
#     display"Access denied"

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

user_input = input("What is your username? ")
if user_input in usernames:
    print("Access granted")
else:
    print("Access denied")
