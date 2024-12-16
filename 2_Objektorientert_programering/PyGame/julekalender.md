# Utvikle en Julekalender: En guidet oppdagelsesreise

## Del 1: Planlegging og Forståelse

### Utforsk problemet
Før vi begynner å programmere, la oss utforske hva vi skal lage. Ta fram penn og papir og prøv å svare på disse spørsmålene:

1. Tegn hvordan du vil at julekalenderen skal se ut på skjermen
2. Merk av på tegningen:
   - Hvor mange rader og kolonner trenger vi?
   - Hvor stort mellomrom vil du ha mellom lukene?
   - Hvilken informasjon må hver luke vise?

### Tenk gjennom strukturen
La oss se på et eksempel på hvordan vi kan organisere lukene:
```
   K0  K1  K2  K3  K4  K5
R0  1   2   3   4   5   6
R1  7   8   9  10  11  12
```

**Din tur:** 
- Fullfør rutenettet for alle 24 luker
- Kan du finne et mønster for hvordan luke-numrene følger rad og kolonne?
- Prøv å skrive en formel for å finne luke-nummer fra rad og kolonne

*Hint: Hvis du er i rad 1, kolonne 2, hvordan kommer du fram til luke-nummer 8?*

### Planlegge klassene
I objektorientert programmering lager vi "maler" for tingene i programmet vårt. Tenk på det som oppskrifter:

**Oppgave: Luke-oppskrift**
Tenk deg at du skal forklare for noen hvordan de skal lage én luke. Skriv ned:
1. Hvilken informasjon trenger luken? (egenskaper)
2. Hva må luken kunne gjøre? (metoder)
3. Hvordan vet luken hvor den skal plassere seg?

*Hint: Tenk på luken som en "boks" som må:*
- *Huske sitt eget nummer*
- *Vite om den er åpen eller lukket*
- *Kunne tegne seg selv*
- *Kunne sjekke om noen klikker på den*

Prøv å skrive din egen Luke-klasse med `pass` i metodene:
```python
class Luke:
    def __init__(self, ...):  # Hvilke parametre trenger vi?
        pass
    
    # Hvilke andre metoder trenger vi?
```

### Første kodestruktur
La oss begynne med å sette opp grunnstrukturen. Hvilke konstanter tror du vi trenger?

**Din tur:** Lag en liste over konstanter vi bør definere. Tenk på:
- Vindusstørrelse
- Farger
- Antall rader og kolonner
- Størrelser og marginer

*Hint: Start med disse og legg til flere du tror vi trenger:*
```python
VINDU_BREDDE = 800
VINDU_HØYDE = 600
ANTALL_RADER = ?  # Hvor mange rader trenger vi for 24 luker?
```

### Beregne luke-størrelse
En viktig del av programmet er å beregne hvor store lukene skal være. 

**Tenkeoppgave:** 
Hvis du har et vindu som er 800 piksler bredt og vil ha 6 luker i bredden med 10 pikslers mellomrom:
1. Hvor mange mellomrom trenger du totalt? (Husk kantene!)
2. Hvor mye plass er igjen til selve lukene?
3. Hvor bred blir hver luke?

*Hint:*
- Tenk først på mellomrommene: Du trenger mellomrom på begge sider og mellom hver luke
- Når du har trukket fra plassen til mellomrom, skal resten deles likt mellom lukene

Prøv å skrive formelen for LUKE_BREDDE før du går videre.

[Vi fortsetter med implementasjonen når du har tenkt gjennom disse tingene...]

## Del 2: Implementere Luke-klassen

Nå som du har planlagt Luke-klassen, la oss bygge den steg for steg.

### Steg 1: Konstruktøren
Konstruktøren (__init__) kjøres når vi lager en ny luke. 

**Din oppgave:** 
Prøv å implementere konstruktøren. Tenk på:
1. Hvilke parametre trenger den?
2. Hvilke egenskaper må hver luke ha?
3. Hvordan regner vi ut x,y posisjon fra rad og kolonne?

