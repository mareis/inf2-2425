
# Oversikt over konsepter og begreper innen objektorientert programmering

Dette dokumentet gir en oversikt over sentrale konsepter og begreper innen objektorientert programmering (OOP) med utgangspunkt i kompetansemålene:

*   Utforske og vurdere alternative løsninger for design og implementering av et program.
*   Anvende objektorientert modellering til å beskrive et programs struktur.
*   Utvikle objektorienterte programmer med klasser, objekter, metoder og arv.
*   Vurdere og bruke strategier for feilsøking og testing av programkode.

## 1. Objektorientert programmering (OOP) - Grunnleggende konsepter

### 1.1 Hva er OOP?

Objektorientert programmering (OOP) er en programmeringsparadigme som baserer seg på konseptet "objekter", som inneholder data i form av felt (ofte kalt **attributter** eller **egenskaper**) og kode, i form av prosedyrer (ofte kalt **metoder**).

### 1.2 Hovedprinsipper i OOP

*   **Abstraksjon:** Skjuler kompleks implementasjonsdetaljer og viser bare nødvendig informasjon til brukeren.
*   **Innkapsling:** Holder data (attributter) og metoder som opererer på disse dataene samlet i en enhet (objekt/klasse), og beskytter dem mot utilsiktet endring.
*   **Arv:** Lar en klasse (subklasse) arve egenskaper og metoder fra en annen klasse (superklasse), noe som fremmer gjenbruk av kode.
*   **Polymorfisme:** Tillater objekter av forskjellige klasser å bli behandlet som objekter av en felles type. Dette muliggjør fleksibilitet og utvidbarhet.

### 1.3 Sentrale begreper

*   **Klasse:** En blåkopi, mal eller prototype som definerer strukturen og oppførselen til objekter.
*   **Objekt:** En instans av en klasse. Et konkret eksempel på en klasse med spesifikke verdier for attributtene.
*   **Attributt/Egenskap:** En variabel som lagrer data om et objekt. Definerer tilstanden til et objekt.
*   **Metode:** En funksjon som er knyttet til et objekt. Definerer oppførselen til et objekt.
*   **Konstruktør:** En spesiell metode som kalles automatisk når et objekt opprettes. Brukes til å initialisere objektets attributter.

## 2. Objektorientert modellering

### 2.1 Hva er objektorientert modellering?

Objektorientert modellering (OOM) er en tilnærming til å modellere et program, et system eller en forretningsprosess ved hjelp av objektorienterte konsepter. Det hjelper til med å forstå og beskrive strukturen og oppførselen til et system før det implementeres i kode.

### 2.2 Klassediagrammer

Klassediagrammer er en type UML-diagram (Unified Modeling Language) som brukes til å visualisere strukturen til et system ved å vise systemets klasser, deres attributter, metoder og relasjonene mellom dem.

**Symboler i klassediagrammer:**

*   **Klasse:** Representeres av et rektangel med tre deler: klassenavn, attributter og metoder.
*   **Attributter:** Listes i den midterste delen av klasserektangelet.
*   **Metoder:** Listes i den nederste delen av klasserektangelet.
*   **Tilgangsnivå:**
    *   `-` (minus): Private (tilgjengelig bare innenfor klassen)
    *   `+` (pluss): Public (tilgjengelig fra hvor som helst)
    *   `#` (hashtag): Protected (tilgjengelig innenfor klassen og dens subklasser)
*   **Relasjoner:**
    *   **Assosiasjon:** En generell relasjon mellom to klasser. Representeres av en heltrukket linje.
        ```
        +------------+       +------------+
        |   Klasse A  |-------|   Klasse B  |
        +------------+       +------------+
        ```
    *   **Arv (Generalisering/Spesialisering):** Viser at en klasse (subklasse) arver fra en annen klasse (superklasse). Representeres av en heltrukket linje med en åpen pil som peker fra subklassen til superklassen.
        ```
        +------------+
        |  Superklasse|
        +------------+
             ^
             |
        +------------+
        |  Subklasse |
        +------------+
        ```
    *   **Aggregering:** En "har-en"-relasjon der en klasse inneholder en annen klasse, men den inneholdte klassen kan eksistere uavhengig. Representeres av en heltrukket linje med en åpen rombe på siden av den inneholdende klassen.
    *   **Komposisjon:** En sterkere form for aggregering der den inneholdte klassen ikke kan eksistere uavhengig av den inneholdende klassen. Representeres av en heltrukket linje med en fylt rombe på siden av den inneholdende klassen.

## 3. Utvikling av objektorienterte programmer

### 3.1 Design og implementering

*   **Design:** Innebærer å planlegge strukturen til programmet ved å identifisere klasser, attributter, metoder og relasjoner. Bruk av klassediagrammer er nyttig i denne fasen.
*   **Implementering:** Innebærer å skrive kode for å realisere designet. Dette inkluderer å definere klasser, skrive metoder og opprette objekter.

### 3.2 Arv

Arv muliggjør gjenbruk av kode ved å la en subklasse arve attributter og metoder fra en superklasse. Subklassen kan deretter legge til egne attributter og metoder, eller overstyre (endre) arvede metoder.

### 3.3 Pseudokode og algoritmer

*   **Pseudokode:** En uformell beskrivelse av en algoritme, skrevet i et språk som ligner på vanlig menneskespråk. Brukes ofte i planleggingsfasen for å beskrive logikken i et program uten å måtte tenke på syntaksen til et spesifikt programmeringsspråk.
*   **Algoritme:** En trinnvis beskrivelse av hvordan et problem skal løses.
*   **Flytskjema:** En diagrammatisk representasjon av en algoritme. Bruker symboler for å representere ulike typer operasjoner og piler for å vise kontrollflyten.

## 4. Feilsøking og testing

### 4.1 Feilsøking

Feilsøking (debugging) er prosessen med å finne og rette feil (bugs) i programkoden.

**Strategier for feilsøking:**

*   **Stepping:** Kjøre koden linje for linje og observere verdiene av variabler.
*   **Breakpoints:** Stoppe programkjøringen på bestemte punkter for å undersøke programmets tilstand.
*   **Logging:** Skrive ut informasjon om programmets tilstand til en loggfil eller konsoll for å kunne følge med på hva som skjer.
*   **Kodeinspeksjon:** Gå nøye gjennom koden for å prøve å finne feil.

### 4.2 Testing

Testing er prosessen med å kjøre et program med forskjellige inndata for å verifisere at det fungerer som forventet.

**Typer av testing:**

*   **Enhetstesting:** Tester individuelle komponenter (f.eks. klasser eller metoder) i isolasjon.
*   **Integrasjonstesting:** Tester samspillet mellom forskjellige komponenter.
*   **Systemtesting:** Tester hele programmet som en helhet.
*   **Unntakshåndtering** Håndtering av uforutsette hendelser og feil

### 4.3 Test-drevet utvikling

Test-drevet utvikling (TDD) er en utviklingsmetodikk der man skriver tester *før* man skriver koden. Dette bidrar til å sikre at koden er testbar og at den oppfyller kravene.

**Rød-grønn-refaktoreringssyklus:**

1. **Rød:** Skriv en test som feiler fordi koden den tester ennå ikke er implementert.
2. **Grønn:** Skriv akkurat nok kode til at testen passerer.
3. **Refaktorer:** Forbedre koden uten å endre dens funksjonalitet.