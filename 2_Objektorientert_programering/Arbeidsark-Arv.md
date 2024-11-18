# Introduksjon til arv i Python
## En steg-for-steg guide for å forstå arv i programmering

### Del 1: Hva er arv? 🤔

La oss starte med noe kjent før vi går inn i programmeringen. 

**Tenk på streaming-tjenester som Netflix:**
- Du har ulike typer innhold: Filmer, Serier, Dokumentarer
- Alt innholdet har noen felles egenskaper:
  - Tittel
  - Lengde
  - Utgivelsesår
  - Rating
- Men hver type har også sine spesielle egenskaper:
  - Filmer har regissør og skuespillere
  - Serier har antall episoder og sesonger
  - Dokumentarer har forteller og tema

Dette er akkurat slik arv fungerer i programmering! Vi kan ha en hovedgruppe (innhold) og undergrupper (film, serie) som arver egenskaper fra hovedgruppen.

**La oss se på et enkelt eksempel:**
```python
# Dette er hovedgruppen (vi kaller den "foreldreklassen")
class Innhold:
    def __init__(self, tittel, år, lengde_minutter):
        self.tittel = tittel
        self.år = år
        self.lengde = lengde_minutter
        self.rating = 0
    
    def gi_rating(self, score):
        self.rating = score
        print(f"{self.tittel} har fått {score} stjerner")

# Dette er en undergruppe (vi kaller den "barneklassen")
class Film(Innhold):
    def __init__(self, tittel, år, lengde_minutter, regissør):
        super().__init__(tittel, år, lengde_minutter)
        self.regissør = regissør
    
    def vis_info(self):
        return f"{self.tittel} ({self.år}) av {self.regissør}"

# La oss prøve å bruke det vi har laget
inception = Film("Inception", 2010, 148, "Christopher Nolan")
inception.gi_rating(5)    # Dette virker fordi Film arvet gi_rating() fra Innhold
print(inception.vis_info())  # Dette er filmens egen spesielle metode
```

### Del 2: Forstå begrepene 📚

La oss ta for oss de viktige begrepene ett for ett:

1. **Klasse**
   - En klasse er som en mal eller oppskrift
   - Den beskriver hva noe er og hva det kan gjøre
   - For eksempel: En Innhold-klasse beskriver hva alt innhold har felles

2. **Foreldreklasse** (også kalt superklasse)
   - Dette er den generelle klassen som andre klasser arver fra
   - I eksempelet vårt er Innhold foreldreklassen
   - Den inneholder egenskaper og handlinger som er felles for alle "barna"

3. **Barneklasse** (også kalt subklasse)
   - Dette er en mer spesialisert versjon av foreldreklassen
   - Den arver alle egenskaper fra foreldreklassen
   - Den kan også ha sine egne spesielle egenskaper
   - I eksempelet vårt er Film barneklassen

4. **Arv**
   - Når en klasse får egenskaper og handlinger fra en annen klasse
   - I Python viser vi dette ved å skrive: `class Barneklasse(Foreldreklasse):`
   - For eksempel: `class Film(Innhold):`

### Del 3: La oss prøve sammen 👥

**Oppgave 1: Forstå arv**
La oss lage en Serie-klasse:
```python
# Vi har allerede Innhold-klassen fra før
class Serie(Innhold):
    def __init__(self, tittel, år, lengde_minutter, antall_sesonger):
        super().__init__(tittel, år, lengde_minutter)
        self.antall_sesonger = antall_sesonger
    
    def neste_episode(self):
        return f"Spiller neste episode av {self.tittel}"

# La oss teste den:
stranger_things = Serie("Stranger Things", 2016, 50, 4)
stranger_things.gi_rating(4)  # Dette kommer fra Innhold-klassen
print(stranger_things.neste_episode())  # Dette er seriens egen metode
```

**Spørsmål å tenke på:**
1. Hvilke metoder har stranger_things tilgang til?
2. Hvor kommer disse metodene fra?
3. Hvorfor er det nyttig at Serie arver fra Innhold?

### Del 4: Din tur! 🎯

**Oppgave: Lag et sosialt medie-innlegg system**
1. Start med denne koden:
```python
class Innlegg:
    def __init__(self, bruker, tekst):
        self.bruker = bruker
        self.tekst = tekst
        self.likes = 0
        self.kommentarer = []
    
    def lik(self):
        self.likes += 1
        print(f"Innlegget har nå {self.likes} likes")

# Lag din egen innleggstype her:
class BildeInnlegg(Innlegg):
    # Legg til noe spesielt som ditt innlegg kan gjøre
    pass

# Test ditt innlegg her:
mitt_innlegg = BildeInnlegg("ditt_brukernavn", "Min første post!")
```

2. Velg en type innlegg (bilde, video, story)
3. Gi innlegget minst én spesiell egenskap
4. Test at innlegget både kan bruke metodene fra Innlegg og sine egne spesielle metoder

### Del 5: La oss diskutere 💭

Snakk med sidemannen om:
1. Hvilken type innlegg lagde dere?
2. Hvilke spesielle egenskaper ga dere til innlegget?
3. Hvorfor var det nyttig å ha en felles Innlegg-klasse?
4. Kan dere tenke på andre sosiale medie-funksjoner hvor arv kunne vært nyttig?

### Del 6: Viktig å huske ⭐

1. Arv lar oss:
   - Gjenbruke kode (vi slipper å skrive de samme tingene om og om igjen)
   - Organisere koden vår på en ryddig måte
   - Lage spesialiserte versjoner av ting vi allerede har

2. Når vi bruker arv:
   - Barneklassen får automatisk alle egenskaper fra foreldreklassen
   - Barneklassen kan ha sine egne spesielle egenskaper i tillegg
   - Vi kan bruke både arvede og egne metoder på barneklassen

### Del 7: Test deg selv 📝

1. Hva mener vi med "arv" i programmering?
2. Hva er forskjellen på en foreldreklasse og en barneklasse?
3. Hvorfor er arv nyttig når vi programmerer?

### Del 8: Utfordring for de som vil prøve mer 🚀

Prøv å lage et system for en musikk-app:
1. Lag en Spor-klasse med grunnleggende egenskaper (tittel, artist, lengde)
2. Lag Sang og Podcast som egne klasser som arver fra Spor
3. Gi dem spesielle egenskaper som passer for deres type

### Tips for å lykkes 💡
- Ta ett steg om gangen
- Test koden din ofte
- Spør om hjelp hvis du står fast
- Samarbeid med andre elever

-------------------

**Husk:**
- Det er lov å gjøre feil - det er slik vi lærer!
- Start enkelt og bygg videre når du forstår det grunnleggende
- Spør hvis noe er uklart - det er derfor læreren er her!
