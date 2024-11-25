import tkinter as tk
from tkinter import ttk
import seaborn as sns
from ipykernel.kernelapp import kernel_aliases

titanic = sns.load_dataset('titanic')
klasser = sorted(titanic['class'].unique())
print(len(titanic[titanic['class'] == "First"]))
print(titanic["class"].head(5))

root = tk.Tk()
root.title('Titanic Dataset')
root.geometry('500x200')

def vis_info(event):
    valgt_klasse = klassevelger.get()
    antall = titanic[titanic['class'] == valgt_klasse]['class'].count()
    info.config(text=f"Det var {antall} pasasjerer fra {valgt_klasse} klasse")

#Nedtrekksliste
klassevelger = ttk.Combobox(root, values=klasser, state='readonly')
klassevelger.set("Velg klasse:")
klassevelger.pack()

info = ttk.Label(root, text='Tester')
info.pack(pady=10)

klassevelger.bind("<<ComboboxSelected>>", vis_info)


root.mainloop()