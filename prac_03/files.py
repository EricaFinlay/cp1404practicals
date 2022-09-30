"""
CP1404 2022 Prac 03
Erica Finlay

Do-from-scratch Exercises
Files
"""

# Question 1. - Ask the user for their name and write it to a file called "name.txt".
# Pseudocode:
# get name
# open file_out
# write name to file_out
# close file_out

name = input("What is your name: ")
out_file = open("name.txt", "w")
print(name, file=out_file)
out_file.close()

# Question 2. - Open the file called "name.txt" and read and print the name.
# Pseudocode:
# open "name.txt" as file_in for reading
# get name from file_in
# close file_in
# display name

in_file = open("name.txt")
text = in_file.read()
in_file.close()
print(f"Your name is {text}")

# Question 3. - Add the first two numbers in "numbers.txt" and prints the sum of these.
# Pseudocode:
# open "numbers.txt" as file_in for reading
# sum_of_numbers = 0
# for count of 2
# read line
# sum_of_numbers = sum_of_numbers + line
# close file_in
# display answer

in_file = open("numbers.txt")
sum_of_numbers = 0
for i in range(2):
    number = int(in_file.readline())
    sum_of_numbers += number
in_file.close()
print(f"The sum of the first two numbers is: {sum_of_numbers}")

# Question 4. - Print the total of all numbers in a file.
# Pseudocode:
# open "numbers.txt" as file_in for reading
# total_of_numbers = 0
# for line in file_in
# total_of_numbers = total_of_numbers + line
# close file_in
# display answer

in_file = open("numbers.txt")
total_of_numbers = 0
for line in in_file:
    total_of_numbers += int(line)
in_file.close()
print(f"The total of all numbers is: {total_of_numbers}")