*Hint for x,y utregning:*
- For hver kolonne vi flytter oss, må vi:
  - Hoppe over en luke-bredde
  - Legge til en margin
- Start med å regne ut for kolonne 0, så kolonne 1
- Se om du kan finne mønsteret

Prøv selv før du ser på løsningen!


## Testing av Luke-konstruktøren

Når vi har laget konstruktøren vår, er det viktig å teste at den fungerer som forventet. 

### Utforskningsoppgave: Teste konstruktøren
La oss lage noen test-luker og se hva som skjer. I hovedløkken din, etter `vindu.fill(BAKGRUNN)`, prøv dette:

```python
test_luke1 = Luke(1, 0, 0)  # Første luke (øverste venstre hjørne)
print(f"Luke 1: x={test_luke1.x}, y={test_luke1.y}")

# Din tur: Lag flere test-luker og print deres posisjoner
```

**Din oppgave:**
1. Lag flere test-luker med forskjellige posisjoner
2. Print ut deres koordinater
3. Stemmer posisjonene med det du forventet?

*Hint: Tegn et koordinatsystem og merk av hvor du tror lukene vil havne før du printer posisjonene*

### Implementere tegning

Nå skal vi få lukene til å vises på skjermen. Før du ser på løsningen, tenk gjennom:

**Planleggingsoppgave:**
1. Hvilke steg trenger vi for å tegne en luke?
   - Hvordan velger vi fargen?
   - Hvilken form skal luken ha?
   - Hvor skal nummeret plasseres?

2. Lag en pseudokode (en oppskrift i vanlig tekst) for hvordan du ville tegnet luken:
   ```
   For å tegne luken:
   1. Hvis luken er åpen...
   2. ...
   ```

*Hint for tekstplassering:*
- Tenk på luken som et rektangel
- Hvor er midtpunktet i rektangelet?
- Hvordan kan vi plassere teksten i dette midtpunktet?

**Eksperimenteringsoppgave:**
Prøv å implementere tegn()-metoden steg for steg:
1. Først, få et rødt rektangel til å vises
2. Deretter, få det til å skifte farge basert på er_åpen
3. Til slutt, legg til nummeret

Test hvert steg før du går videre!

### Håndtere museklikk

Før vi implementerer klikk-sjekking, la oss utforske hvordan museklikk fungerer i Pygame.

**Utforskningsoppgave: Forstå museklikk**
Legg til denne koden i hovedløkken din:
```python
elif hendelse.type == pygame.MOUSEBUTTONDOWN:
    mus_x, mus_y = pygame.mouse.get_pos()
    print(f"Klikk på posisjon: ({mus_x}, {mus_y})")
```

**Din oppgave:**
1. Kjør programmet og klikk forskjellige steder
2. Noter ned noen koordinater hvor du klikker
3. Tegn disse punktene på et koordinatsystem
4. Kan du se sammenhengen mellom hvor du klikker og koordinatene?

*Tenk gjennom:*
- Hvor starter koordinatsystemet (0,0)?
- Hvilken retning går x- og y-aksene?
- Hvordan kan vi bruke denne informasjonen til å sjekke om et klikk traff en luke?

**Designoppgave: klikket_inni()**
Før du implementerer metoden, tenk gjennom:
1. Når er et punkt inni et rektangel?
2. Hvilke grenser må vi sjekke?
3. Hvordan kan vi kombinere disse sjekkene?

*Hint:*
- Et punkt er inni et rektangel hvis:
  - x-koordinaten er mellom venstre og høyre kant
  - y-koordinaten er mellom øvre og nedre kant
- Hvordan kan vi uttrykke dette matematisk?

Prøv å skrive klikk-sjekken selv før du ser på løsningen!

## Del 3: Bygge Kalender-klassen

