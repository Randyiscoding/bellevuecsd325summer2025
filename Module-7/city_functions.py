# --------------------------------------------------------
# Name: Randy Easton
# Date: 6/27/2025
# Assignment: Module 7.2 Assignment: Test Cases
# --------------------------------------------------------
# Purpose:
# Takes in at least 2 and upto 4 inputs (3 strings and 1 integer) and formats it into one full string
# --------------------------------------------------------


def main():
    # Main function to control program flow
    # First Run
    city = "Santiago"
    country = "Chile"
    print(citycountry(city, country))

    # Second Run
    city = input("What city are you in?: ")
    country = input("What Country are you in?: ")
    population = int(input("What is the population of the city?: "))

    while True:
        try:
            print(citycountry(city, country, language=None, population=population))
            break
        except TypeError:
            print("Can only Accept words and letter. Try Again.")
            main()

    # Third Run
    print(citycountry(city="Wakanda", country="Nigeria", population=145236896, language="igbo"))
    pass

# Remove =None to make population or lanaguage required again
def citycountry(city, country, language=None, population=None):
    """
    Accepts three parameters: a city name, a country name and, a population size, Then concats them into one string
    """
    # checks if optional parameter is filled
    match population, language:
        case None, None:
            if isinstance(city, str) and isinstance(country, str):
                return city + ", " + country
            else:
                # Throws an error, Error handling occurs in main loop
                return TypeError
        case population, None:
            # check if Parameters have correct typing
            if isinstance(city, str) and isinstance(country, str) and isinstance(population, int):
                return f"{city}, {country} - population {population}"
            else:
                # Throws an error, Error handling occurs in main loop
                return TypeError
        case None, language:
            # check if Parameters have correct typing
            if isinstance(city, str) and isinstance(country, str) and isinstance(language, str):
                return f"{city}, {country} - Language {language}"
            else:
                # Throws an error, Error handling occurs in main loop
                return TypeError
        case _:
            # check if Parameters have correct typing
            if isinstance(city, str) and isinstance(country, str) and isinstance(population, int) and isinstance(language, str):
                return f"{city}, {country} - population {population}, {language}"
            else:
                # Throws an error, Error handling occurs in main loop
                return TypeError

# Program starts here
if __name__ == "__main__":
    main()
