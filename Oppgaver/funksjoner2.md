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

## Del 4: Kombinere funksjoner 

### Oppgave 4.1: Temperaturkonvertering
Lag to funksjoner:
- `celsius_til_fahrenheit(celsius)` som konverterer fra celsius til fahrenheit
- `fahrenheit_til_celsius(fahrenheit)` som konverterer fra fahrenheit til celsius

Krav:
1. Bruk formlene: 
   - °F = (°C × 9/5) + 32
   - °C = (°F - 32) × 5/9
2. Funksjonene skal returnere verdier med én desimal
3. Lag et testprogram som:
   - Konverterer 20°C til fahrenheit
   - Tar svaret og konverterer det tilbake til celsius
   - Skriver ut alle mellomresultater

### Oppgave 4.2: Kalkulator med funksjoner
Lag en kalkulator med følgende struktur:

1. Matematiske funksjoner:
```python
def add(a, b):
    """Returnerer summen av a og b"""
    return a + b

def subtract(a, b):
    """Returnerer differansen mellom a og b"""
    pass  # Din kode her

def multiply(a, b):
    """Returnerer produktet av a og b"""
    pass  # Din kode her

def divide(a, b):
    """
    Returnerer kvotienten av a og b
    Raises: ValueError hvis b er 0
    """
    pass  # Din kode her
```

2. Hjelpefunksjoner:
```python
def get_numbers():
    """
    Ber brukeren om to tall
    Returns: tuple med to float-verdier
    """
    pass  # Din kode her

def get_operation():
    """
    Ber brukeren velge operasjon (+, -, *, /)
    Returns: string med valgt operator
    """
    pass  # Din kode her

def calculate(a, b, operation):
    """
    Utfører beregningen basert på tall og operator
    Returns: Resultat av beregningen
    Raises: ValueError ved ugyldig operator
    """
    pass  # Din kode her
```

3. Hovedprogram:
```python
def main():
    """
    Hovedløkke som:
    1. Ber om tall og operator
    2. Utfører beregning
    3. Viser resultat
    4. Spør om brukeren vil fortsette
    """
    pass  # Din kode her
```

Krav:
- Alle funksjoner skal ha dokumentasjon (docstrings)
- Programmet skal håndtere feil input på en pen måte
- Brukeren skal kunne gjøre flere beregninger uten å starte programmet på nytt

### Oppgave 4.3: Databehandling med funksjoner
Lag et program som behandler karakterstatistikk med følgende funksjoner:

1. Innlesing og validering:
```python
def les_karakterer():
    """Leser inn karakterer (1-6) til listen er tom"""
    
def valider_karakter(karakter):
    """Sjekker om karakteren er gyldig (1-6)"""
```

2. Statistikkfunksjoner:
```python
def beregn_snitt(karakterer):
    """Returnerer gjennomsnittet av karakterene"""
    
def finn_beste(karakterer):
    """Returnerer høyeste karakter"""
    
def finn_dårligste(karakterer):
    """Returnerer laveste karakter"""
    
def beregn_median(karakterer):
    """Returnerer medianen av karakterene"""
```

3. Rapporteringsfunksjoner:
```python
def lag_karakterfordeling(karakterer):
    """Returnerer ordbok med antall av hver karakter"""
    
def vis_statistikk(karakterer):
    """Skriver ut all statistikk på pen måte"""
```

Krav:
- Alle funksjoner skal håndtere tomme lister
- Statistikk skal rundes til én desimal
- Programmet skal kunne behandle både små og store datasett
- Inkluder minst 3 forskjellige test-datasett

### Oppgave 4.4: Tekstanalyse
Lag følgende funksjoner for tekstanalyse:

```python
def fjern_tegnsetting(tekst):
    """Fjerner all tegnsetting fra teksten"""
    
def tell_ord(tekst):
    """Teller antall ord i teksten"""
    
def finn_lengste_ord(tekst):
    """Finner det lengste ordet"""
    
def lag_ordfrekvens(tekst):
    """Lager ordbok med ord og deres frekvens"""
```

Krav:
1. Funksjonene skal være case-insensitive
2. Håndter både norske og engelske tekster
3. Test med minst tre forskjellige tekster:
   - En kort tekst (under 50 ord)
   - En middels tekst (100-200 ord)
   - En lang tekst (over 500 ord)

### Oppgave 4.5: Tallsekvenser
Lag et program som genererer og analyserer tallsekvenser:

