import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Les CSV-filen
# Merk: For å håndtere æøå og spesialtegn, bruker vi encoding='utf-8'
df = pd.read_csv('Datasett_fodselstall_komma.csv', encoding='utf-8')

# Gi kolonnene mer håndterbare navn
df.columns = ['År', 'Levendefødte', 'Innflyttinger', 'Utflyttinger']

# Vis de første radene og generell informasjon om datasettet
print("De første radene i datasettet:")
print(df.head())
print("\nInformasjon om datasettet:")
print(df.info())
print("\nStatistisk oversikt:")
print(df.describe())

# Beregn netto innvandring (der data eksisterer)
df['Netto_innvandring'] = df['Innflyttinger'] - df['Utflyttinger']

# Lag en visualisering av trendene
plt.figure(figsize=(12, 6))
plt.plot(df['År'], df['Levendefødte'], label='Levendefødte')
plt.plot(df['År'], df['Innflyttinger'], label='Innflyttinger')
plt.plot(df['År'], df['Utflyttinger'], label='Utflyttinger')

plt.title('Fødsels- og innvandringstall i Norge (1945-2023)')
plt.xlabel('År')
plt.ylabel('Antall')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)

# For bedre lesbarhet, vis bare hvert 5. år på x-aksen
plt.xticks(df['År'][::5])

plt.tight_layout()
plt.show()

# Vis noen nøkkeltall for de siste 10 årene
siste_10_ar = df.tail(10)
print("\nOversikt over de siste 10 årene:")
print(siste_10_ar[['År', 'Levendefødte', 'Innflyttinger', 'Utflyttinger', 'Netto_innvandring']])