Nå som vi har en fungerende Luke-klasse, skal vi bygge selve kalenderen. Dette er en større utfordring som krever god planlegging.

**Tankeprosess: Planlegge rutenettet**
1. Hvordan kan vi lagre alle lukene?
   - En enkel liste?
   - En liste med lister (2D)?
   - Noe annet?

2. Tegn et diagram som viser hvordan du ville organisere datastrukturen
   ```
   rutenett = [
     [Luke1, Luke2, Luke3],
     [Luke4, Luke5, Luke6],
     ...
   ]
   ```

*Hint:*
- Tenk på hvordan du vil få tak i en spesifikk luke
- Hvilken struktur gjør det enklest å tegne alle lukene?
- Hvordan håndterer vi plassene etter luke 24?


## Utforske rutenett-strukturen

Før vi bygger hele kalenderen, la oss utforske hvordan vi kan jobbe med et rutenett i Python. Vi starter med noe enkelt:

### Eksperiment 1: Lage et lite rutenett
Prøv denne koden i Python-konsollet eller et testprogram:

```python
# Et lite 2x3 rutenett med tall
rutenett = [
    [1, 2, 3],
    [4, 5, 6]
]
```

**Din utforskning:**
1. Hvordan får du tak i tallet 5? 
2. Hvordan printer du ut alle tallene i første rad?
3. Hvordan printer du ut alle tallene i andre kolonne?

*Hint: Tenk på rad og kolonne som koordinater i rutenettet*

### Eksperiment 2: Bygge rutenettet
Nå skal vi prøve å bygge rutenettet med en løkke:

**Din oppgave:**
Prøv å skrive kode som lager det samme rutenettet som over, men med en løkke:
```python
rutenett = []
tall = 1
# Din kode her
```

*Hint:*
- Start med en tom liste
- Du trenger to løkker (en for rader og en for kolonner)
- For hver nye rad, lag først en tom liste

### Forstå rutenett-oppbygging

La oss tenke gjennom hvordan vi skal bygge kalender-rutenettet:

**Tankeeksperiment:**
For et 4x6 rutenett med 24 luker:
1. Hvor mange rader trenger vi?
2. Hvor mange kolonner?
3. Hva skjer med plassene etter luke 24?
4. Hvordan vet vi når vi skal stoppe å lage luker?

*Tegn opp rutenettet og marker:*
- Hvor luke 1 skal være
- Hvor luke 24 skal være
- Hvilke plasser som skal være tomme

## Implementere Kalender-klassen

Nå er vi klare til å implementere Kalender-klassen bit for bit.

### Steg 1: Skjelettet
Start med denne strukturen og tenk gjennom hva hver metode skal gjøre:

```python
class Kalender:
    def __init__(self):
        """
        Oppretter en ny kalender.
        """
        pass
    
    def _opprett_rutenett(self):
        """
        Lager et rutenett (2D-liste) med luker.
        Returnerer: Liste av lister med Luke-objekter
        """
        pass
    
    def tegn(self, vindu):
        """
        Tegner hele kalenderen på vinduet.
        """
        pass
```

**Din oppgave:**
1. Hvilken metode bør vi implementere først?
2. Hvilken metode er mest komplisert?
3. Hvordan kan vi teste hver metode?

### Steg 2: Bygge rutenettet

La oss fokusere på _opprett_rutenett først. Tenk gjennom disse spørsmålene:

**Planlegging:**
1. Hvordan holder vi styr på hvilket luke-nummer vi er på?
2. Når skal vi stoppe å lage nye luker?
3. Hva skal vi fylle tomme plasser med?

*Hint:*
- Start med en variabel `luke_nummer = 1`
- Øk denne for hver luke vi lager
- Når luke_nummer > 24, hva da?

**Prøv selv:**
Implementer _opprett_rutenett gradvis:
1. Først, lag rutenettet med None i alle posisjoner
2. Deretter, legg til Luke-objekter for de første 24 plassene
3. Test at du får riktig antall luker

