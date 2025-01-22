import pandas as pd

# Load the dataset
df = pd.read_csv('Datasett_fodselstall_komma.csv')

# Calculate netto folkevekst
df['netto_folkevekst'] = df['fødselstall'] - df['innflyttinger'] + df['utflyttinger']

# Display the result
print(df[['fødselstall', 'innflyttinger', 'utflyttinger', 'netto_folkevekst']])
