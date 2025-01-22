import tkinter as tk
from tkinter import ttk

def dag_valgt(event):
    valgt_dag = dag_velger.get()
    resultat_label.config(text=f"Du valgte: {valgt_dag}")

# Hovedvindu
root = tk.Tk()
root.title("Velg Dag")
root.geometry("300x200")

# Overskrift
overskrift = ttk.Label(
    root,
    text="Velg en ukedag:",
    font=('Helvetica', 12)
)
overskrift.pack(pady=10)

# Liste over dager
dager = ["Mandag", "Tirsdag", "Onsdag", "Torsdag", "Fredag", "Lørdag", "Søndag"]

# Lag dropdown
dag_velger = ttk.Combobox(root, values=dager, state='readonly')
dag_velger.pack(pady=10)
dag_velger.set("Velg dag")  # Standard tekst

# Vis valgt dag
resultat_label = ttk.Label(root, text="")
resultat_label.pack(pady=20)

# Bind hendelse til dropdown
dag_velger.bind('<<ComboboxSelected>>', dag_valgt)

root.mainloop()