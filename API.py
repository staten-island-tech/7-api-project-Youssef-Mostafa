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


# API Project Part 1: Definition Finder

""" import tkinter as tk
import requests

window = tk.Tk()
window.title("DEFINITION FINDER")
window.geometry("1000x800")
window.resizable(False, False)
window.configure(bg="white")

Word_search = tk.Label(window, text="Write a word to search for a definition:",
font=("Times New Roman", 25),
bg="white",
fg="black")
Word_search.pack(pady=10)

entry = tk.Entry(window, font=("Comic Sans MS", 20), width=30, bg="lightblue")
entry.pack(pady=5)

output_label = tk.Label(window, text="", font=("Comic Sans MS", 20),
bg="white",
fg="lightblue",
wraplength=900)
output_label.pack(pady=20)

def get_definition():
    word_to_search = entry.get()
    try:
        response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word_to_search}")
        data = response.json()
        definition = data[0]["meanings"][0]["definitions"][0]["definition"]
        print(definition)
        output_label.config(text=definition)
    except Exception as e:
        output_label.config(text="Word not found. Please try another word.")
        print("Error:", e)

my_button = tk.Button(window, text="Search Word", font=("Times New Roman", 20),
bg="lightblue", fg="black", relief="raised",
command=get_definition)
my_button.pack(pady=25)

window.mainloop() """




# API Project Part 2: Word Guessing Game

import tkinter as tk
import requests

window = tk.Tk()
window.title("DEFINITION FINDER")
window.geometry("1000x800")
window.resizable(False, False)
window.configure(bg="white")

Word_search = tk.Label(window, text="Write a word to search for a definition:",
font=("Times New Roman", 25),
bg="white",
fg="black")
Word_search.pack(pady=10)

entry = tk.Entry(window, font=("Comic Sans MS", 20), width=30, bg="lightblue")
entry.pack(pady=5)

output_label = tk.Label(window, text="", font=("Comic Sans MS", 20),
bg="white",
fg="lightblue",
wraplength=900)
output_label.pack(pady=20)

def get_definition():
    word_to_search = entry.get()
    try:
        response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word_to_search}")
        data = response.json()
        definition = data[0]["meanings"][0]["definitions"][0]["definition"]
        print(definition)
        output_label.config(text=definition)
    except Exception as e:
        output_label.config(text="Word not found. Please try another word.")
        print("Error:", e)

my_button = tk.Button(window, text="Search Word", font=("Times New Roman", 20),
bg="lightblue", fg="black", relief="raised",
command=get_definition)
my_button.pack(pady=25)

window.mainloop()

