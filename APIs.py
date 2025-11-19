# Examples

import tkinter as tk
""" window = tk.Tk()
window.title("Hello World Window")
window.geometry("1000x750")
window.resizable(False, False)
prompt = tk.Label(window, text="Hello World Input:",
font=("Times New Roman", 14))
prompt.pack(pady=10)
entry = tk.Entry(window, font=("Arial", 14), width=30)
entry.pack(pady=5) """

def Hello_World():
    print("Hello World!!!")
    window = tk.Tk()
    coolbutton = tk.Button(window)
    text="Hello World!"
    font=("Times New Roman", 16)
    fg="red"
    bg="blue"
    width=10
    height=2
    relief="raised"
    coolbutton.pack(pady=20)
    window.mainloop()