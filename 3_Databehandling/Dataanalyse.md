# Arbeidsark: Interaktiv Dataanalyse med CSV-filer

## Mål
- Lese inn, rense og presentere data med pandas.
- Utføre enkle beregninger (f.eks. beregne netto folkevekst).
- Filtrere data med ipywidgets.
- Lage interaktive diagrammer (linje-, stolpe- og sektordiagram) med matplotlib og seaborn.
- Bygge trygghet gjennom trinnvise oppgaver med reelle CSV-filer.

---

## Del 1: Befolkningsdata

### Datasett: befolkning.csv
Kopier følgende tekst og lagre den som `befolkning.csv`:

```
År,Fødselstall,Innflyttinger,Utflyttinger
1945,61814,5000,3000
1946,70727,5500,973
1947,67625,5300,1477
1948,65618,5200,2398
1949,63052,5100,2669
1950,61500,5000,2500
1951,62000,5050,2600
1952,63000,5100,2650
1953,64000,5150,2700
1954,65000,5200,2750
```

### Oppgave 1a: Innlesing og visning av data
1. Les inn datasettet med pandas.  
   **Eksempel:**
   ```python
   import pandas as pd
   data = pd.read_csv("befolkning.csv")
   print(data.head(10))
   ```
2. Kontroller at dataene vises korrekt.

### Oppgave 1b: Rensing og konvertering
1. Fjern unødvendige anførselstegn og ekstra mellomrom i kolonnenavnene:
   ```python
   data.columns = data.columns.str.replace('"', '').str.strip()
   print(data.columns)
   ```
2. Konverter kolonnene `Fødselstall`, `Innflyttinger` og `Utflyttinger` til numerisk datatype:
   ```python
   for col in ['Fødselstall', 'Innflyttinger', 'Utflyttinger']:
       data[col] = pd.to_numeric(data[col], errors='coerce')
   print(data.dtypes)
   ```

### Oppgave 1c: Beregn netto folkevekst
Beregningen skal utføres med formelen:  
**Netto folkevekst = Fødselstall + Innflyttinger - Utflyttinger**
```python
data['Netto folkevekst'] = data['Fødselstall'] + data['Innflyttinger'] - data['Utflyttinger']
print(data.head())
```

### Oppgave 1d: Vis data med scrollbar
Presenter hele datasettet i en tabell med en scrollbar:
```python
from IPython.display import display, HTML
html_tabell = data.to_html(index=False)
scroll_tabell = f"""
<div style="max-height: 300px; overflow-y: auto; border: 1px solid #ddd; padding: 10px;">
    {html_tabell}
</div>
"""
display(HTML(scroll_tabell))
```
Forklar kort hva CSS‑egenskapen `overflow-y: auto` gjør.

### Oppgave 1e: Interaktivt linjediagram for netto folkevekst
Opprett to IntSlider‑widgets for å velge start- og sluttår (fra 1945 til 1954), og lag et linjediagram:
```python
import matplotlib.pyplot as plt
import seaborn as sns
import ipywidgets as widgets

min_aar = int(data['År'].min())
maks_aar = int(data['År'].max())

start_aar_widget = widgets.IntSlider(value=1945, min=min_aar, max=maks_aar, step=1, description='Startår:', continuous_update=False)
slutt_aar_widget = widgets.IntSlider(value=1954, min=min_aar, max=maks_aar, step=1, description='Sluttår:', continuous_update=False)

def oppdater_plot(start, slutt):
    if start > slutt:
        print("Feil: Startår må være mindre enn eller lik sluttår.")
        return
    df_filtrert = data[(data['År'] >= start) & (data['År'] <= slutt)]
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=df_filtrert, x='År', y='Netto folkevekst', marker='o')
    plt.title(f'Utvikling i netto folkevekst: {start} - {slutt}')
    plt.xlabel('År')
    plt.ylabel('Netto folkevekst')
    plt.grid(True)
    plt.show()

widgets.interactive(oppdater_plot, start=start_aar_widget, slutt=slutt_aar_widget)
```
Forklar hvordan interaktiv filtrering med `widgets.interactive()` fungerer.

---

## Del 2: Aktivitetstidsdata

### Datasett: aktiviteter.csv
Kopier følgende tekst og lagre den som `aktiviteter.csv`:

```
Aktivitet,Kjønn,Tidsbruk
Skole,Menn,300
Skole,Kvinner,320
Arbeid,Menn,480
Arbeid,Kvinner,450
Fritid,Menn,180
Fritid,Kvinner,200
Trening,Menn,60
Trening,Kvinner,75
Husarbeid,Menn,90
Husarbeid,Kvinner,110
```

