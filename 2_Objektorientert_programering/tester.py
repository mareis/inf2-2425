import pandas as pd
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import ttk

# Les inn datasettet
file_path = 'test.csv'
data = pd.read_csv(file_path, encoding='latin1', sep=',')

# Skriv ut de faktiske kolonnenavnene for å undersøke dem
print("Faktiske kolonnenavn:", data.columns)

# Fjern eventuelle leading/trailing whitespace fra kolonnenavnene
data.columns = data.columns.str.strip()

# Beregn netto folkevekst
data['Netto folkevekst'] = (data['Levendefodt'].fillna(0) +
                            data['Innflyttinger'].fillna(0).astype(int) -
                            data['Utflyttinger'].fillna(0).astype(int))

def plot_data():
    selected_column = column_var.get()
    start_year = int(start_year_entry.get())
    end_year = int(end_year_entry.get())

    # Filter data for valgt periode
    filtered_data = data[(data['Ar'] >= start_year) & (data['Ar'] <= end_year)]

    # Plot data
    plt.figure(figsize=(10, 6))
    plt.plot(filtered_data['Ar'], filtered_data[selected_column], marker='o')
    plt.title(f'{selected_column} fra {start_year} til {end_year}')
    plt.xlabel('Ar')
    plt.ylabel(selected_column)
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Opprett GUI-vindu
root = Tk()
root.title('Folkevekstdiagram')

# Opprett og plasser GUI-elementer
column_label = ttk.Label(root, text='Velg kolonne:')
column_label.grid(column=0, row=0, padx=10, pady=5)
columns = ['Levendefodt', 'Innflyttinger', 'Utflyttinger', 'Netto folkevekst']
column_var = StringVar(value=columns[0])
column_dropdown = ttk.Combobox(root, textvariable=column_var, values=columns)
column_dropdown.grid(column=1, row=0, padx=10, pady=5)

start_year_label = ttk.Label(root, text='Startår:')
start_year_label.grid(column=0, row=1, padx=10, pady=5)
start_year_entry = ttk.Entry(root)
start_year_entry.grid(column=1, row=1, padx=10, pady=5)
start_year_entry.insert(0, '1945')  # Default verdi

end_year_label = ttk.Label(root, text='Sluttår:')
end_year_label.grid(column=0, row=2, padx=10, pady=5)
end_year_entry = ttk.Entry(root)
end_year_entry.grid(column=1, row=2, padx=10, pady=5)
end_year_entry.insert(0, '2024')  # Default verdi

plot_button = ttk.Button(root, text='Plotte', command=plot_data)
plot_button.grid(column=0, row=3, columnspan=2, padx=10, pady=10)

# Start GUI-løkke
root.mainloop()
