"""
CP1404 2022 Prac 04
Erica Finlay

CP1404/CP5632 Practical
Debugging exercise: almost-working version of a CSV scores file program.
The scores.csv file stores scores for each subject for 10 people.
This code reads the lines into lists, saves the first line as a list of subject codes and
converts the rest of the lines from a list of strings into a list of numbers,
which it then prints with the maximum value for that subject.
Nice. Except, it’s broken! It reads the lists per user not per subject so the results are incorrect.
Use the debugger to follow what it's doing... then fix it.
"""


# Lindsay, I'm aware of having repeated myself in this program and that a suitable 'for' loop would
# have prevented this, however it's the best I can come up with at present.

def main():
    """Read and display student scores from scores file."""
    scores_file = open("scores.csv")
    scores_data = scores_file.readlines()
    print(scores_data)
    print()
    del (scores_data[0])
    IT101 = []
    IT201 = []
    IT202 = []
    IT301 = []
    IT302 = []
    for score in scores_data:
        parts = score.split(',')
        IT101.append(parts[0])
        IT201.append(parts[1])
        IT202.append(parts[2])
        IT301.append(parts[3])
        IT302.append(parts[4])
    print(f"The 10 scores for IT101 are:")
    total = 0
    for grade in IT101:
        print(grade, end=" ")
        grade = int(grade)
        total += grade
    print()
    print(f"The maximum grade is: {max(IT101):>4}")
    print(f"The minimum grade is: {min(IT101):>4}")
    average = total / len(IT101)
    print(f"The average grade is:   {average:.1f}")
    print()
    print(f"The 10 scores for IT201 are:")
    total = 0
    for grade in IT201:
        print(grade, end=" ")
        grade = int(grade)
        total += grade
    print()
    print(f"The maximum grade is: {max(IT201):>4}")
    print(f"The minimum grade is: {min(IT201):>4}")
    average = total / len(IT201)
    print(f"The average grade is:   {average:.1f}")
    print()
    print(f"The 10 scores for IT202 are:")
    total = 0
    for grade in IT202:
        print(grade, end=" ")
        grade = int(grade)
        total += grade
    print()
    print(f"The maximum grade is: {max(IT202):>4}")
    print(f"The minimum grade is: {min(IT202):>4}")
    average = total / len(IT202)
    print(f"The average grade is:   {average:.1f}")
    print()
    print(f"The 10 scores for IT301 are:")
    total = 0
    for grade in IT301:
        print(grade, end=" ")
        grade = int(grade)
        total += grade
    print()
    print(f"The maximum grade is: {max(IT301):>4}")
    print(f"The minimum grade is: {min(IT301):>4}")
    average = total / len(IT301)
    print(f"The average grade is:   {average:.1f}")
    print()
    print(f"The 10 scores for IT302 are:")
    total = 0
    for grade in IT302:
        grade = grade[:-2]
        print(grade, end=" ")
        grade = int(grade)
        total += grade
    print()
    print(f"The maximum grade is: {max(IT302):>4}", end="")
    print(f"The minimum grade is: {min(IT302):>4}", end="")
    average = total / len(IT302)
    print(f"The average grade is:   {average:.1f}")


main()
