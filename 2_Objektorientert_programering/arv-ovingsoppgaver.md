# Øvingsoppgaver: Arv i Python 🎯
## Fra enkle til mer utfordrende oppgaver

### Nivå 1: Kom i gang 🌱

**Oppgave 1: Kjæledyr**
```python
class Kjæledyr:
    def __init__(self, navn, alder):
        self.navn = navn
        self.alder = alder
    
    def vis_info(self):
        print(f"{self.navn} er {self.alder} år gammel")

# Din oppgave:
# 1. Lag en klasse Hamster som arver fra Kjæledyr
# 2. Legg til en metode spis_godbit() som printer f"{self.navn} spiser en gulrot!"
# 3. Test klassen din med en hamster
```

**Oppgave 2: Former**
```python
class Form:
    def __init__(self, farge):
        self.farge = farge
    
    def vis_farge(self):
        print(f"Denne formen er {self.farge}")

# Din oppgave:
# 1. Lag en klasse Sirkel som arver fra Form
# 2. Legg til en egenskap radius i __init__
# 3. Lag en metode beregn_omkrets() som returnerer omkretsen (2 * 3.14 * radius)
# 4. Test at du kan bruke både vis_farge() og beregn_omkrets()
```

### Nivå 2: Litt mer utfordrende 🌿

**Oppgave 3: Bibliotek**
```python
class Medium:
    def __init__(self, tittel, år):
        self.tittel = tittel
        self.år = år
        self.er_utlånt = False
    
    def lån_ut(self):
        if not self.er_utlånt:
            self.er_utlånt = True
            return f"{self.tittel} er nå lånt ut"
        return f"{self.tittel} er allerede utlånt"

# Din oppgave:
# 1. Lag en klasse Bok som arver fra Medium
# 2. Legg til forfatter og sideantall i __init__
# 3. Lag en metode vis_info() som printer all informasjon om boken
# 4. Lag en klasse Film som også arver fra Medium
# 5. Legg til regissør og lengde_minutter i __init__ for Film
# 6. Test at både Bok og Film kan bruke lån_ut() fra Medium
```

**Oppgave 4: Bankkonto**
```python
class Konto:
    def __init__(self, kontonummer, eier, saldo=0):
        self.kontonummer = kontonummer
        self.eier = eier
        self.saldo = saldo
    
    def vis_saldo(self):
        return f"Saldo: {self.saldo} kr"
    
    def sett_inn(self, beløp):
        self.saldo += beløp
        return self.vis_saldo()

# Din oppgave:
# 1. Lag en klasse Sparekonto som arver fra Konto
# 2. Legg til en egenskap rente (prosent) i __init__
# 3. Lag en metode beregn_renteinntekt() som returnerer årlig renteinntekt
# 4. Lag en klasse Brukskonto som også arver fra Konto
# 5. Legg til en kredittgrense i Brukskonto
# 6. Lag en metode kan_ta_ut() som sjekker om det er dekning for et beløp
```

### Nivå 3: Mer komplekse oppgaver 🌳

**Oppgave 5: Ansatte**
```python
class Ansatt:
    def __init__(self, navn, ansatt_id, grunnlønn):
        self.navn = navn
        self.ansatt_id = ansatt_id
        self.grunnlønn = grunnlønn
    
    def beregn_lønn(self):
        return self.grunnlønn

# Din oppgave:
# 1. Lag en klasse Selger som arver fra Ansatt
# 2. Legg til provisjonsprosent og månedens_salg i __init__
# 3. Overstyrt beregn_lønn() til å inkludere provisjon av salg
# 4. Lag en klasse Konsulent som arver fra Ansatt
# 5. Legg til timer_jobbet og timerate i __init__
# 6. Overstyrt beregn_lønn() for Konsulent
# 7. Test at ulike typer ansatte får riktig lønn
```

**Oppgave 6: Spill-karakterer**
```python
class Karakter:
    def __init__(self, navn, helse=100):
        self.navn = navn
        self.helse = helse
        self.level = 1
        self.er_i_live = True
    
    def ta_skade(self, skade):
        self.helse -= skade
        if self.helse <= 0:
            self.er_i_live = False
            return f"{self.navn} er beseiret!"
        return f"{self.navn} har {self.helse} helse igjen"

# Din oppgave:
# 1. Lag en klasse Kriger som arver fra Karakter
# 2. Legg til styrke og rustning i __init__
# 3. Overstyrt ta_skade() for å ta hensyn til rustning
# 4. Lag en metode angrip() som returnerer skade basert på styrke
# 5. Lag en klasse Magiker som arver fra Karakter
# 6. Legg til mana og magi_styrke i __init__
# 7. Lag metoder for å kaste ulike typer magi
# 8. Lag en kamp-simulator der karakterene kan kjempe mot hverandre
```

### Nivå 4: Ekstra utfordringer 🌲

**Oppgave 7: Transport-system**
Lag et system for ulike transportmidler:
1. Lag en hovedklasse Kjøretøy med:
   - Egenskaper: merke, modell, år, km_stand
   - Metoder: kjør(), vedlikehold()
2. Lag minst tre ulike typer kjøretøy som arver fra denne
3. Hvert kjøretøy skal ha sine unike egenskaper og metoder
4. Lag et system for å beregne drivstofforbruk
5. Implementer en metode for å sammenligne kjøretøy

**Oppgave 8: Skole-administrasjon**
Lag et komplett system for en skole:
1. Lag en hovedklasse Person med grunnleggende informasjon
2. Lag klasser for Elev, Lærer og Administrativ som arver fra Person
3. Implementer:
   - Karaktersetting for elever
   - Fravær-registrering
   - Timeplan-håndtering
   - Lønn for ansatte
4. Lag metoder for å vise relevant informasjon for hver type person

### Tips for oppgaveløsning 💡
1. Start med å lese oppgaven nøye
2. Planlegg hvilke egenskaper og metoder du trenger
3. Begynn med den enkleste funksjonaliteten
4. Test koden din underveis
5. Bygg på med mer funksjonalitet når det grunnleggende fungerer

### Test din forståelse etter hver oppgave 📝
Spør deg selv:
1. Hvorfor brukte jeg arv i denne oppgaven?
2. Hvilke fordeler ga arv meg i denne løsningen?
3. Kunne jeg løst oppgaven uten arv? Hvorfor/hvorfor ikke?
4. Er det andre måter jeg kunne strukturert klassene på?

### Be om hjelp når du trenger det 🤝
- Hvis du står fast, prøv å forklare problemet til en medelev
- Noen ganger kan det å forklare problemet hjelpe deg å finne løsningen
- Ikke vær redd for å spørre læreren om hjelp
