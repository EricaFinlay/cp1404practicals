"""
CP1404 2022 Prac 05
Erica Finlay

Do-From_Scratch Exercises
Game Set Match

Estimate:   1 hour
Actual:     50 minutes

The solution to this program was consulted on GitHub.

Pseudocode:
FILE_NAME = "wimbledon.csv"

function main()
    with open(FILE_NAME, "r", encoding="utf-8-sig") as in_file
        dictionary_of_champions = empty dictionary
        length_of_champion = 0
        countries = empty list
        for line in in_file
            champions = split line at comma [2]
            if champions in dictionary_of_champions
                dictionary_of_champions[champions] += 1
            else:
                dictionary_of_champions[champions] = 1
            country = split line at comma [3]
            add country to countries
        del "Champion" entry in dictionary
        for champion in dictionary_of_champions
            if length of champion > length_of_champion
                length_of_champion = length of champion
        display heading
        for champion in dictionary_of_champions
            display champion and number of times won
        delete countries[0]
        unique_countries = empty list
        for country in countries
            if country not in unique_countries
                add country to unique countries
        sort unique_countries
        display heading
        for country in unique_countries[:12]
            display country
    close in_file
"""

FILE_NAME = "wimbledon.csv"


def main():
    """Reads an in_file and displays champion, number of times won, and top 12 winning countries."""
    with open(FILE_NAME, "r", encoding="utf-8-sig") as in_file:
        dictionary_of_champions = {}
        length_of_champion = 0
        countries = []
        for line in in_file:
            champions = line.split(',')[2]
            if champions in dictionary_of_champions:
                dictionary_of_champions[champions] += 1
            else:
                dictionary_of_champions[champions] = 1
            country = line.split(',')[3]
            countries.append(country)
        del dictionary_of_champions["Champion"]
        for champion in dictionary_of_champions:
            if len(champion) > length_of_champion:
                length_of_champion = len(champion)
        print("Wimbledon Champions:")
        for champion in dictionary_of_champions:
            print(f"{champion:{length_of_champion}} won {dictionary_of_champions[champion]} times")
        del countries[0]
        unique_countries = []
        for country in countries:
            if country not in unique_countries:
                unique_countries.append(country)
        unique_countries.sort()
        print()
        print("These 12 countries have won Wimbledon:")
        for country in unique_countries[:12]:
            print(country, end=", ")
    in_file.close()


main()
