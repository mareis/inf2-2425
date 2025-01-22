import tkinter as tk
from tkinter import ttk

def legg_til_oppgave():
    oppgave = oppgave_input.get()
    if oppgave:
        oppgave_liste.insert(tk.END, oppgave)
        oppgave_input.delete(0, tk.END)

def slett_oppgave():
    # Hent valgt oppgave
    try:
        valgt = oppgave_liste.curselection()[0]
        oppgave_liste.delete(valgt)
    except IndexError:
        pass  # Ingen oppgave valgt

def enter_trykket(event):
    legg_til_oppgave()

root = tk.Tk()
root.title("Min Huskeliste")
root.geometry("300x400")

# Hovedramme med padding
hovedramme = ttk.Frame(root, padding="10")
hovedramme.pack(fill='both', expand=True)

# Input-felt
oppgave_input = ttk.Entry(hovedramme)
oppgave_input.pack(padx=10, pady=10, fill='x')
# Bind Enter-tasten
oppgave_input.bind('<Return>', enter_trykket)

# Knapper i egen ramme
knapp_ramme = ttk.Frame(hovedramme)
knapp_ramme.pack(fill='x', pady=5)

legg_til_knapp = ttk.Button(knapp_ramme, text="Legg til", command=legg_til_oppgave)
legg_til_knapp.pack(side='left', padx=5)

slett_knapp = ttk.Button(knapp_ramme, text="Slett", command=slett_oppgave)
slett_knapp.pack(side='left')

# Liste
oppgave_liste = tk.Listbox(hovedramme)
oppgave_liste.pack(padx=10, pady=10, fill='both', expand=True)

root.mainloop()