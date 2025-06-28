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
    while True:
        try:
            print(citycountry(city,country))
            break
        except TypeError:
            print("Can only Accept words and letter. Try Again.")
            main()
    # Second Run
    city = "Santiago"
    country = "Chile"
    print(citycountry(city,country))

    # Third Run
    print(citycountry(city="Wakanda", country="Nigeria"))
    pass


def citycountry(city, country):
    """
    Accepts two parameters: a city name and a country name, Then concats them into one string
    """
    if isinstance(city, str) and isinstance(country, str):
        return city +", "+country
    else:
        #Throws an error, Error handling occurs in main loop
        return TypeError
    pass


# Program starts here
if __name__ == "__main__":
    main()
