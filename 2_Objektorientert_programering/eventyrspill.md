# Praktisk Oppgave: Lag ditt eget Tekstbaserte Eventyrspill

I denne oppgaven skal du bruke objektorientert programmering til å lage et enkelt tekstbasert eventyrspill. Du vil lære hvordan du kan bruke klasser og objekter til å representere spillkomponenter som spillere, monstre og skatter.

## Scenario

Du er en eventyrer som utforsker en mystisk hule full av skatter og monstre. Målet ditt er å finne skatten uten å bli fanget av monstrene.

---

## Trinn 1: Definer klassen `Spiller`

Først trenger vi en klasse som representerer spilleren.

### Oppgave 1:

- Lag en klasse `Spiller` med følgende egenskaper:
  - `navn`
  - `helse` (starter på 100)
  - `styrke` (et tall mellom 5 og 10)

- Legg til en metode `angrip()` som returnerer spillerens styrkeverdi.

---

## Trinn 2: Definer klassen `Monster`

Vi trenger også en klasse for monstrene i hulen.

### Oppgave 2:

- Lag en klasse `Monster` med følgende egenskaper:
  - `navn` (f.eks. "Goblin", "Troll")
  - `helse` (et tall mellom 50 og 100)
  - `styrke` (et tall mellom 5 og 15)

- Legg til en metode `angrip()` som returnerer monsterets styrkeverdi.

---

## Trinn 3: Definer klassen `Skatt`

La oss også ha en klasse for skattene spilleren kan finne.

### Oppgave 3:

- Lag en klasse `Skatt` med følgende egenskaper:
  - `navn` (f.eks. "Gullmynt", "Diamant")
  - `verdi` (et tall som representerer skattenes verdi)

---

## Trinn 4: Samhandle med objektene

Nå skal vi bruke disse klassene til å simulere en enkel hendelse i spillet.

### Oppgave 4:

- Opprett et `Spiller`-objekt med et navn du velger.
- Opprett et `Monster`-objekt (du kan velge navn, helse og styrke).
- Skriv en enkel kampsekvens der:
  - Spilleren og monsteret angriper hverandre i tur.
  - Trekk styrkeverdien fra motstanderens helse ved hvert angrep.
  - Fortsett til enten spilleren eller monsterets helse er 0 eller mindre.
- Skriv ut hva som skjer i hver runde.

**Eksempel på output:**

```
Spiller angriper Goblin og gjør 8 skade.
Goblin har nå 42 helse igjen.
Goblin angriper Spiller og gjør 6 skade.
Spiller har nå 94 helse igjen.
...
```
---

## Trinn 5: Utvid spillet (Frivillig)

Hvis du vil, kan du utvide spillet ytterligere.

### Oppgave 5:

- Lag en liste over flere monstre og skatter.
- La spilleren bevege seg gjennom hulen og møte tilfeldige monstre eller finne skatter.
- Legg til valgmuligheter for spilleren, som å angripe eller flykte.

---

## Oppsummering

Gjennom denne oppgaven har du:

- Lært hvordan du definerer klasser og oppretter objekter.
- Brukt egenskaper og metoder til å modellere spillkomponenter.
- Skapt interaksjoner mellom objekter.

---

