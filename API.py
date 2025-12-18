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

# Imports needed for game

import tkinter as tk
from tkinter import messagebox   #creates little windows for errors/ experimental code suggested by ChatGPT
import requests

current_word = ""
hint_index = 0
current_info = {}

# Window elements

window = tk.Tk()
window.title("GUESS THAT WORD!!!")
window.geometry("1000x800")
window.resizable(False, False)
window.configure(bg="steelblue")

# Ui and text for game

Word_search = tk.Label(
window, 
text="Guess the hidden word!:",
font=("Times New Roman", 25),
bg="steelblue",
fg="lightblue")
Word_search.pack(pady=10)

entry = tk.Entry(
window, 
font=("Comic Sans MS", 20), 
width=30, 
bg="lightblue")
entry.pack(pady=5)

output_label = tk.Label(
window, 
text="", 
font=("Comic Sans MS", 16),
bg="steelblue",
fg="lightblue",
wraplength=900,
justify = "left")
output_label.pack(pady=20)

hint_label = tk.Label(
window, 
text="", 
font=("Comic Sans MS", 18), 
bg ="steelblue", 
fg="blue")
hint_label.pack(pady=5)

clue_label = tk.Label(
window,
text="",
font=("Comic Sans MS", 16),
bg = "steelblue",
fg = "lightblue",
wraplength=900,
justify="left")
clue_label.pack(pady=10)

# All the functions for code

def get_word_info(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"

    try:
        data = requests.get(url, timeout=5).json()
        if isinstance(data, dict) and data.get("title") == "No Definitions Found":
            return None
        
        meanings = data[0]["meanings"]
        definition = meanings[0]["definitions"][0].get(
            "definition", "No definition available.")
        
        synonyms = []
        antonyms = []

        for m in meanings:
            synonyms.extend(m.get("synonyms", []))
            antonyms.extend(m.get("antonyms", []))
            for d in m["definitions"]:
                synonyms.extend(d.get("synonyms", []))
                antonyms.extend(d.get("antonyms", []))

        return {
            "definition": definition,
            "synonyms": list(set(synonyms))[:8],
            "antonyms": list(set(antonyms))[:8]
        }
    
    except Exception:
        return None

def get_random_word():
    global current_word, hint_index, current_info

# Button to click to accept input and print the definition

my_button = tk.Button(window, text="Guess Word", font=("Times New Roman", 20),
bg="lightblue", fg="black", relief="raised",
command=get_definition)
my_button.pack(pady=25) 

# Finds a random word on sepearate API

def randomwordfinder():
    url = "https://random-word-api.herokuapp.com/word"
    try:
        response2 = requests.get(url)
        data2 = response2.json()
        randomword = data2[0]
        print(randomword)
    except Exception:
        print("Error fetching random word:")
        return None
randomwordfinder()




window.mainloop()

