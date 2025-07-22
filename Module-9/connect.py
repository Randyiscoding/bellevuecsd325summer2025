# --------------------------------------------------------
# Name: Randy Easton
# Date: 7/11/2025
# Assignment: Module 9: JSON and Application Programming Interfaces (APIs)
# --------------------------------------------------------
# Purpose:
# Tutorial on how to use APIs
# --------------------------------------------------------


import requests

def main():
    import random
    rand = random.randint(1, 1025)
    print("Hey Prof Parks, in an effort to make this slightly more readable I added the option to see each part")
    print("of this code run, or you can run it all at once. So select 1 for the first part of the tutorial.")
    print("press 2 for the second part of the tutorial, press three for question 6: The pokedex or, press anykey")
    print("for a wall of text")
    selection = input("1,2 or, 3?: ")
    match selection:
        case "1":
            print("API Tutorial Part 1 Status Code and Formatting using dumps\n")
            print(api_tutorial_1())
        case "2":
            print("\n \n API Tutorial Part 2: Filtering \n")
            print(api_tutorial_2())
        case "3":
            print("\n API Module 9 part 6: Application of Lesson\n")
            print(pokedex(rand))
        case _:
            print("API Tutorial Part 1 Status Code and Formatting using dumps\n")
            print(api_tutorial_1())
            print("\n \n API Tutorial Part 2: Filtering \n")
            print(api_tutorial_2())
            print("\n API Module 9 part 6: Application of Lesson\n")
            print(pokedex(rand))


def api_tutorial_1():
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

def api_tutorial_2():
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
    '''
    Gets pokemon information based on pokedex number
    '''
    import requests, json
    baseurl = 'https://pokeapi.co/api/v2/pokemon/'
    response = requests.get(f'{baseurl}{pokenum}/')
    data = response.json()
    poke_id = data['id']
    poke_name = data['name']
    print(f"The response code for this address is: {response.status_code} \n")  # Prints Server/client Status code
    print(f"You generated Pokemon #{poke_id}: {poke_name} \n \n")
    print(f"\n {response.json()}")  # unformated response from Json
    jsondataformated = json.dumps(response.json(), sort_keys=True, indent=4)

    print(jsondataformated)

# Program starts here
if __name__ == "__main__":
    main()