For å teste implementasjonen din, kan du legge til denne hjelpemetoden:

```python
def skriv_ut_rutenett(self):
    """
    Hjelpemetode for å se strukturen av rutenettet.
    """
    for rad in self.rutenett:
        for luke in rad:
            if luke is None:
                print("[ ]", end=" ")
            else:
                print(f"[{luke.nummer}]", end=" ")
        print()  # Ny linje for hver rad
```

**Test implementasjonen:**
```python
kalender = Kalender()
kalender.skriv_ut_rutenett()
```

Du bør se noe som ligner på:
```
[1] [2] [3] [4] [5] [6] 
[7] [8] [9] [10] [11] [12] 
...
```

### Steg 3: Implementere tegning

Nå som vi har rutenettet, skal vi implementere tegn-metoden. Tenk gjennom:

**Planlegging:**
1. Hvordan går vi gjennom alle lukene?
2. Hvordan håndterer vi None-verdier?
3. Hvordan kan vi teste at tegningen fungerer?

*Hint:*
- Bruk to løkker for å gå gjennom rutenettet
- Sjekk om luken eksisterer før du prøver å tegne den
- Test med én luke først, så hele raden, så hele kalenderen


## Utforske hendelser i Pygame

Før vi implementerer klikk-håndtering i kalenderen vår, la oss forstå hvordan hendelser fungerer i Pygame. En hendelse er noe som skjer i spillet, som et tastetrykk eller et museklikk.

### Eksperiment 1: Utforske hendelser
La oss lage et enkelt program for å se på hendelser:

```python
import pygame
pygame.init()
vindu = pygame.display.set_mode((400, 300))

kjører = True
while kjører:
    for hendelse in pygame.event.get():
        print(f"Hendelse: {hendelse}")
        if hendelse.type == pygame.QUIT:
            kjører = False

pygame.quit()
```

**Din utforskning:**
1. Kjør programmet og prøv forskjellige handlinger:
   - Klikk med venstre museknapp
   - Klikk med høyre museknapp
   - Beveg musen
   - Trykk på tastaturet
2. Observer hvilke hendelser som dukker opp i konsollen
3. Hva er forskjellen mellom MOUSEBUTTONDOWN og MOUSEBUTTONUP?

### Eksperiment 2: Musens posisjon
La oss utvide eksperimentet for å forstå museposisjoner bedre:

```python
# Legg til denne koden i hovedløkken:
if hendelse.type == pygame.MOUSEBUTTONDOWN:
    mus_x, mus_y = pygame.mouse.get_pos()
    print(f"Klikk på ({mus_x}, {mus_y})")
```

**Din oppgave:**
1. Tegn et koordinatsystem på et papir
2. Klikk på forskjellige steder i vinduet og merk av punktene på papiret
3. Kan du se et mønster i hvordan koordinatene fungerer?

*Tenk gjennom:*
- Hvor er koordinat (0, 0)?
- Hvilken retning øker x-koordinatene?
- Hvilken retning øker y-koordinatene?

## Implementere klikk-håndtering i Kalender

Nå skal vi legge til klikk-håndtering i Kalender-klassen. La oss tenke gjennom prosessen:

### Steg 1: Planlegge klikk-håndtering

**Tankeeksperiment:**
Når brukeren klikker i vinduet:
1. Hvordan finner vi ut hvilken luke som ble klikket på?
2. Må vi sjekke alle lukene?
3. Hva skal skje når en luke blir klikket?

*Hint:*
- Tenk på rutenettet som et koordinatsystem
- Hver luke har sin egen klikket_inni()-metode
- Vi må kanskje sjekke alle luker, men kan vi stoppe når vi finner den rette?

### Steg 2: Implementere håndter_klikk

Start med denne strukturen:

