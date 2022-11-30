"""
CP1404 2022 Prac 10
Erica Finlay
"""
import wikipedia


def main():
    search_term = input("What do you want to search for? ")
    while search_term != "":
        try:
            search_result = wikipedia.page(search_term)
        except wikipedia.exceptions.DisambiguationError as e:
            print(e.options)
        print(search_result)
        print(search_result.title)
        print(search_result.content)
        print(search_result.url)
        search_term = input("What do you want to search for? ")
    print("Thanks for searching!")


main()
