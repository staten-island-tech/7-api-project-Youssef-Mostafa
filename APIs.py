# Examples

import tkinter as tk
window = tk.Tk()
window.title("Hello World Window")
window.geometry("800x800")
window.resizable(False, False)
prompt = tk.Label(window, text="Hello World Text:",
font=("Times New Roman", 14))
prompt.pack(pady=10)










window.mainloop()