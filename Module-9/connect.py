# --------------------------------------------------------
# Name: Randy Easton
# Date: 7/11/2025
# Assignment: Module 9: JSON and Application Programming Interfaces (APIs)
# --------------------------------------------------------
# Purpose:
# [Brief one-sentence description of what the program does]
# --------------------------------------------------------


import requests

def main():
    import random
    rand = random.randint(1, 1025)
    # print(apitutorial1())
    # print(apitutorial2())
    print(pokedex(rand))


# Function definitions go here
# Use descriptive names and explain any non-obvious logic
# Example:
def apitutorial1():
    """
    Tutorial from https://www.dataquest.io/blog/api-in-python/ for astronaughts
    """
    import requests, json
    OpenNotify = 'http://api.open-notify.org/astros' # Store web address to be requested
    response = requests.get(OpenNotify) # Stores the responses data recieved by the API
    print(f"The response code for this address is: {response.status_code} \n") # Prints Server/client Status code
    # print(f"\n {response.json()}") # unformated response from Json
    jsondataformated = json.dumps(response.json(), sort_keys=True, indent=4)

    print(jsondataformated)

def apitutorial2():
    """
    Dataquest Tutorial Filter section https://www.dataquest.io/blog/api-in-python/
    """
    import requests, json
    base = 'https://api-server.dataquest.io/economic_data/countries?filter_by=' # Store web address to be requested
    filt = 'region=Sub-Saharan Africa' # Stores Filtering information. Note while dataquest says we must include
                                       # '%20' to represent a space, it is not required as that is done automatically
                                       # by requests. it is probably a good habit though
    response = requests.get(f"{base}{filt}")  # Stores the responses data recieved by the API
    print(f"The response code for this address is: {response.status_code} \n")  # Prints Server/client Status code
    print(f"\n {response.json()}") # unformated response from Json
    jsondataformated = json.dumps(response.json(), sort_keys=True, indent=4)

    # print(jsondataformated)

def pokedex(pokenum):
    import requests, json
    baseurl = 'https://pokeapi.co/api/v2/pokemon/'
    response = requests.get(f'{baseurl}{pokenum}/')
    print(f"The response code for this address is: {response.status_code} \n")  # Prints Server/client Status code
    print(f"\n {response.json()}")  # unformated response from Json
    jsondataformated = json.dumps(response.json(), sort_keys=True, indent=4)

    print(jsondataformated)

# Program starts here
if __name__ == "__main__":
    main()
