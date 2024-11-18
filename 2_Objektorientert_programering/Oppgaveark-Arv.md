# Arv i Python - IT2
## Med eksempler fra din hverdag 🎮 🎵 📱

### Del 1: Forstå konseptet arv

La oss starte med noe kjent: Strømmetjenester som Spotify og Netflix.
Tenk på hvordan innhold er organisert:
- Alt innhold har noen felles egenskaper (tittel, lengde, år, etc.)
- Men ulike typer innhold har også sine spesielle egenskaper
- En film har skuespillere og regissør
- En serie har episoder og sesonger
- En låt har artist og album

Dette er et perfekt eksempel på når vi kan bruke arv i programmering!

```python
class Innhold:
    def __init__(self, tittel, år, lengde_minutter):
        self.tittel = tittel
        self.år = år
        self.lengde = lengde_minutter
        self.likes = 0
    
    def lik(self):
        self.likes += 1
        return f"👍 {self.tittel} har nå {self.likes} likes"

class Film(Innhold):
    def __init__(self, tittel, år, lengde_minutter, regissør, aldersgrense):
        # Vi bruker super() for å kalle Innhold sin __init__
        super().__init__(tittel, år, lengde_minutter)
        self.regissør = regissør
        self.aldersgrense = aldersgrense
    
    def vis_info(self):
        return f"{self.tittel} ({self.år}) - Regissert av {self.regissør}"

# La oss teste:
inception = Film("Inception", 2010, 148, "Christopher Nolan", 12)
print(inception.vis_info())
print(inception.lik())  # Vi kan bruke lik() fordi Film arvet den fra Innhold
```

### Del 2: Øvingsoppgaver - Nivå 1 🎯

**Oppgave 1: Spotify-lignende System**
```python
class Media:
    def __init__(self, tittel, artist, lengde_sekunder):
        self.tittel = tittel
        self.artist = artist
        self.lengde = lengde_sekunder
        self.avspillinger = 0
    
    def spill_av(self):
        self.avspillinger += 1
        return f"▶️ Spiller av {self.tittel}"

# Din oppgave:
# 1. Lag en klasse Sang som arver fra Media
# 2. Legg til album og sjanger i __init__
# 3. Lag en spilleliste-funksjon
# 4. Test med noen av dine favorittlåter
```

**Oppgave 2: SoMe-Post System**
```python
class Post:
    def __init__(self, bruker, tekst):
        self.bruker = bruker
        self.tekst = tekst
        self.likes = 0
        self.kommentarer = []
    
    def legg_til_kommentar(self, kommentar):
        self.kommentarer.append(kommentar)

# Din oppgave:
# 1. Lag en klasse BildePost som arver fra Post
# 2. Legg til bilde_url og filter i __init__
# 3. Lag en klasse VideoPost som også arver fra Post
# 4. Legg til video_lengde og visninger i VideoPost
```

### Del 3: Mer Avanserte Oppgaver 🚀

**Oppgave 3: Gaming Character System**
```python
class Spiller:
    def __init__(self, brukernavn, level=1):
        self.brukernavn = brukernavn
        self.level = level
        self.xp = 0
        self.achievements = []
    
    def få_xp(self, mengde):
        self.xp += mengde
        if self.xp >= 100:
            self.level_up()
    
    def level_up(self):
        self.level += 1
        self.xp = 0

# Din oppgave:
# 1. Lag en klasse CompetitiveSpiller som arver fra Spiller
# 2. Legg til rank og competitive_points
# 3. Lag en metode for å oppdatere rank basert på vinst/tap
# 4. Lag en klasse CasualSpiller med andre relevante egenskaper
```

**Oppgave 4: E-commerce System**
```python
class Produkt:
    def __init__(self, navn, pris, lager_antall):
        self.navn = navn
        self.pris = pris
        self.lager_antall = lager_antall
    
    def kjøp(self, antall):
        if antall <= self.lager_antall:
            self.lager_antall -= antall
            return True
        return False

# Din oppgave:
# 1. Lag klasser for ulike produkttyper (Elektronikk, Klær, etc.)
# 2. Legg til relevante egenskaper for hver type
# 3. Implementer rabatt-system
# 4. Lag handlekurv-funksjonalitet
```

### Del 4: Gruppe-prosjekt: Festival-app 🎵

Lag et system for en musikkfestival med følgende klasser:

```python
class Arrangement:
    def __init__(self, navn, dato, sted):
        self.navn = navn
        self.dato = dato
        self.sted = sted
        self.deltakere = []

# Din gruppes oppgave:
# 1. Lag klasser for ulike typer arrangementer:
#    - Konsert (artist, sjanger, varighet)
#    - Workshop (instruktør, tema, maks_deltakere)
#    - Konkurranse (premie, påmeldingsfrist)
# 2. Implementer billettsystem med ulike billettyper
# 3. Lag funksjonalitet for påmelding og avmelding
# 4. Implementer schema-visning
```

### Del 5: Real-world Utfordring: Streaming-plattform 📺

**Scenario:** Du skal lage backend for en ny streaming-tjeneste.

```python
class Innhold:
    def __init__(self, tittel, produksjonsår, aldersgrense):
        self.tittel = tittel
        self.år = produksjonsår
        self.aldersgrense = aldersgrense
        self.rating = 0
        self.antall_ratings = 0
    
    def gi_rating(self, score):
        self.rating = ((self.rating * self.antall_ratings) + score) / (self.antall_ratings + 1)
        self.antall_ratings += 1

# Din oppgave:
# 1. Utvid systemet med klasser for:
#    - Film (regissør, skuespillere, sjanger)
#    - Serie (episoder, sesonger, status)
#    - Dokumentar (tema, forteller)
# 2. Implementer:
#    - Anbefalingssystem
#    - Fortsett å se-funksjon
#    - Personlig watchlist
```

### Tips for oppgaveløsning 💡
1. Tenk gjennom hva som er felles for alle typer (dette hører hjemme i hovedklassen)
2. Identifiser hva som er unikt for hver type (dette hører hjemme i subklassene)
3. Test koden din med realistiske eksempler
4. Tenk på hvordan dette ligner på systemer du bruker til daglig

### Utfordrende Elementer å Legge Til 🌟
- Implementer JSON-lagring av data
- Lag et enkelt brukergrensesnitt
- Legg til statistikk og analyser
- Implementer søkefunksjonalitet
- Legg til vennelister og delingsmuligheter

### Refleksjonsspørsmål 🤔
1. Hvordan ligner dette på ekte systemer du bruker?
2. Hvilke andre funksjoner kunne vært nyttige å legge til?
3. Hvordan ville du strukturert systemet annerledes?
4. Hvilke sikkerhetshensyn burde tas i et slikt system?
