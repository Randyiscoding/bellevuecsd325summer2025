# --------------------------------------------------------
# Name: Randy Easton
# Date: 6/27/2025
# Assignment: Module 7.2 Assignment: Test Cases
# --------------------------------------------------------
# Purpose:
# [Brief one-sentence description of what the program does]
# --------------------------------------------------------

def main():
    # Main function to control program flow
    # First Run
    city = input("What city are you in?: ")
    country = input("What Country are you in?: ")
    population = int(input("What is the population of the city?: "))
    while True:
        try:
            print(citycountry(city, country, population))
            break
        except TypeError:
            print("Can only Accept words and letter. Try Again.")
            main()
    # Second Run
    city = "Santiago"
    country = "Chile"
    print(citycountry(city, country))

    # Third Run
    print(citycountry(city="Wakanda", country="Nigeria", population=5789943))
    pass

# Remove =None to make population required again
def citycountry(city, country, population=None):
    """
    Accepts three parameters: a city name, a country name and, a population size, Then concats them into one string
    """
    # checks if optional parameter is filled
    if population != None:
        #check if Parameters have correct typing
        if isinstance(city, str) and isinstance(country, str) and isinstance(population, int):
            return f"{city}, {country} - population {population}"
        else:
            # Throws an error, Error handling occurs in main loop
            return TypeError
    else:
        if isinstance(city, str) and isinstance(country, str):
            return city + ", " + country
        else:
            # Throws an error, Error handling occurs in main loop
            return TypeError
    pass


# Program starts here
if __name__ == "__main__":
    main()
