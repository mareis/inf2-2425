# 🎃 Halloween-programmering: Funksjoner i Python 🎃

## Del 1: Enkle funksjoner uten parameter og returverdi 🧙‍♂️
I denne delen skal vi lære å lage enkle funksjoner som kan skremme vettet av folk!

### Oppgave 1.1 
Lag en funksjon som heter `spøkelse()` som skriver ut "Buuuuuu!" når den kalles.
```python
# Din kode her
```

### Oppgave 1.2
Lag en funksjon som heter `tegn_gresskar()` som skriver ut et mønster av stjerner som ligner et gresskar:
```python
 *****
*     *
* ^ ^ *
*  >  *
 *****
```

## Del 2: Funksjoner med parameter 🧛‍♂️
Nå skal vi lage funksjoner som kan ta imot informasjon og bruke den til å spre Halloween-stemning!

### Oppgave 2.1
Lag en funksjon `skrem_person(navn)` som tar imot et navn og skriver ut en skremmende hilsen til denne personen.
```python
# Eksempel på bruk:
skrem_person("Ada")  # Skal skrive ut: "Møørke hilsener, Ada! Spøkelsene ser deg! 👻"
```

### Oppgave 2.2
Lag en funksjon `tegn_spøkelseshus(bredde, høyde)` som tegner et hjemsøkt hus av stjerner med gitt bredde og høyde.
```python
# Eksempel på bruk:
tegn_spøkelseshus(4, 3)
# Skal gi:
#  /\
# ****
# |  |
```

## Del 3: Funksjoner med returverdi 🎃
Her skal vi lage funksjoner som kan gi tilbake verdier vi kan bruke senere.

### Oppgave 3.1
Lag en funksjon `beregn_godteri(barn, godteri_per_barn)` som returnerer hvor mye godteri som trengs totalt.
```python
# Eksempel på bruk:
total_godteri = beregn_godteri(5, 10)
print(f"Du trenger {total_godteri} godteri til Halloween-festen! 🍬")
```

### Oppgave 3.2
Lag en funksjon `tell_monstre(tekst)` som teller hvor mange ganger ordene "spøkelse", "vampyr", "zombie" eller "heks" forekommer i en tekst.
```python
# Eksempel på bruk:
antall = tell_monstre("Det var en heks og to spøkelser i huset")
print(f"Det er {antall} monstre i historien! 👻")
```

## Del 4: Kombinere funksjoner 🧟‍♂️
Nå skal vi lage programmer som bruker flere funksjoner sammen.

### Oppgave 4.1: Monster-temperatur
Lag to funksjoner:
- `menneske_til_monster_temp(menneske_temp)` som konverterer vanlig temperatur til monster-temperatur (gang med 0.666)
- `monster_til_menneske_temp(monster_temp)` som konverterer tilbake

Lag deretter et program som konverterer frem og tilbake for å sjekke om regningen stemmer!

### Oppgave 4.2: Heksebrygg-kalkulator
Lag følgende funksjoner:
- `bland(ingrediens1, ingrediens2)` - blander to ingredienser
- `kok(ingrediens)` - koker en ingrediens
- `knus(ingrediens)` - knuser en ingrediens
- `lagBrygg(oppskrift)` - følger en heksebrygg-oppskrift

```python
# Eksempel på bruk:
resultat = lagBrygg(["øgleøyne", "flaggermusvinger"])
print(f"Din brygg er: {resultat} 🧪")
```

### Oppgave 4.3: Monstervalidering
Lag et system som sjekker om et monster er skummelt nok. Del opp i følgende funksjoner:
- `har_skarpe_tenner(monster)` - sjekker om monsteret har skarpe tenner
- `kan_fly(monster)` - sjekker om monsteret kan fly
- `er_nattaktiv(monster)` - sjekker om monsteret er aktivt om natten
- `har_magiske_krefter(monster)` - sjekker om monsteret har magiske krefter
- `er_stort_nok(monster)` - sjekker om monsteret er minst 2 meter høyt

Lag til slutt en hovedfunksjon `valider_monster(monster)` som bruker alle disse funksjonene.

