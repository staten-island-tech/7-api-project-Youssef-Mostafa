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
window.resizable(True, True)
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

    hint_index = 0
    hint_label.config(text="")
    output_label.config(text="")
    entry.delete(0, tk.END)

    try:
        current_word = requests.get("https://random-word-api.herokuapp.com/word", timeout=5).json()[0].lower()
        info = get_word_info(current_word)
        current_info = info if info else {
            "definition": "No definition available.",
            "synonyms": [],
            "antonyms": []
        }

        syn = current_info["synonyms"][0] if current_info["synonyms"] else "None"
        ant = current_info["antonyms"][0] if current_info["antonyms"] else "None"

        clue_text = (
            f"Definiton:\n{current_info['definition']}\n\n"
            f"Synonym Clue: {syn}\n"
            f"Antonym Clue: {ant}\n\n"
            f"Hint: Click 'Reveal Hint' to show letters of the word."
        )
        clue_label.config(text=clue_text)
    
    except Exception as e:
        messagebox.showerror("Error", f"Could not load word: {e}")


def check_guess():
    guess = entry.get().strip().lower()

    if not guess:
        messagebox.showwarning("Input Error", "Enter a guess first!")
        return
    
    if guess == current_word:
        output_label.config(
            text=(
            f"Correct! The word was: {current_word}\n\n"
                f"Definition: {current_info['definition']}\n\n"
                f"Synonyms: {', '.join(current_info['synonyms']) or 'None'}\n"
                f"Antonyms: {', '.join(current_info['antonyms']) or 'None'}"
            )
        )
    else:
        output_label.config(text="Incorrect! Guess again!")


def reveal_hint():
    global hint_index

    if not current_word:
        hint_label.config(text="Let a word load first!")
        return
    
    if hint_index >= len(current_word):
        hint_label.config(text="All letters have been revealed!")
        return
    
    hint_index += 1
    revealed = current_word[:hint_index] + "*" * (len(current_word) - hint_index)
    hint_label.config(text=f"Hint: {revealed}")

# Buttons for the games functions

btn_new_word = tk.Button(
window,
text="New Random Word",
font=("Times New Roman", 20),
bg="blue",
command=get_random_word
)
btn_new_word.pack(pady=5)

btn_reveal = tk.Button(
    window,
    text="Reveal Hint",
    font=("Times New Roman", 20),
    bg="steelblue",
    command=reveal_hint
)
btn_reveal.pack(pady=5)

btn_guess = tk.Button(
    window,
    text="Submit Guess",
    font=("Times New Roman", 20),
    bg="lightblue",
    command=check_guess
)
btn_guess.pack(pady=5) 

window.mainloop()

