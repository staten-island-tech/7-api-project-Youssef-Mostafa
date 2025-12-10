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
from PIL import Image, ImageTk   #Pillow - built in import trying to fetch images
import requests
import io #uploads and stores images im memory/database compliments pillow and


# Window elements

window = tk.Tk()
window.title("GUESS THAT WORD!!!")
window.geometry("1000x800")
window.resizable(False, False)
window.configure(bg="white")

# Text for game

Word_search = tk.Label(window, text="Guess the word in the box below:",
font=("Times New Roman", 25),
bg="white",
fg="black")
Word_search.pack(pady=10)

# Input or where the word is guessed

entry = tk.Entry(window, font=("Comic Sans MS", 20), width=30, bg="lightblue")
entry.pack(pady=5)

# Where the final answer is printed

output_label = tk.Label(window, text="", font=("Comic Sans MS", 20),
bg="white",
fg="lightblue",
wraplength=900,
justify = "left")
output_label.pack(pady=20)

# Image for the random word

image_label = tk.Label(window, bg="white")
image_label.pack(pady=10)

# Gets the definition, meaning, synonym, and antonym of a random word

def get_definition():
    word_to_search = entry.get()
    try:
        response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word_to_search}")
        data = response.json()
        meanings = data[0]["meanings"]
        definition = meanings[0]["definitions"][0].get("definition", "No definition found.")
        synonyms = meanings[0].get("synonyms", [])
        antonyms = meanings[0].get("antonyms", [])
        return {
            "definition": definition,
            "synonyms": synonyms[:8],
            "antonyms": antonyms[:8]}
    except Exception:
        return None
    
# Gets images for the random word

def fetch_image(word):
    try:
        image_url = f"https://source.unsplash.com/600x400/?{word}"
        img_data = requests.get(image_url, timeout=5).content
        img = Image.open(io.BytesIO(img_data))
        return img
    except Exception:
        return None


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