### Oppgave 4.4: Spøkelseshistorie-generator
Lag et system for å generere spøkelseshistorier med følgende funksjoner:
- `velg_setting()` - velger tilfeldig sted (hjemsøkt hus, kirkegård, etc.)
- `velg_monster()` - velger tilfeldig monster
- `velg_hendelse()` - velger tilfeldig skummel hendelse
- `lag_historie(lengde)` - genererer en historie av ønsket lengde

```python
# Eksempel på bruk:
historie = lag_historie(3)  # Genererer historie med 3 hendelser
print(f"🦇 Din spøkelseshistorie: {historie}")
```

### Oppgave 4.5: Godteributikk-system
Lag et Halloween-butikksystem med følgende funksjoner:
- `opprett_godteri(navn, pris, skremmefaktor)` - oppretter et godteri
- `beregn_pris(godteri, antall)` - beregner totalprisen
- `beregn_sukkerinnhold(godteri)` - beregner sukkermengden
- `formater_kvittering(handlekurv)` - lager en spooky kvittering

```python
# Eksempel på bruk:
handlekurv = [
    {"godteri": opprett_godteri("Øyeeple-gelé", 15.50, 8), "antall": 3},
    {"godteri": opprett_godteri("Vampyrtannpinner", 25.90, 9), "antall": 2}
]
print(lag_ordre(handlekurv)) # 🍬
```

### Oppgave 4.6: Monster-kampssystem
Lag et enkelt kampsystem med følgende funksjoner:
- `opprett_monster(navn, type)` - oppretter et monster med spesielle egenskaper
- `angrip(monster1, monster2)` - håndterer et angrep mellom to monstre
- `bruk_spesialevne(monster)` - aktiverer monsteres spesialevne
- `er_beseiret(monster)` - sjekker om et monster er beseiret
- `vis_monster_status(monster)` - viser monsteres nåværende tilstand

```python
# Eksempel på bruk:
vampyr = opprett_monster("Dracula", "vampyr")
varulv = opprett_monster("Fenris", "varulv")
kjør_monsterkamp(vampyr, varulv) # 🧛‍♂️ vs 🐺
```

## Ekspertoppgaver 🏆
Disse oppgavene er for deg som virkelig vil utfordre deg selv!

### Ekspertoppgave 1: Forbannelseskalkulator 🧙‍♀️
Lag et program som kan beregne styrken og varigheten av magiske forbannelser ved hjelp av rekursjon og minnelagring.

1. Lag følgende funksjoner:
- `beregn_forbannelse_styrke(ingredienser, måne_fase)` 
- `kombinerer_forbannelser(forbannelse1, forbannelse2)`
- `finn_motgift(forbannelse)`
- `simuler_forbannelse_over_tid(forbannelse, dager)`

2. Programmet skal:
- Håndtere kombinasjoner av ulike ingredienser
- Beregne hvordan månefaser påvirker styrken
- Finne optimale motgifter
- Visualisere forbannelsens styrke over tid

### Ekspertoppgave 2: Avansert Spøkelsesdeteksjon 👻
Lag et program som kan analysere "spøkelsesaktivitet" i forskellige bygninger.

1. Lag følgende hovedfunksjoner:
- `analyser_aktivitet(målinger)` - analyserer EMF-målinger og temperaturfall
- `identifiser_spøkelsestype(mønstre)` - kategoriserer type spøkelse
- `beregn_hjemsøkelsesnivå(data)` - estimerer hvor hjemsøkt et sted er
- `generer_aktivitetsrapport(sted, tid, målinger)` - lager detaljert rapport

2. Implementer avansert dataanalyse for:
- Mønstergjenkjenning i spøkelsesaktivitet
- Korrelasjon mellom ulike typer aktivitet
- Prediksjon av fremtidig aktivitet
- Visualisering av "hot spots" i bygninger

## Bonustips for alle oppgavene 🎃
- Husk å legge til dokumentasjon (docstrings) i funksjonene dine
- Test funksjonene dine grundig med forskjellige input-verdier
- Tenk på hva som kan gå galt og håndter feil på en pen måte
- Ha det gøy mens du programmerer! 👻