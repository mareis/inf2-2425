# Del 1: Objektorientert programmering (OOP)

## 1.1 Grunnleggende konsepter

1. Hvilket av de følgende prinsippene innen objektorientert programmering handler om gjenbruk av kode? Velg riktig svar:

    *   [ ] abstraksjon
    *   [ ] polymorfisme
    *   [ ] innkapsling
    *   [ ] arv
2. Hvilket av følgende alternativer beskriver best en klasse i objektorientert programmering (OOP)?

    *   [ ] En klasse er en instans av et objekt.
    *   [ ] En klasse er en funksjon som utfører en spesifikk oppgave.
    *   [ ] En klasse er en mal eller en prototype for objekter.
    *   [ ] En klasse er en metode for å lagre data.
3. Hva er hovedprinsippet bak objektorientert programmering (OOP)? Velg riktig alternativ.

    *   [ ] å lage lineære og sekvensielle programkoder
    *   [ ] å bryte ned et problem i et sett med funksjoner
    *   [ ] å representere data og funksjoner som objekter
    *   [ ] å minimere bruken av variabler

## 1.2 Klasserelasjoner

4. Hva er riktig type relasjon mellom de to klassene i objektorientert modellering (OOM)?

    *   [ ] assosiasjon
    *   [ ] generalisering
    *   [ ] komposisjon
    *   [ ] aggregering

    ```
    +------------+       +------------+
    |   Klasse A  |-------|   Klasse B  |
    +------------+       +------------+
    ```
5. Hvis en klasse B arver fra klasse A, hvilken betegnelse er mest korrekt for klasse B i forhold til klasse A i objektorientert modellering?

    *   [ ] B er en spesialisering av A.
    *   [ ] B er en assosiert klasse til A.
    *   [ ] B er en generalisering av A.
    *   [ ] B er en avhengig klasse av A.

## 1.3 Klassediagram og implementering

6. Det skal lages en applikasjon for et energisystem med en klasse som beskriver et batteri. Denne klassen skal gjøre det mulig å håndtere lading av et batteri og bruk av energi fra batteriet, samt å vise hvor mye energi som er igjen i batteriet. Nedenfor finner du et forslag til klassediagram for denne klassen.

    Merk: Datatypen float representerer desimaltall, - angir tilgangsnivå private og + angir tilgangsnivå public.

    ```
    +---------------------+
    |       Batteri      |
    +---------------------+
    | -batteriID : str    |
    | -energinivå : float |
    | -energikapasitet: float|
    +---------------------+
    | +ladOpp(energi:float): None|
    | +brukEnergi(energi:float): None|
    | +visEnerginivå(): float|
    +---------------------+
    ```

    a) Ta utgangspunkt i klassediagrammet ovenfor og implementer klassen i programmeringsspråket ditt.
    b) Implementer en egnet testprogram for å teste klassen, og identifiser to mulige feil og ett unntak.
    c) Implementer nødvendig håndtering av feilene og unntaket du identifiserte i punkt b).

# Del 2: Pseudokode og algoritmer

## 2.1 Forstå og tolke pseudokode

7. Ta utgangspunkt i følgende pseudokode:

    ```
    FUNCTION beregn(n):
        SET s TO 0
        FOR hvert tall i fra og med 1 til og med n
            IF i % 2 EQUAL TO 0
                SET s TO s + i
            ELSE
                SET s TO s - i
            ENDIF
        ENDFOR
        RETURN s
    ENDFUNCTION

    DISPLAY beregn(7)
    ```

    Hva vil vises som resultat av programmet beskrevet av pseudokoden ovenfor?

    *   [ ] 1
    *   [ ] -1
    *   [ ] -4
    *   [ ] -4
8. I pseudokoden nedenfor er h et positivt heltall. Merk: Operatoren // betyr heltallsdivisjon.

    ```
    READ h
    SET t TO h
    SET s TO 0
    SET r TO 0
    WHILE h NOT EQUAL TO 0
        SET r TO h % 10
        SET s TO s * 10 + r
        SET h TO h // 10
    ENDWHILE
    IF t EQUAL TO s
        DISPLAY True
    ELSE
        DISPLAY False
    ENDIF
    ```

    a) Forklar med egne ord algoritmen som er beskrevet av pseudokoden ovenfor. Skriv svaret ditt nedenfor.
