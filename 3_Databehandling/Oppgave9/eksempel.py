import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from tkinter import *
from tkinter import ttk


class BefolkningsAnalyse:
    def __init__(self, root):
        self.root = root
        self.root.title("Befolkningsstatistikk Norge")

        # Les datasettet
        self.df = pd.read_csv('Datasett_fodselstall_komma.csv', encoding='utf-8')
        self.df.columns = ['År', 'Levendefødte', 'Innflyttinger', 'Utflyttinger']

        # Lag periodevalg (tilsvarer kjønnsvalg i originaloppgaven)
        self.periode_label = Label(root, text="Velg periode:")
        self.periode_label.pack(pady=5)

        self.periode_var = StringVar()
        self.periode_var.set("Alle år")

        perioder = ["Alle år", "Siste 10 år", "Siste 20 år"]
        self.periode_menu = ttk.Combobox(root, textvariable=self.periode_var, values=perioder)
        self.periode_menu.pack(pady=5)

        # Bind oppdateringsfunksjon til periodevalg
        self.periode_menu.bind('<<ComboboxSelected>>', self.oppdater_visning)

        # Opprett tabell
        self.tree = ttk.Treeview(root, columns=("År", "Levendefødte", "Innflyttinger", "Utflyttinger"), show="headings")
        self.tree.heading("År", text="År")
        self.tree.heading("Levendefødte", text="Levendefødte")
        self.tree.heading("Innflyttinger", text="Innflyttinger")
        self.tree.heading("Utflyttinger", text="Utflyttinger")
        self.tree.pack(pady=10, padx=10)

        # Lag knapp for å vise diagrammer
        self.vis_diagram_btn = Button(root, text="Vis diagrammer", command=self.vis_diagrammer)
        self.vis_diagram_btn.pack(pady=10)

        # Initialiser visning
        self.oppdater_visning(None)

    def oppdater_visning(self, event):
        # Tøm eksisterende data
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Filtrer data basert på valgt periode
        if self.periode_var.get() == "Siste 10 år":
            data = self.df.tail(10)
        elif self.periode_var.get() == "Siste 20 år":
            data = self.df.tail(20)
        else:
            data = self.df

        # Fyll tabellen med data
        for index, row in data.iterrows():
            self.tree.insert("", "end", values=(row['År'],
                                                row['Levendefødte'],
                                                row['Innflyttinger'],
                                                row['Utflyttinger']))

    def vis_diagrammer(self):
        # Hent filtrert data
        if self.periode_var.get() == "Siste 10 år":
            data = self.df.tail(10)
        elif self.periode_var.get() == "Siste 20 år":
            data = self.df.tail(20)
        else:
            data = self.df

        # Opprett figur med to subplot
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

        # Stolpediagram
        ax1.bar(data['År'], data['Levendefødte'], label='Levendefødte')
        ax1.set_title('Antall levendefødte')
        ax1.set_xlabel('År')
        ax1.set_ylabel('Antall')
        ax1.tick_params(axis='x', rotation=45)

        # Sektordiagram
        # Beregn gjennomsnitt for perioden
        gjennomsnitt = {
            'Levendefødte': data['Levendefødte'].mean(),
            'Innflyttinger': data['Innflyttinger'].mean(),
            'Utflyttinger': data['Utflyttinger'].mean()
        }

        ax2.pie(gjennomsnitt.values(),
                labels=gjennomsnitt.keys(),
                autopct='%1.1f%%')
        ax2.set_title('Fordeling av befolkningsendringer')

        plt.tight_layout()
        plt.show()


# Start applikasjonen
if __name__ == "__main__":
    root = Tk()
    app = BefolkningsAnalyse(root)
    root.mainloop()