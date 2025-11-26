import requests

""" def getPoke(poke):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{poke.lower()}")
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    
    data = response.json()
    return {
        "name": data["name"],
        "height": data["height"],
        "weight": data["weight"],
        "types": [t["type"]["name"] for t in data["types"]]
    }

pokemon = getPoke("Bulbasaur")
print(pokemon) """


import requests

def getJoke(joke):
    response = requests.get(f"https://geek-jokes.sameerkumar.website/api?format=json")
    if response.status_code != 200:
        print("Error fetching joke!")
        return None
    
    data = response.json()

ChuckN = getJoke("Joke")
print(ChuckN)