9. ```
    SET b TO 4
    SET c TO 5
    FOR hvert heltall a fra og med 2 til og med 4
        DISPLAY c
        DECREMENT b
        SET c TO c + b
    ENDFOR
    ```

    Hva blir resultatet av programmet som er beskrevet i pseudokoden ovenfor?

    *   [ ] 1 3 6
    *   [ ] 5 8 10
    *   [ ] 3 6 9
    *   [ ] 5 8 10
10. Ta utgangspunkt i følgende pseudokode:

    ```
    SET n TO 10
    SET a[0] TO 0
    SET a[1] TO 1
    FOR hvert heltall i fra og med 2 til n
        SET a[i] TO a[i-1] + a[i-2]
    ENDFOR
    DISPLAY a[n]
    ```

    a) Hva blir resultatet av programmet som er beskrevet i pseudokoden ovenfor? Skriv svaret ditt her:

    b) Forklar algoritmen som er beskrevet i pseudokoden ovenfor. Skriv svaret ditt her:

## 2.2 Sortering og rekkefølge

11. Nedenfor ser du flere linjer med pseudokode i uordnet rekkefølge. Når linjene er sortert i riktig rekkefølge, skal de beskrive et program som vurderer temperaturverdier og viser en passende melding.

    Dette er meldingene som skal vises ved de ulike temperaturverdiene:

    *   Over 25 grader: "Det er varmt."
    *   Mellom 10 og 25 grader: "Det er mildt."
    *   Mellom 0 og 10 grader: "Det er kjølig."
    *   Under 0 grader: "Det er kaldt."

    Sorter linjene med pseudokode i riktig rekkefølge slik at resultatet viser riktige meldinger:

    ```
    [ ] DISPLAY "Det er varmt."
    [ ] DISPLAY "Det er mildt."
    [ ] DISPLAY "Det er kjølig."
    [ ] DISPLAY "Det er kaldt."
    [ ] ELSE IF temperatur GREATER THAN OR EQUAL TO 0
    [ ] ELSE
    [ ] ELSE IF temperatur GREATER THAN OR EQUAL TO 10
    [ ] ENDIF
    [ ] IF temperatur GREATER THAN 25
    ```

12. Nedenfor ser du flere linjer med pseudokode som skal skrive ut følgende resultat når linjene er sortert i riktig rekkefølge:

    ```
    -2 er negativt og partall
    -1 er negativt og oddetall
    0 er null
    1 er positivt og oddetall
    2 er positivt og partall
    ```

    Sorter linjene med pseudokode i riktig rekkefølge slik at den skriver ut resultatet som er beskrevet ovenfor. Merk: Operatoren % betyr rest ved heltallsdivisjon og kan skrives som mod eller Mod i noen programmeringsspråk.

    ```
    [ ] DISPLAY num + " er positivt og partall"
    [ ] DISPLAY num + " er positivt og oddetall"
    [ ] DISPLAY num + " er negativt og oddetall"
    [ ] DISPLAY num + " er negativt og partall"
    [ ] IF num % 2 EQUAL TO 0
    [ ] FOR hver num LESSER THAN OR EQUAL TO 2
    [ ] ELSE
    [ ] SET num to -2
    [ ] ELSE IF num EQUAL TO 0
    ```

## 2.3 Utvikling av algoritmer

13. Ta utgangspunkt i algoritmen fra punkt 8. Utvid og implementer algoritmen til et program som teller opp og viser hvor mange tresifrede tall som oppfyller IF-betingelsen fra algoritmen.
14. c) Utvid/endre algoritmen fra punkt 10 slik at den viser de ti første av tallene som er generert på denne måten og som er partall. Lag et flytskjema som representerer denne nye algoritmen.
15. Vi ønsker å lage en liten kalkulator for de fire regneoperasjonene – pluss, minus, gange og dele. Nedenfor finner du pseudokode som beskriver en del av en løsning ved hjelp av fire funksjoner:

    ```
    FUNCTION pluss(a, b)
        RETURN a + b
    ENDFUNCTION

    FUNCTION minus(a, b)
        RETURN a - b
    ENDFUNCTION

    FUNCTION gange(a, b)
        RETURN a * b
    ENDFUNCTION

    FUNCTION dele(a, b)
        RETURN a / b
    ENDFUNCTION
    ```

    a) Lag et klassediagram for en tilsvarende klasse kalt Kalkulator til bruk i en objektorientert løsning.
    b) Implementer klassen i ditt programmeringsspråk.
    c) Implementer et egnet testprogram for å teste løsningen, og identifiser mulige feil og unntak.
    d) Implementer nødvendig håndtering av mulige feil og unntak.
