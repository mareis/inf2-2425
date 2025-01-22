import tkinter as tk
from tkinter import ttk
import seaborn as sns

# Last inn datasettet
titanic = sns.load_dataset('titanic')

# Opprett hovedvindu
root = tk.Tk()
root.title("Titanic Klasser")
root.geometry("300x200")

# Funksjon som viser info når man velger klasse
def vis_info(event):
    valgt_klasse = klasse_velger.get()
    passasjerer = titanic[titanic['class'] == valgt_klasse]
    antall = len(passasjerer)
    info_label.config(text=f"Antall passasjerer i {valgt_klasse}: {antall}")

# Lag en label
ttk.Label(root, text="Velg passasjerklasse:").pack(pady=20)

# Opprett dropdown med klasser
klasser = sorted(titanic['class'].unique())
klasse_velger = ttk.Combobox(root, values=klasser, state='readonly')
klasse_velger.pack()

# Label som viser informasjon
info_label = ttk.Label(root, text="")
info_label.pack(pady=20)

# Bind funksjonen til dropdown
klasse_velger.bind('<<ComboboxSelected>>', vis_info)

# Start appen
root.mainloop()