```python
def håndter_klikk(self, mus_x, mus_y):
    """
    Sjekker om et museklikk traff en luke og håndterer det.
    
    Args:
        mus_x: Museklikketes x-koordinat
        mus_y: Museklikketes y-koordinat
    """
    pass
```

**Din oppgave:**
1. Hvordan vil du gå gjennom rutenettet for å finne riktig luke?
2. Hva skal skje når du finner luken som ble klikket?
3. Hvordan kan du teste at funksjonen virker?

*Hint for implementasjon:*
- Du trenger to løkker for å gå gjennom rutenettet
- Husk å sjekke om det faktisk er en luke der (ikke None)
- Når du finner riktig luke, kan du endre dens tilstand

### Steg 3: Testing av klikk-håndtering

La oss teste systematisk:

```python
def test_klikk(self, x, y):
    """
    Hjelpemetode for å teste klikk-håndtering.
    """
    print(f"Tester klikk på posisjon ({x}, {y})")
    self.håndter_klikk(x, y)
    print("Etter klikk:")
    self.skriv_ut_rutenett()
```

**Test-oppgaver:**
1. Test klikk midt i første luke
2. Test klikk mellom to luker
3. Test klikk utenfor kalenderen
4. Test å åpne og lukke samme luke flere ganger

## Sette alt sammen

Nå har vi alle delene vi trenger. La oss koble alt sammen i hovedprogrammet:

### Steg 4: Oppdatere hovedløkken

**Tenk gjennom:**
1. Hvor i hovedløkken skal vi håndtere museklikk?
2. Hvordan kan vi vise at programmet reagerer på klikk?
3. Hvordan kan vi gjøre det lettere å finne feil?

*Hint:*
- Legg til print-setninger for å følge med på hva som skjer
- Test én ting om gangen
- Start med å bare tegne kalenderen, så legge til klikk-håndtering


## Systematisk feilsøking

Når vi programmerer, er det helt normalt at ting ikke fungerer på første forsøk. La oss lære hvordan vi kan finne og fikse feil på en systematisk måte.

### Forstå feilmeldinger

Når Python gir oss en feilmelding, forteller den oss egentlig tre viktige ting:
1. Hvilken type feil som oppstod
2. Hvor i koden feilen skjedde
3. Hva som førte til feilen

**Utforskningsoppgave: Tolke feilmeldinger**
Prøv å lage disse vanlige feilene med vilje og se på feilmeldingene:

```python
# 1. Skrivefeil i variabelnavn
vindu.fill(BAKGRUNN_FARGE)  # Vi skrev BAKGRUNN_FARGE istedenfor BAKGRUNN

# 2. Glemme paranteser
pygame.init

# 3. Feil innrykk
class Luke:
def __init__(self):  # Mangler innrykk
    pass
```

*Tenk gjennom:*
- Hva forteller feilmeldingen deg?
- Hvilken linje peker den på?
- Hvordan kan du bruke denne informasjonen til å fikse feilen?

### Feilsøkingsteknikker

La oss utforske noen praktiske teknikker for å finne feil:

**Teknikk 1: Print-debugging**
Dette er en enkel men effektiv måte å se hva som skjer i programmet:

```python
def håndter_klikk(self, mus_x, mus_y):
    print(f"Sjekker klikk på posisjon ({mus_x}, {mus_y})")
    for rad_index, rad in enumerate(self.rutenett):
        for kol_index, luke in enumerate(rad):
            if luke:
                print(f"Sjekker luke {luke.nummer} på posisjon ({luke.x}, {luke.y})")
                if luke.klikket_inni(mus_x, mus_y):
                    print(f"Fant treff på luke {luke.nummer}!")
```

**Din oppgave:**
1. Legg til print-setninger i din kode for å spore:
   - Når luker blir opprettet
   - Når museklikk blir registrert
   - Når en luke endrer tilstand
2. Kjør programmet og se på utskriftene
3. Ser du noe uventet?