16. En uordnet liste (liste/array) skal sorteres i stigende rekkefølge etter følgende algoritme: Man sammenligner hvert element fra venstre til høyre i listen med neste element, og hvis elementet er større enn neste element, bytter de plass. Deretter går man videre til neste element og sammenligner på nytt frem til hele listen er gjennomgått. Dette gjentas til hele listen gjennomgås uten at det forekommer noen ombyttinger.

    Under finner du deler av pseudokoden for denne algoritmen. Her er a en liste med n elementer, og a[ i ] er elementet på plass i i listen.

    ```
    SET i TO 0
    FOR hver i LESSER THAN n – 1
        IF a[i] GREATER THAN a[i+1]
            CALL byttPlass()
        ENDIF
    ENDFOR
    ```

    Presisering: `byttPlass()` er en funksjon som bytter plass på naboelementer i listen.

    a) Hva blir innholdet i listen etter at vi har kjørt programmet representert ved pseudokoden over for listen a = [8, 5, 2, 6, 12], som har n = 5 elementer?

    *   [ ] [5, 8, 2, 6, 12]
    *   [ ] [5, 2, 6, 8, 12]
    *   [ ] [5, 2, 6, 8, 12]
    *   [ ] [2, 5, 6, 8, 12]

    b) Utvid pseudokoden slik at programmet den representerer, sorterer ferdig listen a i stigende rekkefølge etter algoritmen som er vist øverst. Forklar endringene du gjør. Obs! Du må også lage pseudokode for funksjonen `byttPlass()`.
    c) Implementer pseudokoden fra punkt b i ditt programmeringsspråk. Listen skal leses inn automatisk, og den ferdig sorterte listen skal skrives til konsollet eller vises i programmet.

## 2.4 Flytskjema

17. Et system som beregner billettprisen avhengig av kjøperens alder, bruker følgende regler for billettkategorier:

    *   Hvis brukeren er 15 år gammel eller yngre, skal brukeren få barnebillett til 30 kroner.
    *   Hvis brukeren er 16 år gammel eller eldre, skal brukeren få voksenbillett til 50 kroner.
    *   Hvis brukeren er 67 år gammel eller eldre, skal brukeren få pensjonistbillett til 35 kroner.

    Lag et flytdiagram for et program der brukeren skriver inn alderen på kjøperen og programmet regner ut og skriver ut riktig billettpris.

    Lag flytdiagrammet i et egnet program, og lever det i et allment lesbart format (f.eks. pdf) i det komprimerte arkivet som du laster opp til slutt i oppgavesettet.

# Del 3: Generell programmeringsforståelse

## 3.1 Pseudokode

18. Hvilket av følgende er **ikke** et typisk kjennetegn på pseudokode? Velg riktig alternativ.

    *   [ ] Den har uformell syntaks.
    *   [ ] Den ligner på vanlig menneskespråk.
    *   [ ] Den kan kjøres direkte på en datamaskin.
    *   [ ] Den brukes ofte i planleggingsfasen av programmering.

## 3.2 Løkker

19. Hvilken av de følgende påstandene er riktig om for- og while-løkker innen programmering? Velg riktig alternativ.

    *   [ ] en for-løkke kan bare brukes med tallsekvenser
    *   [ ] en while-løkke kjører alltid et bestemt antall ganger
    *   [ ] en for-løkke er best egnet når du vet hvor mange ganger du vil at løkken skal kjøre
    *   [ ] en while-løkke kan ikke bruke en teller for å holde rede på hvor mange ganger den har kjørt
20. Hvilke av de følgende sekvensene med pseudokode skriver ut tallene fra og med 1 til og med 5? Flere alternativer kan være riktige. Velg riktige svar.

    *   [ ] SET i TO 1
        FOR hver i LESSER OR EQUAL 5
            PRINT i
        ENDFOR
    *   [ ] SET i TO 1
        WHILE i < 6
            PRINT i
            INCREMENT i
        ENDWHILE
    *   [ ] SET i TO 0
        FOR hver i LESSER OR EQUAL 4
            PRINT i+1
        ENDFOR
    *   [ ] SET i TO 1
        WHILE i <= 5
            PRINT i
            INCREMENT i BY 2
        ENDWHILE

Lykke til med forberedelsene til prøven!
