# Arbeidsark: Funksjoner i Python 🐍

## Del 1: Enkle funksjoner uten parameter og returverdi
I denne delen skal vi lære å lage enkle funksjoner som utfører bestemte oppgaver.

### Oppgave 1.1
Lag en funksjon som heter `hilsen()` som skriver ut "Hei verden!" når den kalles.
```python
# Din kode her
```

### Oppgave 1.2
Lag en funksjon som heter `tegn_stjerner()` som skriver ut et mønster av stjerner:
```python
*****
*****
*****
```

## Del 2: Funksjoner med parameter
Nå skal vi lage funksjoner som kan ta imot informasjon og bruke den.

### Oppgave 2.1
Lag en funksjon `personlig_hilsen(navn)` som tar imot et navn og skriver ut en hilsen til denne personen.
```python
# Eksempel på bruk:
personlig_hilsen("Ada")  # Skal skrive ut: "Hei, Ada! Håper du har en fin dag!"
```

### Oppgave 2.2
Lag en funksjon `tegn_rektangel(bredde, høyde)` som tegner et rektangel av stjerner med gitt bredde og høyde.
```python
# Eksempel på bruk:
tegn_rektangel(4, 3)
# Skal gi:
# ****
# ****
# ****
```

## Del 3: Funksjoner med returverdi
Her skal vi lage funksjoner som kan gi tilbake verdier vi kan bruke senere.

### Oppgave 3.1
Lag en funksjon `beregn_areal(lengde, bredde)` som returnerer arealet av et rektangel.
```python
# Eksempel på bruk:
areal = beregn_areal(5, 3)
print(f"Arealet er {areal} kvadratmeter")
```

### Oppgave 3.2
Lag en funksjon `tell_bokstaver(tekst, bokstav)` som teller hvor mange ganger en bestemt bokstav forekommer i en tekst.
```python
# Eksempel på bruk:
antall = tell_bokstaver("programmering", "m")
print(f"Bokstaven forekommer {antall} ganger")
```

## Del 4: Kombinere funksjoner
Nå skal vi lage programmer som bruker flere funksjoner sammen.

### Oppgave 4.1: Temperaturkonvertering
Lag to funksjoner:
- `celsius_til_fahrenheit(celsius)` som konverterer fra celsius til fahrenheit
- `fahrenheit_til_celsius(fahrenheit)` som konverterer fra fahrenheit til celsius

Lag deretter et program som bruker begge funksjonene til å:
1. Konvertere 20°C til fahrenheit
2. Ta svaret og konvertere det tilbake til celsius
3. Sjekk at du får 20°C igjen!

### Oppgave 4.2: Enkel kalkulator
Lag følgende funksjoner:
- `pluss(a, b)` - returnerer summen av to tall
- `minus(a, b)` - returnerer differansen mellom to tall
- `gang(a, b)` - returnerer produktet av to tall
- `del(a, b)` - returnerer kvotienten av to tall (husk å sjekke for deling på 0!)

Lag deretter en funksjon `kalkuler(tall1, operasjon, tall2)` som bruker de andre funksjonene til å utføre beregningen.

### Oppgave 4.3: Passordvalidering
Lag et system som sjekker om et passord er sterkt nok. Del opp i følgende funksjoner:
- `har_stor_bokstav(passord)` - sjekker om passordet inneholder minst én stor bokstav
- `har_liten_bokstav(passord)` - sjekker om passordet inneholder minst én liten bokstav
- `har_tall(passord)` - sjekker om passordet inneholder minst ett tall
- `har_spesialtegn(passord)` - sjekker om passordet inneholder minst ett spesialtegn
- `er_langt_nok(passord)` - sjekker om passordet er minst 8 tegn langt

Lag til slutt en hovedfunksjon `valider_passord(passord)` som bruker alle disse funksjonene og returnerer True bare hvis alle kravene er oppfylt.

### Oppgave 4.4: Tekstbehandling
Lag et system for å analysere og modifisere tekst med følgende funksjoner:
- `fjern_tegnsetting(tekst)` - fjerner all tegnsetting fra teksten
- `tell_ord(tekst)` - teller antall ord i teksten
- `finn_lengste_ord(tekst)` - finner det lengste ordet i teksten
- `lag_akronym(tekst)` - lager et akronym av første bokstav i hvert ord

Lag deretter en funksjon `analyser_tekst(tekst)` som bruker alle funksjonene og returnerer en ordbok med resultatene.

```python
# Eksempel på bruk:
tekst = "Python er et morsomt programmeringsspråk!"
resultat = analyser_tekst(tekst)
print(f"Antall ord: {resultat['antall_ord']}")
print(f"Lengste ord: {resultat['lengste_ord']}")
print(f"Akronym: {resultat['akronym']}")
```

### Oppgave 4.5: Butikksystem
Lag et enkelt butikksystem med følgende funksjoner:
- `opprett_vare(navn, pris)` - oppretter en ordbok som representerer en vare
- `beregn_pris(vare, antall)` - beregner totalprisen for et antall av en vare
- `beregn_moms(pris)` - beregner moms (25% av prisen)
- `formater_kvittering(varer, antall)` - lager en pen kvittering som tekst

Lag til slutt en funksjon `lag_ordre(handleliste)` som tar imot en liste med varer og antall, og produserer en fullstendig kvittering.

