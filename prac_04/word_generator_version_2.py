"""
CP1404 2022 Prac 04
Erica Finlay

CP1404/CP5632 - Practical
Random word generator - based on format of words

Another way to get just consonants would be to use string.ascii_lowercase
(all letters) and remove the vowels.
"""

# Version 1:  Ask the user to input the new word format.
import random

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"


# word_format = "ccvcvvc"
def main():
    word_format = input("Please select a combinations of (c)onsonants and (v)owels for your word: ").lower()
    result = is_valid_format(word_format)
    print(f"All letters are c's or v's? {result}")
    word = ""
    for kind in word_format:
        if kind == "c":
            word += random.choice(CONSONANTS)
        else:
            word += random.choice(VOWELS)

    print(word)


# # Version 2:  Generates a new word using wildcard substitution.
# import random
#
# VOWELS = "aeiou"
# CONSONANTS = "bcdfghjklmnpqrstvwxyz"
#
# word_format = input("Please enter your wildcard word (containing some %'s and #'s): ").lower()
# word = ""
# for kind in word_format:
#     if kind == "c":
#         word += random.choice(CONSONANTS)
#     elif kind == "%":
#         word += random.choice(CONSONANTS)
#     elif kind == "v":
#         word += random.choice(VOWELS)
#     elif kind == "*":
#         word += random.choice(VOWELS)
#     else:
#         word += kind
#
# print(word)
#
# # Version 3:  Automatically generates the wildcard word format of random length.
# import random
#
# VOWELS = "aeiou"
# CONSONANTS = "bcdfghjklmnpqrstvwxyz"
# WORD_FORMAT_CHOICES = "vc%#"
#
# word_length = random.randint(1, 30)
# word_format = ""
# for i in range(word_length):
#     new_word_format_character = random.choice(WORD_FORMAT_CHOICES)
#     word_format += new_word_format_character
# word = ""
# for kind in word_format:
#     if kind == "c":
#         word += random.choice(CONSONANTS)
#     elif kind == "%":
#         word += random.choice(CONSONANTS)
#     elif kind == "v":
#         word += random.choice(VOWELS)
#     elif kind == "*":
#         word += random.choice(VOWELS)
#     else:
#         word += kind
#
#
# print(word)

def is_valid_format(word_format):
    for char in word_format:
        if char != "c" and char != "v":
            return False
    return True


main()
