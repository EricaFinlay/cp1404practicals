"""
CP1404 2022 Prac 04
Erica Finlay

Practice & Extension Work
Memberwise Addition

Pseudocode:
function main()
    items = [1, 2, 3]
    products = [1, 2, 3, 4]
    answers = empty list
    if length of items <= length of products
        difference_in_indexes = length of products - length of items
        for the count of difference_in_indexes
            place_holder = 0
            append placeholder to items
        for the count of length of products
            number_one = items[i]
            number_two = products[i]
            answer = number_one + number_two
            append answer to answers
    else
        difference_in_indexes = length of items - length of products
        for count of difference_in_indexes
            place_holder = 0
            append placeholder to products
        for count of length of items
            number_one = items[i]
            number_two = products[i]
            answer = number_one + number_two
            append answer to answers
    display answers
"""


def main():
    """Add integers in a list of corresponding index number."""
    items = [1, 2, 3]
    products = [1, 2, 3, 4]
    answers = []
    if len(items) <= len(products):
        difference_in_indexes = len(products) - len(items)
        for i in range(difference_in_indexes):
            place_holder = 0
            items.append(place_holder)
        for i in range(len(products)):
            number_one = items[i]
            number_two = products[i]
            answer = number_one + number_two
            answers.append(answer)
    else:
        difference_in_indexes = len(items) - len(products)
        for i in range(difference_in_indexes):
            place_holder = 0
            products.append(place_holder)
        for i in range(len(items)):
            number_one = items[i]
            number_two = products[i]
            answer = number_one + number_two
            answers.append(answer)
    print(answers)


main()