```python
# Eksempel på bruk:
handleliste = [
    {"vare": opprett_vare("Melk", 23.50), "antall": 2},
    {"vare": opprett_vare("Brød", 35.90), "antall": 1}
]
print(lag_ordre(handleliste))
```

### Oppgave 4.6: Spillsystem
Lag et enkelt spill-system med følgende funksjoner:
- `opprett_spiller(navn)` - oppretter en spiller med navn og start-HP (100)
- `angrip(angriper, forsvarer)` - håndterer et angrep mellom to spillere
- `helbred(spiller, mengde)` - helbreder en spiller
- `er_i_live(spiller)` - sjekker om en spiller fortsatt lever
- `vis_status(spiller)` - viser spillerens nåværende status

Lag deretter en funksjon `kjør_kamp(spiller1, spiller2)` som simulerer en kamp mellom to spillere.

```python
# Eksempel på bruk:
spiller1 = opprett_spiller("Thor")
spiller2 = opprett_spiller("Loki")
kjør_kamp(spiller1, spiller2)
```

[Resten av innholdet forblir det samme...]
## Utfordringsoppgave
Lag et enkelt tekstbasert spill der spilleren skal gjette et tall mellom 1 og 100. Bruk følgende funksjoner:
- `lag_tilfeldig_tall()` - genererer et tilfeldig tall mellom 1 og 100
- `sjekk_gjetting(gjetting, fasit)` - returnerer "For høyt", "For lavt" eller "Riktig!"
- `spill_runde()` - håndterer en hel spillrunde
- `hovedprogram()` - starter spillet og lar spilleren spille flere runder

Tips: Bruk `random.randint(1, 100)` for å generere tilfeldige tall.


## Ekspertoppgaver 🏆
Disse oppgavene er for deg som virkelig vil utfordre deg selv!

### Ekspertoppgave 1: Fibonacci-kalkulator med cache
Lag et program som regner ut Fibonacci-tall effektivt ved hjelp av flere funksjoner og minnelagring (caching).

1. Lag følgende funksjoner:
- `lag_fibonacci_cache()` - oppretter en ordbok for å lagre tidligere utregnede Fibonacci-tall
- `fibonacci(n, cache)` - regner ut det n-te Fibonacci-tallet ved hjelp av cache
- `print_fibonacci_sekvens(antall)` - skriver ut de første n Fibonacci-tallene
- `finn_fibonacci_under(maksverdi)` - finner alle Fibonacci-tall under en gitt verdi

2. Programmet skal:
- Bruke rekursjon OG iterasjon (lag to ulike versjoner)
- Håndtere store tall effektivt (test med n = 1000)
- Inkludere tidtaking for å sammenligne de ulike metodene
- Ha feilhåndtering for negative tall og andre ugyldige input

```python
# Eksempel på bruk:
cache = lag_fibonacci_cache()
print(fibonacci(100, cache))  # Skal regne ut det 100. Fibonacci-tallet lynraskt
print(finn_fibonacci_under(1000))  # Skal finne alle Fibonacci-tall under 1000
```

### Ekspertoppgave 2: Avansert Tekstanalyse
Lag et program som kan analysere tekst ved hjelp av flere spesialiserte funksjoner. Programmet skal kunne analysere både enkelttekster og sammenligne flere tekster.

1. Lag følgende hovedfunksjoner:
- `analyser_tekst(tekst)` - hovedfunksjon som kaller andre funksjoner og samler resultater
- `finn_ordfrekvens(tekst)` - lager ordbok med ord og deres frekvens
- `finn_setninger(tekst)` - deler tekst inn i setninger
- `beregn_lesbarhet(tekst)` - regner ut tekstens lesbarhetsnivå
- `finn_vanligste_ordkombinasjoner(tekst, lengde)` - finner vanlige ordmønstre

2. Lag hjelpefunksjoner for:
- Fjerning av tegnsetting og spesialtegn
- Normalisering av tekst (store/små bokstaver)
- Identifisering av ordklasser (verb, substantiv, etc.)
- Beregning av statistikk (gjennomsnitt, median, etc.)

3. Lag analysefunksjoner som:
- Finner de mest unike ordene i en tekst sammenlignet med en annen
- Identifiserer mulige sitater eller plagiering
- Genererer en lesbarhetsscore basert på:
  * Gjennomsnittlig ordlengde
  * Gjennomsnittlig setningslengde
  * Andel vanskelige ord
  * Variasjon i ordbruk

```python
# Eksempel på bruk:
tekst1 = les_fil("tekst1.txt")
tekst2 = les_fil("tekst2.txt")

analyse1 = analyser_tekst(tekst1)
print("Lesbarhetsscore:", analyse1["lesbarhet"])
print("Mest brukte ordkombinasjoner:", analyse1["ordkombinasjoner"])

likheter = sammenlign_tekster(tekst1, tekst2)
print("Likhetsgrad:", likheter["prosent"])
print("Mulige sitater:", likheter["sitater"])
```

4. Utfordringer programmet må håndtere:
- Store tekstmengder (flere MB)
- Tekster på flere språk
- Ulike filformater
- Feilaktig formatert input
- Minneeffektiv håndtering av store datasett