*Hint: Print-setninger er som små vinduer inn i programmets tankegang*

**Teknikk 2: Isolere problemet**
Når noe ikke fungerer, er det lurt å teste én ting om gangen:

```python
# Test 1: Kan vi lage én luke?
test_luke = Luke(1, 0, 0)
print(f"Luke opprettet: nummer={test_luke.nummer}, posisjon=({test_luke.x}, {test_luke.y})")

# Test 2: Kan vi tegne luken?
test_luke.tegn(vindu)
pygame.display.flip()

# Test 3: Fungerer klikk-sjekk?
mus_x, mus_y = pygame.mouse.get_pos()
print(f"Klikk registrert: {test_luke.klikket_inni(mus_x, mus_y)}")
```

### Vanlige problemer og løsninger

La oss se på noen typiske utfordringer og hvordan vi kan løse dem:

**Problem 1: Lukene tegnes på feil sted**
*Utforsk:*
1. Print ut x, y for hver luke når den opprettes
2. Tegn et rutenett på papir og sammenlign med skjermen
3. Sjekk utregningen av posisjoner - husk MARGIN!

**Problem 2: Klikk registreres ikke**
*Utforsk:*
1. Er museklikk-hendelsen i hovedløkken?
2. Print museposisjonen ved hvert klikk
3. Tegn en ramme rundt hver luke for å se kollisjonsområdet

## Videreutvikling av kalenderen

Når grunnfunksjonaliteten fungerer, kan vi begynne å legge til nye funksjoner. La oss utforske noen muligheter:

### Idé 1: Tell antall åpne luker

**Tenk gjennom:**
1. Hvor skal vi lagre antall åpne luker?
2. Når må vi oppdatere tellingen?
3. Hvordan kan vi vise tallet på skjermen?

*Start med denne strukturen:*
```python
class Kalender:
    def __init__(self):
        self.rutenett = self._opprett_rutenett()
        self.antall_åpne = 0  # Ny variabel
    
    def oppdater_telling(self):
        """Teller antall åpne luker i kalenderen."""
        pass  # Din kode her
```

**Din oppgave:**
1. Implementer oppdater_telling()
2. Når bør denne metoden kalles?
3. Hvordan vil du vise tallet på skjermen?


# Videreutvikling av Julekalenderen: Nabo-interaksjon

## Utforske nabo-konseptet

La oss først utforske hva vi mener med "naboer" i et rutenett. Tenk deg rutenettet vårt som et kart, der hver luke kan ha opptil åtte naboer: over, under, til sidene og på skrå.

### Del 1: Forstå naboposisjoner

La oss se på et eksempel med luke nummer 8:
```
   7   8   9
   14  15  16
```

For luke 8 er naboene:
- Over: ingen (utenfor brettet)
- Under: 15
- Venstre: 7
- Høyre: 9
- Skrått: 14, 16 (nede til venstre og høyre)

**Utforskningsoppgave:**
1. Tegn opp en del av rutenettet og marker alle naboene til luke nummer 13
2. Hvilke spesialtilfeller må vi tenke på?
   - Luker på kanten av brettet
   - Luker i hjørnene
   - Plasser uten luke (etter nummer 24)

### Del 2: Planlegge implementasjonen

Før vi begynner å kode, la oss tenke gjennom hva vi trenger:

**Diskuter og skriv ned:**
1. Hvordan kan vi finne rad og kolonne for naboene?
   - For naboen over: (rad - 1, kolonne)
   - For naboen under: (rad + 1, kolonne)
   - For naboen til venstre: (rad, kolonne - 1)
   - Kan du finne mønsteret?

2. Hvilke sjekker må vi gjøre for hver nabo?
   - Er posisjonen innenfor rutenettet?
   - Finnes det en luke på denne posisjonen?

### Del 3: Implementere nabo-funksjonalitet

