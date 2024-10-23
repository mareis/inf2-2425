import operator

personer = [
    {'fornavn': 'Kari', 'etternavn': 'Hansen', 'fødselsår': 2001},
    {'fornavn': 'Gustav', 'etternavn': 'Monsen', 'fødselsår': 1995},
    {'fornavn': 'Anette', 'etternavn': 'Ås', 'fødselsår': 1998},
    {'fornavn': 'Marius', 'etternavn': 'Lie', 'fødselsår': 2002},
    {'fornavn': 'Wenche', 'etternavn': 'Hovland', 'fødselsår': 1999}
]
valg = int(input(
    f'1: Fornavn\n'
    f'2: Etternavn\n'
    f'3: Fødselsår\n'
    f'0: Avslutt\n'
))
sortering = list(personer[0].keys())[valg - 1]

kolonner = ""
for key in personer[0].keys():
    kolonner += key.capitalize() + " " * 5

print(kolonner)
print("_" * 35)

for person in sorted(personer, key=operator.itemgetter(sortering), reverse=False):
    print(f'{person["fornavn"]:12}{person["etternavn"]:8}{person["fødselsår"]:10}')