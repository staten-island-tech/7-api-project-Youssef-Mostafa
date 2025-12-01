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

def comic(input): 
    word = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{input}")
    dictionary = word.json()
    print(dict(dictionary))

    