```python
def generer_fibonacci(n):
    """Genererer de første n fibonacci-tallene"""
    
def generer_primtall(n):
    """Genererer de første n primtallene"""
    
def er_perfekt_tall(tall):
    """Sjekker om et tall er et perfekt tall"""
    
def finn_faktorer(tall):
    """Finner alle faktorer i et tall"""
```

Krav:
1. Alle funksjoner skal være effektive for tall opp til 10000
2. Inkluder dokumentasjon med kjøretidsanalyse
3. Lag tester som verifiserer at funksjonene er korrekte

# Oppgave 4.6: Spill-kampssystem

## Introduksjon
Du skal lage et enkelt tekstbasert kampspill der spillere kan kjempe mot hverandre. Spillet skal ha et meny-system der brukeren kan opprette spillere og la dem kjempe mot hverandre.

## Systemstruktur
```
spillsystem/
    ├── spillertyper.py   (inneholder spillerdata)
    └── hovedprogram.py   (inneholder alle funksjoner og hovedmenyen)
```

### Flytdiagram over systemet
```
Start Spill
    │
    ▼
┌─────────────┐
│  Hovedmeny  │
└──────┬──────┘
       │
       ├───────────┬────────────┬───────────┐
       │           │            │           │
       ▼           ▼            ▼           ▼
   Valg 1      Valg 2       Valg 3     Valg 4
Opprett      Start Kamp    Vis         Avslutt
Spiller                    Spillere
   │              │            │
   ▼              ▼            │
Velg Type    Velg Spiller 1    │
   │              │            │
   ▼              ▼            │
Sett Navn    Velg Spiller 2    │
   │              │            │
   │              ▼            │
   │         Kjør Kamp         │
   │              │            │
   │              ▼            │
   │        Vis Resultat       │
   │              │            │
   └──────────────┴────────────┘
                 │
                 ▼
          Tilbake til Meny
```

## Grunnleggende Strukturer

### spillertyper.py
```python
# Dette er grunnegenskapene for hver spillertype
SPILLERTYPER = {
    'kriger':     {'hp': 100, 'styrke': 15, 'forsvar': 10, 'hastighet': 8},
    'magiker':    {'hp': 80,  'styrke': 20, 'forsvar': 5,  'hastighet': 10},
    'bueskytter': {'hp': 90,  'styrke': 12, 'forsvar': 7,  'hastighet': 15}
}
```

### hovedprogram.py
Du må implementere følgende hovedfunksjoner:

```python
def opprett_spiller(navn, type):
    """
    Oppretter en ny spiller
    navn: spillerens navn (str)
    type: type spiller - 'kriger', 'magiker' eller 'bueskytter' (str)
    returnerer: spiller som ordbok med alle egenskaper
    """
    # Din kode her

def utfør_angrep(angriper, forsvarer):
    """
    Håndterer ett angrep mellom to spillere
    angriper: spiller som angriper (ordbok)
    forsvarer: spiller som forsvarer seg (ordbok)
    returnerer: tekst som beskriver hva som skjedde
    """
    # Din kode her

def kjør_kamp(spiller1, spiller2):
    """
    Gjennomfører en hel kamp mellom to spillere
    spiller1, spiller2: spillerne som skal kjempe (ordbøker)
    returnerer: tekst som beskriver hele kampen
    """
    # Din kode her

def vis_spillerstatus(spiller):
    """
    Viser status for en spiller
    spiller: spilleren som skal vises (ordbok)
    returnerer: tekst med spillerens status
    """
    # Din kode her

def vis_hovedmeny():
    """
    Viser hovedmenyen og håndterer brukervalg
    """
    # Din kode her
```

## Eksempler på Brukergrensesnitt

### Hovedmeny
```
===== KAMPSPILL =====
1. Opprett ny spiller
2. Start kamp
3. Vis alle spillere
4. Avslutt
Valg > _
```

### Opprette Spiller
```
-- OPPRETT SPILLER --
Velg type:
1. Kriger
2. Magiker
3. Bueskytter
Valg > 1

Navn på spiller: Erik
Spiller opprettet!
```

### Kampforløp
```
=== KAMP START ===
Sigurd (Kriger) VS Gandalf (Magiker)

-- Runde 1 --
Gandalf angriper først! (høyere hastighet)
Gandalf angriper Sigurd for 15 skade!
Sigurd har 85 HP igjen.
Sigurd angriper Gandalf for 12 skade!
Gandalf har 68 HP igjen.

-- Status --
Sigurd: HP 85/100 [=================== ]
Gandalf: HP 68/80 [===============     ]

-- Runde 2 --
[...]

=== KAMP SLUTT ===
Gandalf vant kampen!
```