La oss begynne med å legge til en metode i Kalender-klassen for å finne naboer:

```python
def finn_naboer(self, rad, kolonne):
    """
    Finner alle gyldige naboer til en luke.
    
    Args:
        rad: Radens indeks i rutenettet
        kolonne: Kolonnens indeks i rutenettet
    
    Returns:
        Liste med Luke-objekter som er naboer
    """
    # Din kode her
    pass
```

**Din oppgave:**
1. Lag en liste med alle mulige nabo-posisjoner
2. Filtrer ut ugyldige posisjoner
3. Returner bare luker som faktisk eksisterer

*Hint for å finne nabo-posisjoner:*
```python
# Alle mulige retninger (delta_rad, delta_kolonne)
retninger = [
    (-1, -1), (-1, 0), (-1, 1),  # Over
    (0, -1),           (0, 1),    # Sidene
    (1, -1),  (1, 0),  (1, 1)     # Under
]
```

### Del 4: Teste nabo-funksjonen

La oss lage en testfunksjon for å se om nabo-logikken fungerer:

```python
def test_naboer(self):
    """Hjelpemetode for å teste nabo-funksjonaliteten."""
    for rad in range(ANTALL_RADER):
        for kol in range(ANTALL_KOLONNER):
            if self.rutenett[rad][kol]:
                luke = self.rutenett[rad][kol]
                naboer = self.finn_naboer(rad, kol)
                print(f"Luke {luke.nummer} har {len(naboer)} naboer:")
                for nabo in naboer:
                    print(f"  - Luke {nabo.nummer}")
```

### Del 5: Legge til effekter

Nå som vi kan finne naboer, kan vi legge til interessante effekter. Her er noen ideer å prøve:

**Idé 1: Åpne naboer**
```python
def håndter_klikk(self, mus_x, mus_y):
    for rad_index, rad in enumerate(self.rutenett):
        for kol_index, luke in enumerate(rad):
            if luke and luke.klikket_inni(mus_x, mus_y):
                luke.er_åpen = not luke.er_åpen
                # Finn og påvirk naboene
                naboer = self.finn_naboer(rad_index, kol_index)
                for nabo in naboer:
                    # Din kode her - hva skal skje med naboene?
                return
```

**Utfordringsoppgaver:**
1. Lett: Få alle naboer til å åpne seg når en luke åpnes
2. Medium: Få annenhver nabo til å åpne seg
3. Vanskelig: Lag en kjedereaksjon der naboene åpner seg etter tur

### Del 6: Kreative utvidelser

Når du har fått nabo-funksjonaliteten til å virke, prøv disse utvidelsene:

1. **Farge-effekter:**
   - Gi naboene en annen farge når en luke åpnes
   - La fargen gradvis gå tilbake til normal
   - Eksperimenter med forskjellige fargemønstre

2. **Animasjoner:**
   - Få naboene til å "vinke" når en luke åpnes
   - Lag en bølgeeffekt som sprer seg til naboene
   - Animer lukenes størrelse basert på naboenes tilstand

3. **Spillmekanikker:**
   - La luker bare åpnes hvis en nabo er åpen
   - Lag et "puslespill" der visse lukekombinasjoner må åpnes
   - Tell antall trekk og prøv å minimere dem

### Tips for implementasjon:

1. **Start enkelt:**
   - Få først naboene til å reagere på enklest mulig måte
   - Test grundig før du legger til mer kompleksitet
   - Print informasjon underveis for å se hva som skjer

2. **Feilsøking:**
   - Sjekk at naboer blir funnet korrekt
   - Verifiser at kanten av brettet håndteres riktig
   - Test hjørnetilfeller og luker nær slutten av kalenderen

3. **Optimalisering:**
   - Tenk på hvordan du kan gjøre koden mer effektiv
   - Unngå å sjekke samme nabo flere ganger
   - Hold koden ryddig og lesbar med gode kommentarer