"""
CP1404 2022 Prac 05
Erica Finlay

Do-From_Scratch Exercises
Word Occurrences

Estimate:   1 hour
Actual:     1 hour 7 minutes

The solution to this program was consulted on GitHub.

Pseudocode:
function main()
    word_occurrences = empty dictionary
    get user_input
    split user_input
    for word in words
        if word in word_occurrences:
            word_occurrences[word] += 1
        else
            word_occurrences[word] = 1
    create list of keys
    sort list
    width_of_word = length of word
    for word in words
        display word, value
"""


def main():
    """Split a user inputted string in separate words, sort alphabetically and print with number of occurrences."""
    word_occurrences = {}
    user_input = input("Text: ").lower()
    words = user_input.split()
    for word in words:
        if word in word_occurrences:
            word_occurrences[word] += 1
        else:
            word_occurrences[word] = 1
    words = list(word_occurrences.keys())
    words.sort()
    width_of_word = len(word)
    for word in words:
        print(f"{word:{width_of_word}} : {word_occurrences[word]}")


main()
