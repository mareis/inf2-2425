# Funksjoner i Python

Dette arbeidsarket gir en grundig innføring i funksjoner i Python. Du vil lære hva funksjoner er, hvorfor vi bruker dem, hvordan de defineres og brukes, samt få nyttige tips for god programmeringspraksis. Til slutt finner du oppgaver for å teste og styrke din forståelse.

## Innhold

1. [Hva er en funksjon?](#hva-er-en-funksjon)
2. [Hvorfor bruke funksjoner?](#hvorfor-bruke-funksjoner)
3. [Definere en funksjon i Python](#definere-en-funksjon-i-python)
4. [Parametere og argumenter](#parametere-og-argumenter)
5. [Returverdier](#returverdier)
6. [Variabelscope (variabelomfang)](#variabelscope-variabelomfang)
7. [Lambda-funksjoner](#lambda-funksjoner)
8. [Dokumentasjonsstrenger (docstrings)](#dokumentasjonsstrenger-docstrings)
9. [Funksjonsanrop](#funksjonsanrop)
10. [Eksempler](#eksempler)
11. [Tips](#tips)
12. [Oppgaver](#oppgaver)

## Hva er en funksjon?

En funksjon er en gjenbrukbar kodeblokk som utfører en spesifikk oppgave. Funksjoner hjelper med å:

- **Organisere koden**: Gjør koden mer strukturert og oversiktlig.
- **Gjenbruk**: Unngå repetisjon ved å bruke samme kode flere steder.
- **Lesbarhet**: Gjør det lettere for andre (og deg selv) å forstå koden.

## Hvorfor bruke funksjoner?

Funksjoner er essensielle i programmering fordi de:

- **Forenkler komplekse problemer**: Ved å dele opp store problemer i mindre, håndterbare biter.
- **Øker kodenes modularitet**: Gjør det enklere å vedlikeholde og oppdatere koden.
- **Fremmer gjenbruk av kode**: Reduserer behovet for å skrive samme kode flere ganger.
- **Legger til rette for samarbeid**: Flere utviklere kan jobbe på forskjellige funksjoner samtidig.

## Definere en funksjon i Python

For å definere en funksjon i Python bruker du `def`-nøkkelordet, etterfulgt av:

- **Funksjonsnavn**: En identifikator som følger navngivingsreglene i Python.
- **Parenteser `()`**: Inneholder eventuelle parametere.
- **Kolon `:`**: Indikerer starten på funksjonens kropp.
- **Innrykket kodeblokk**: Koden som utgjør funksjonens logikk.

**Syntaks**:

```python
def funksjonsnavn(parametre):
    """Dokumentasjonsstreng (valgfritt)"""
    # Kodeblokk
    ...
```

**Eksempel**:

```python
def hils():
    print("Hei!")
```

## Parametere og argumenter

- **Parametere**: Variabler definert i funksjonens parenteser ved definisjon. De fungerer som plassholdere.
- **Argumenter**: Verdier som sendes til funksjonen når den kalles, og erstatter parametrene.

**Eksempel**:

```python
def hils(navn):
    print(f"Hei, {navn}!")

hils("Per")  # "Per" er argumentet som sendes til parameteren "navn"
```

## Returverdier

Funksjoner kan returnere verdier ved hjelp av `return`-nøkkelordet. Når en funksjon når `return`, avsluttes den, og den angitte verdien sendes tilbake til der funksjonen ble kalt.

**Eksempel**:

```python
def addisjon(a, b):
    return a + b

resultat = addisjon(5, 3)
print(resultat)  # Output: 8
```

**Funksjoner uten returverdi**:

Noen funksjoner utfører en oppgave uten å returnere en verdi. Disse returnerer implisitt `None`.

**Eksempel**:

```python
def si_hei():
    print("Hei!")

verdi = si_hei()  # Output: Hei!
print(verdi)      # Output: None
```

## Variabelscope (variabelomfang)

- **Lokale variabler**: Variabler definert inne i en funksjon. De er kun tilgjengelige innenfor den funksjonen.
- **Globale variabler**: Variabler definert utenfor alle funksjoner. De er tilgjengelige i hele skriptet, men må deklareres som `global` inne i en funksjon hvis du vil endre dem.

**Eksempel**:

```python
x = 10  # Global variabel

def funksjon():
    x = 5  # Lokal variabel
    print(x)

funksjon()  # Output: 5
print(x)    # Output: 10
```

## Lambda-funksjoner

Lambda-funksjoner er anonyme, kortfattede funksjoner definert med `lambda`-nøkkelordet. De brukes ofte for enkle operasjoner eller som argumenter til andre funksjoner.

**Syntaks**:

```python
lambda parametre: uttrykk
```

**Eksempel**:

```python
kvadrat = lambda x: x ** 2
print(kvadrat(5))  # Output: 25
```

## Dokumentasjonsstrenger (docstrings)

En dokumentasjonsstreng er en trippel-anførselstegn-innrammet streng som beskriver hva funksjonen gjør. Den plasseres rett under funksjonsdefinisjonen og kan hentes ved hjelp av `help(funksjonsnavn)` eller `funksjonsnavn.__doc__`.

**Eksempel**:

```python
def addisjon(a, b):
    """Returnerer summen av a og b."""
    return a + b
```

## Funksjonsanrop

For å bruke en funksjon, skriver du funksjonsnavnet etterfulgt av parenteser som inneholder eventuelle argumenter.

**Eksempel**:

```python
def hils(navn):
    print(f"Hei, {navn}!")

hils("Anna")  # Kaller funksjonen med argumentet "Anna"
```

## Eksempler

1. **Funksjon uten parametere og uten returverdi**

    ```python
    def si_hei():
        print("Hei!")

    si_hei()  # Output: Hei!
    ```

2. **Funksjon uten parametere med returverdi**

    ```python
    def hent_hilsen():
        return "Hei!"

    hilsen = hent_hilsen()
    print(hilsen)  # Output: Hei!
    ```

3. **Funksjon med parametere uten returverdi**

    ```python
    def hils(navn):
        print(f"Hei, {navn}!")

    hils("Per")  # Output: Hei, Per!
    ```

4. **Funksjon med parametere og returverdi**

    ```python
    def multipliser(a, b):
        produkt = a * b
        return produkt

    resultat = multipliser(4, 5)
    print(resultat)  # Output: 20
    ```

5. **Funksjon som arbeider med lister**

    ```python
    def finn_sum(liste):
        total = sum(liste)
        return total

    tall = [1, 2, 3, 4, 5]
    print(finn_sum(tall))  # Output: 15
    ```

6. **Funksjon som arbeider med ordbøker**

    ```python
    def skriv_telefonbok(telefonbok):
        for navn, nummer in telefonbok.items():
            print(f"{navn}: {nummer}")

    telefonbok = {"Per": "12345678", "Anna": "87654321"}
    skriv_telefonbok(telefonbok)
    # Output:
    # Per: 12345678
    # Anna: 87654321
    ```

## Tips

- **Navngiving**: Bruk beskrivende funksjonsnavn som reflekterer funksjonens oppgave.
- **Dokumentasjon**: Bruk docstrings for å forklare hva funksjonen gjør, dens parametere og returverdier.
- **Modularisering**: Del opp koden i mindre funksjoner for bedre lesbarhet og vedlikehold.
- **Testing**: Test funksjonene dine med ulike inputverdier for å sikre at de fungerer som forventet.
- **Kommentarer**: Bruk kommentarer (`#`) for å forklare kompliserte deler av koden.

## Oppgaver

Prøv å løse oppgavene på egen hånd før du ser på løsningsforslagene.

1. **Hei verden!**

    Skriv en funksjon `hei_verden()` som skriver ut “Hei, verden!” til konsollen.

2. **Generer hilsen**

    Lag en funksjon `generer_hilsen()` som returnerer strengen “God dag!”.

3. **Dobbel verdi**

    Skriv en funksjon `dobbel(tall)` som tar inn et tall og returnerer det dobbelte av tallet.

4. **Sjekk partall**

    Lag en funksjon `er_partall(tall)` som tar inn et tall og returnerer `True` hvis tallet er et partall, ellers `False`.

5. **Summen av to tall**

    Skriv en funksjon `summen(a, b)` som tar inn to tall og returnerer summen av dem.

6. **Tell antall elementer i liste**

    Lag en funksjon `tell_elementer(liste)` som returnerer antall elementer i en liste.

7. **Finn maksimum i liste**

    Skriv en funksjon `finn_maks(liste)` som finner og returnerer det største tallet i en liste.

8. **Reverser en liste**

    Lag en funksjon `reverser_liste(liste)` som tar inn en liste og returnerer en ny liste med elementene i omvendt rekkefølge.

9. **Tell vokaler i en streng**

    Skriv en funksjon `tell_vokaler(s)` som tar inn en streng og returnerer antall vokaler (`a, e, i, o, u, y, æ, ø, å`).

10. **Slå sammen to ordbøker**

    Lag en funksjon `sammenslaa_dict(dict1, dict2)` som slår sammen to ordbøker og returnerer den sammenslåtte ordboken.

11. **Generer passord**

    Skriv en funksjon `generer_passord(lengde)` som genererer et tilfeldig passord av en gitt lengde. Passordet bør inneholde en blanding av bokstaver, tall og spesialtegn.

12. **Anvend funksjon på liste**

    Lag en funksjon `anvend_på_liste(funksjon, liste)` som tar inn en funksjon og en liste, og returnerer en ny liste der funksjonen er anvendt på hvert element i listen.

13. **Implementer Quicksort**

    Skriv en rekursiv funksjon `quicksort(liste)` som sorterer en liste ved hjelp av Quicksort-algoritmen.
