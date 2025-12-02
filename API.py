# Examples

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


# API Project

import tkinter as tk
import requests

def words(input): 
    word = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{input}")
    dictionary = word.json()
    entry = dictionary[0]
    definition = entry["meanings"][0]["definitions"][0]["definition"]
    print(definition)
words("yell")


window = tk.Tk()
window.title("DEFINITION FINDER")
window.geometry("1000x800")
window.resizable(False, False)
window.configure(bg="black")
window.attributes("-alpha", 0.8)

Word_search = tk.Label(window, text = "Write a word to search for a definition:", font=("Times New Roman", 25))
Word_search.pack(pady = 10)

entry = tk.Entry(window, font=("Comic Sans MS", 20), width=30)
entry.pack(pady=5)


my_button = tk.Button(window, text="Search Word",)
command=words
font=("Arial", 16)
bg="lightblue"
fg="black"
relief="raised"
padx=10, pady=5
my_button.pack(pady=20)



window.mainloop()






