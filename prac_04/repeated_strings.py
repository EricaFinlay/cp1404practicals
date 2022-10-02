"""
CP1404 2022 Prac 04
Erica Finlay

Practice & Extension Work
3. Repeated Strings

Pseudocode:
phrases = empty string
get phrase
while length of phrase > 0
    append phrase to phrases
    get phrase
repeated_phrases = empty string
total = 0
for phrase in phrases:
    phrase_to_find = phrases[0]
    delete phrases[0]
    if phrase_to_find in phrases
        append phrase_to_find to repeated_phrases
        total = total + 1
if total > 0
    display message
    for repeated_phrase in repeated_phrases
        display repeated_phrase
else:
    display nil message
"""

phrases = []
phrase = input("Enter a phrase: ")
while len(phrase) > 0:
    phrases.append(phrase)
    phrase = input("Enter a phrase: ")
repeated_phrases = []
total = 0
for phrase in phrases:
    phrase_to_find = phrases[0]
    del phrases[0]
    if phrase_to_find in phrases:
        repeated_phrases.append(phrase_to_find)
        total += 1
if total > 0:
    print("Repeated phrases are:")
    for repeated_phrase in repeated_phrases:
        print(repeated_phrase)
else:
    print("No repeated phrases.")