## Krav til Implementasjon
1. Spillersystem:
   - Minst 3 forskjellige spillertyper
   - Hver type skal ha unike egenskaper
   - Spillere må lagres så de kan brukes i flere kamper

2. Kampsystem:
   - Tydelig visning av hva som skjer hver runde
   - Bruk hastighet til å bestemme hvem som angriper først
   - Vis status etter hver runde
   - Avslutt når en spiller er beseiret (HP = 0)

3. Brukergrensesnitt:
   - Tydelig meny med valg
   - Enkel navigering
   - Feilhåndtering av brukerinput
   - Pen formatering av output

## Testing av Spillet
```python
def test_spillersystem():
    """Funksjon for å teste at spillet fungerer som det skal"""
    print("\nStarter testing av spillsystemet...")
    
    # Test 1: Opprette spillere
    print("\nTest 1: Oppretter spillere")
    kriger = opprett_spiller("Sigurd", "kriger")
    magiker = opprett_spiller("Gandalf", "magiker")
    
    # Sjekk verdier
    if kriger['hp'] != 100:
        print(f"Feil: Krigeren har {kriger['hp']} HP, skulle hatt 100")
    else:
        print("OK: Kriger har riktig HP")
        
    if magiker['styrke'] != 20:
        print(f"Feil: Magikeren har {magiker['styrke']} styrke, skulle hatt 20")
    else:
        print("OK: Magiker har riktig styrke")
    
    # Test 2: Kjøre kamp
    print("\nTest 2: Kjører en kamp")
    kamp_resultat = kjør_kamp(kriger, magiker)
    if len(kamp_resultat) > 0:
        print("OK: Kampen ga et resultat")
    else:
        print("Feil: Kampen ga ikke resultat")
```

## Utvidelsesmuligheter
Når grunnspillet fungerer, kan du legge til:
1. Spesialangrep for hver spillertype
2. System for å lagre kamphistorikk
3. Rangering av spillere
4. Mulighet for å forbedre spillere over tid

## Tips til Utvikling
1. Start med å få hovedmenyen til å fungere
2. Implementer én funksjon om gangen
3. Test hver funksjon grundig før du går videre
4. Bruk print() for å sjekke verdier underveis
5. Lagre spiller-data i en liste eller ordbok

## Vurderingskriterier
- Grunnleggende funksjonalitet fungerer
- Koden er ryddig og godt dokumentert
- Brukergrensesnittet er brukervennlig
- Spillet håndterer feil på en god måte
- Kampsystemet er balansert og interessant

## Ekspertoppgaver

### Ekspertoppgave 1: Effektiv primtallsfaktorisering
Lag et program som finner primtallsfaktoriseringen av store tall (opptil 1 million).

Krav:
1. Implementer minst to forskjellige algoritmer:
   - Enkel trial division
   - En mer effektiv metode (f.eks. Pollards rho)
2. Sammenlign og dokumenter kjøretiden
3. Håndter edge cases (primtall, kvadrattall, etc.)
4. Vis faktorene på standard form (f.eks. 2⁴ × 3² × 5)

### Ekspertoppgave 2: Datakompresjonsalgoritme
Implementer en enkel datakompresjonsalgoritme (f.eks. run-length encoding) med følgende krav:

1. Kompresjonfunksjoner:
```python
def komprimer(data):
    """Komprimerer input-data"""
    
def dekomprimer(komprimert_data):
    """Dekomprimerer data tilbake til original"""
    
def beregn_kompressjonsrate(original, komprimert):
    """Beregner hvor mye plass som ble spart"""
```

2. Krav:
   - Må fungere for både tekst og tallserier
   - Må håndtere alle ASCII-tegn
   - Komprimert data må være mindre enn original for repeterende mønstre
   - Må kunne rekonstruere originalen perfekt
   - Inkluder grundig testing med ulike typer input

3. Bonuspoeng:
   - Implementer flere kompresjonsalgoritmer
   - Lag system for å velge beste algoritme basert på input
   - Visualiser kompresjon/dekompresjon-prosessen



## Bonustips for alle oppgavene 🎃
- Husk å legge til dokumentasjon (docstrings) i funksjonene dine
- Test funksjonene dine grundig med forskjellige input-verdier
- Tenk på hva som kan gå galt og håndter feil på en pen måte
- Ha det gøy mens du programmerer! 👻