### Oppgave 2a: Visning av aktivitetstidsdata
Les inn datasettet og vis de første radene:
```python
data_akt = pd.read_csv("aktiviteter.csv")
display(data_akt.head())
```

### Oppgave 2b: Filtrering etter kjønn med dropdown
Bruk en dropdown-widget for å filtrere dataene etter kjønn ("Alle", "Menn", "Kvinner"):
```python
import ipywidgets as widgets
from IPython.display import display, HTML

kjønn_widget = widgets.Dropdown(options=['Alle', 'Menn', 'Kvinner'], value='Alle', description='Kjønn:')

def vis_filtrert_tabell(kjønn):
    if kjønn == 'Alle':
        filtrert = data_akt
    else:
        filtrert = data_akt[data_akt['Kjønn'] == kjønn]
    html_tabell = filtrert.to_html(index=False)
    scroll_tabell = f"""
    <div style="max-height: 300px; overflow-y: auto; border: 1px solid #ddd; padding: 10px;">
        {html_tabell}
    </div>
    """
    display(HTML(scroll_tabell))

widgets.interactive(vis_filtrert_tabell, kjønn=kjønn_widget)
```
Diskuter hvordan filtreringen utføres med `data_akt[data_akt['Kjønn'] == kjønn]`.

### Oppgave 2c: Visualisering av aktivitetstidsdata

#### Del 2c-1: Stolpediagram
Lag et stolpediagram som viser tidsbruk per aktivitet for det valgte kjønn:
```python
import matplotlib.pyplot as plt
import seaborn as sns

def vis_stolpediagram(kjønn):
    if kjønn == 'Alle':
        df_filtrert = data_akt
    else:
        df_filtrert = data_akt[data_akt['Kjønn'] == kjønn]
    plt.figure(figsize=(10,6))
    sns.barplot(data=df_filtrert, x='Aktivitet', y='Tidsbruk', ci=None)
    plt.title(f"Stolpediagram for tidsbruk - {kjønn}")
    plt.xlabel("Aktivitet")
    plt.ylabel("Tidsbruk (min)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

widgets.interactive(vis_stolpediagram, kjønn=kjønn_widget)
```
Forklar kort hvordan `sns.barplot()` fungerer og hva diagrammet viser.

#### Del 2c-2: Sektordiagram
Lag et sektordiagram som viser andelen av total tidsbruk per aktivitet for det valgte kjønn:
```python
def vis_sektordiagram(kjønn):
    if kjønn == 'Alle':
        df_filtrert = data_akt
    else:
        df_filtrert = data_akt[data_akt['Kjønn'] == kjønn]
    # Gruppér data etter aktivitet og summer tidsbruk
    gruppert = df_filtrert.groupby('Aktivitet')['Tidsbruk'].sum()
    plt.figure(figsize=(8,8))
    plt.pie(gruppert, labels=gruppert.index, autopct='%1.1f%%', startangle=140)
    plt.title(f"Sektordiagram over tidsbruk - {kjønn}")
    plt.axis('equal')
    plt.show()

widgets.interactive(vis_sektordiagram, kjønn=kjønn_widget)
```
Forklar hvordan et sektordiagram viser prosentandeler, og hva parameteren `autopct` gjør.

---

## Ekstra utfordringer (valgfrie)
- Kombiner stolpediagram og sektordiagram slik at begge diagrammene oppdateres samtidig ved valg i dropdownen.
- Konverter notatboken til et frittstående dashboard med Voila. For eksempel, kjør:
  ```bash
  py -m voila din_notebook.ipynb
  ```
- Skriv en kort refleksjonsrapport (ca. 1 side) om hva du har lært om interaktiv datavisualisering med Python.

---

## Tidsplan
**Del 1 – Befolkningsdata:**  
- Teori og demonstrasjoner: 45 minutter  
- Praktiske oppgaver (oppgaver 1a-1e): 45 minutter

**Del 2 – Aktivitetstidsdata:**  
- Teori om filtrering og diagrammer: 30 minutter  
- Praktisk koding og visualisering (oppgaver 2a-2c): 60 minutter

**Fagdag og test:**  
- Fagdag i klasserommet: 180 minutter (gjennomgang, demonstrasjon og praktisk arbeid)  
- Avsluttende test: 90 minutter

---

Denne strukturen gir dere en trinnvis innføring i dataanalyse og interaktiv visualisering med Python, og det legges vekt på mestring gjennom enkle oppgaver før man går videre til mer komplekse utfordringer. Lykke til med arbeidet!
