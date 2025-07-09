# --------------------------------------------------------
# Name: Randy Easton
# Date: 6/27/2025
# Assignment: Module 7.2 Assignment: Test Cases
# --------------------------------------------------------
# Purpose:
# Used to run city functions, in particular the final bullet point:
# Run city_functions.py. Call the function at least three times using a City, Country for one, City, Country,
# Population for the next and City, Country, Population, Language for the last. Excecute city_functions.py
# and take a screenshot of the result. Paste that screenshot into your Word document.
# --------------------------------------------------------

from city_functions import citycountry as cc

def main():
    # Main function to control program flow
    # First Run
    city = input("What city are you in?: ")
    country = input("What Country are you in?: ")

    while True:
        try:
            print(cc(city, country))
            break
        except TypeError:
            print("Can only Accept words and letter. Try Again.")
            main()
    # Second Run
    city2 = input("What city are you in?: ")
    country2 = input("What Country are you in?: ")
    population2 = int(input("What is the population of the city?: "))

    while True:
        try:
            print(cc(city2, country2, population=population2))
            break
        except TypeError:
            print("Can only Accept words and letter. Try Again.")
            main()

    # Third Run
    city3 = input("What city are you in?: ")
    country3 = input("What Country are you in?: ")
    population3 = int(input("What is the population of the city?: "))
    language3 = input("What language do you speak?: ")
    while True:
        try:
            print(cc(city3, country3, language3, population3))
            break
        except TypeError:
            print("Can only Accept words and letter. Try Again.")
            main()
# Program starts here
if __name__ == "__main__":
    main()
