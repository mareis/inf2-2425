import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Laste inn 'penguins'-datasettet
df = sns.load_dataset('penguins')

# Tittel for applikasjonen
st.title('Pingvin Datautforsker')

# a) Presentasjon av data
st.subheader('a) Presentasjon av data')
st.write('Viser de første radene av pengvindataene:')
st.dataframe(df.head())

# b) Filtrering etter art
st.subheader('b) Filtrering etter art')
art = st.multiselect(
    'Velg art(er):',
    options=df['species'].unique(),
    default=df['species'].unique()
)

# Filtrere datasettet basert på valgt art
filtrert_df = df[df['species'].isin(art)]

# Vise filtrerte data
st.write(f'Data for valgt(e) art(er): {", ".join(art)}')
st.dataframe(filtrert_df)

# c) Visualisering av data

# Stolpediagram: Gjennomsnittlig nebb-lengde per art
st.subheader('c) Visualisering av data')
st.write('**Stolpediagram over gjennomsnittlig nebb-lengde per art**')

# Beregne gjennomsnittlig nebb-lengde
gj_snitt_nebblengde = filtrert_df.groupby('species')['bill_length_mm'].mean().reset_index()

# Lage stolpediagram
fig1, ax1 = plt.subplots()
sns.barplot(data=gj_snitt_nebblengde, x='species', y='bill_length_mm', ax=ax1)
ax1.set_title('Gjennomsnittlig nebb-lengde per art')
ax1.set_xlabel('Art')
ax1.set_ylabel('Nebblengde (mm)')

st.pyplot(fig1)

# Scatterplot: Nebb-lengde vs. nebb-dybde
st.write('**Scatterplot av nebb-lengde mot nebb-dybde**')
fig2, ax2 = plt.subplots()
sns.scatterplot(data=filtrert_df, x='bill_length_mm', y='bill_depth_mm', hue='species', ax=ax2)
ax2.set_title('Nebblengde vs. Nebbdybde')
ax2.set_xlabel('Nebblengde (mm)')
ax2.set_ylabel('Nebbdybde (mm)')

st.pyplot(fig2)
