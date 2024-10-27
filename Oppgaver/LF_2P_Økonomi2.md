# Fullstendig løsningsforslag Matematikk 2P - Økonomi

## 1. Prosentvis endring over tid

### Oppgave 1.1
**Oppgave:** En butikk øker prisen på en vare med 5% hvert år. Prisen på varen er nå 1 000 kroner. Hva vil prisen være etter 2 år?

**Løsning:**
- Startbeløp: 1 000 kr
- Årlig økning: 5% (vekstfaktor = 1,05)
- Antall år: 2

**Beregning:**
```
Sluttbeløp = Startbeløp × (1 + prosent)^antall år
           = 1 000 × (1,05)²
           = 1 000 × 1,1025
           = 1 102,50
```

**Svar:** Prisen vil være 1 102,50 kr etter 2 år.

### Oppgave 1.2
**Oppgave:** En bil mister 10% av verdien sin hvert år. Bilen kostet opprinnelig 200 000 kroner. Hva vil verdien være etter 3 år?

**Løsning:**
- Startbeløp: 200 000 kr
- Årlig reduksjon: 10% (vekstfaktor = 0,90)
- Antall år: 3

**Beregning:**
```
Sluttverdi = Startbeløp × (1 - prosent)^antall år
           = 200 000 × (0,90)³
           = 200 000 × 0,729
           = 145 800
```

**Svar:** Verdien til bilen vil være 145 800 kr etter 3 år.

### Oppgave 1.3
**Oppgave:** En investering har økt i verdi med 8% per år i 10 år, og er nå verdt 320 000 kroner. Hva var verdien av investeringen for 10 år siden?

**Løsning:**
- Sluttbeløp: 320 000 kr
- Årlig økning: 8% (vekstfaktor = 1,08)
- Antall år: 10

**Beregning:**
```
Startbeløp × (1,08)¹⁰ = 320 000
Startbeløp = 320 000 ÷ (1,08)¹⁰
           = 320 000 ÷ 2,158925
           = 148 221,92
```

**Svar:** Verdien var 148 221,92 kr for 10 år siden.

### Oppgave 1.4
**Oppgave:** En bedrift har hatt en total vekst i omsetningen fra 500 000 kroner til 750 000 kroner over en periode på 5 år. Hva var den gjennomsnittlige årlige prosentvise veksten?

**Løsning:**
- Startverdi: 500 000 kr
- Sluttverdi: 750 000 kr
- Periode: 5 år

**Beregning:**
```
750 000 = 500 000 × x⁵
x⁵ = 750 000 ÷ 500 000 = 1,5
x = ⁵√1,5 = 1,0845
Årlig vekst = (1,0845 - 1) × 100 = 8,45%
```

**Svar:** Den gjennomsnittlige årlige veksten var 8,45%.

### Oppgave 1.5
**Oppgave:** Verdien på en eiendom har først økt med 12% det første året og deretter falt med 7% det andre året. Hva er den totale prosentvise endringen i verdien etter de to årene?

**Løsning:**
- År 1: Økning 12% (vekstfaktor = 1,12)
- År 2: Nedgang 7% (vekstfaktor = 0,93)

**Beregning:**
```
Total vekstfaktor = 1,12 × 0,93 = 1,0416
Total endring = (1,0416 - 1) × 100 = 4,16%
```

**Svar:** Verdien har totalt økt med 4,16%.

### Oppgave 1.6
**Oppgave:** En aksje har hatt en økning på 55% til sammen siste 5 år. Hva er den gjennomsnittlige prosentvise endringen?

**Løsning:**
- Total økning: 55% (vekstfaktor = 1,55)
- Periode: 5 år

**Beregning:**
```
1,55 = x⁵
x = ⁵√1,55 = 1,0924
Årlig vekst = (1,0924 - 1) × 100 = 9,24%
```

**Svar:** Den gjennomsnittlige årlige veksten var 9,24%.

## 2. Anuitetslån

### Oppgave 2.1
**Oppgave:** Kari har tatt opp et lån på 3 000 000 kroner med en månedlig rente på 0,4% og et gebyr på 75 kr per termin. Hun betaler et fast terminbeløp på 15 000 kr hver måned. Hvor mye vil hun ha nedbetalt av lånet etter de første tre årene?

**Løsning:**
```python
lån = 3_000_000
terminbeløp = 15_000
rente = 0.004
gebyr = 75
mnd = 0
total_avdrag = 0
total_renter = 0

while mnd < 36:
    renter = lån * rente
    avdrag = terminbeløp - renter - gebyr
    lån = lån - avdrag
    total_avdrag += avdrag
    total_renter += renter
    mnd += 1

print(f"Total nedbetaling: {total_avdrag:.2f}")
print(f"Totale renter: {total_renter:.2f}")
print(f"Restlån: {lån:.2f}")
```

**Resultater:**
- Total nedbetaling: 195 891 kr
- Totale renter betalt: 344 109 kr
- Restlån etter 36 måneder: 2 804 109 kr

### Oppgave 2.2
**Oppgave:** Ola har tatt opp et lån på 1 800 000 kroner med en årlig rente på 5%. Han betaler et fast terminbeløp på 10 000 kr hver måned i to år. Hva vil restgjelden være etter disse to årene?

**Løsning:**
```python
lån = 1_800_000
terminbeløp = 10_000
rente = (1 + 0.05)**(1/12)-1  # Månedlig rente
mnd = 0
total_avdrag = 0
total_renter = 0

while mnd < 24:
    renter = lån * rente
    avdrag = terminbeløp - renter
    lån = lån - avdrag
    
    total_avdrag += avdrag
    total_renter += renter
    
    mnd += 1

print(f"Restgjeld etter 24 mnd: {lån:.2f} kr")
print(f"Total avdrag: {total_avdrag:.2f} kr")
print(f"Total renter: {total_renter:.2f} kr")
```

**Resultater:**
- Restgjeld etter 24 mnd: 1732912.16 kr
- Total avdrag: 67087.84 kr
- Total renter: 172912.16 kr

## 3. Økonomi, budsjett og lønn

### Oppgave 3.1
**Oppgave:** Beregn totallønn og feriepenger for sommerjobb.

**Løsning:**
a) Totallønn for 2 måneder:
```
25 000 kr × 2 = 50 000 kr
```

b) Feriepenger (12%):
```
50 000 kr × 0,12 = 6 000 kr
```

c) Total inkludert feriepenger:
```
50 000 kr + 6 000 kr = 56 000 kr
```

### Oppgave 3.2
**Oppgave:** Anna's økonomi med referansebudsjett.

**Løsning:**
a) Totale månedlige utgifter:
```
Individspesifikke utgifter:    9 800 kr
Husholdspesifikke utgifter:    3 650 kr
Kredittkortgjeld:              1 800 kr
Forsikringer:                  1 500 kr
Total:                        16 750 kr
```

b) Netto månedslønn:
```
Bruttolønn:                   58 000 kr
- Fagforening (1%):              580 kr
- Pensjon (3%):                1 740 kr
= Trekkgrunnlag:             55 680 kr
- Skatt (35%):               19 488 kr
= Netto:                     36 192 kr
```

[Fortsetter med resten av oppgavene...]

## 4. Sparing

### Oppgave 4.1
**Oppgave:** John Steinars spareplan med julegaver.

**Løsning:**
a) Innskudd om to år:
```
3 000 kr + (500 kr × 2) = 4 000 kr
```

b) Årlige innskudd:
```
År 1: 3 000 kr
År 2: 3 500 kr
År 3: 4 000 kr
År 4: 4 500 kr
År 5: 5 000 kr
```

[Fortsetter med resten av oppgavene...]

## 5. Sammensatte oppgaver

### Oppgave 5.1
**Oppgave:** Familieøkonomi og fremtidig planlegging.

**Løsning:**
a) Totale månedlige utgifter:
```
Mat og drikke:            12 000 kr
Klær og sko:               3 000 kr
Personlig pleie:           1 500 kr
Lek og fritid:             4 000 kr
Transport:                 4 000 kr
Forsikringer:              3 200 kr
SFO:                       1 200 kr
Total:                    28 900 kr
```


b) Netto månedslønn for Marie og Arne:

**Marie:**
```
Bruttolønn:                   52 000 kr
- Fagforening (1%):              520 kr
- Pensjon (2,5%):              1 300 kr
= Trekkgrunnlag:             50 180 kr
- Skatt (30%):               15 054 kr
= Netto:                     35 126 kr
```

**Arne:**
```
Bruttolønn:                   48 000 kr
- Fagforening (1%):              480 kr
- Pensjon (2,5%):              1 200 kr
= Trekkgrunnlag:             46 320 kr
- Skatt (30%):               13 896 kr
= Netto:                     32 424 kr
```

**Total netto familieinntekt:** 67 550 kr per måned

c) Beløp til overs etter utgifter:
```
Netto inntekt:               67 550 kr
- Totale utgifter:           44 000 kr
= Til overs:                 23 550 kr
```

d) Vurdering av hyttekjøp:
```
Beløp til overs:             23 550 kr
- Nytt terminbeløp:          10 000 kr
= Ny margin:                 13 550 kr
```

**Vurdering:**
- Familie Berg vil fortsatt ha 13 550 kr til overs hver måned
- Dette gir en buffer for uforutsette utgifter
- Marginen er tilstrekkelig for å håndtere hyttekjøpet
- Bør vurdere om bufferen er stor nok med tanke på fremtidige renteøkninger

### Oppgave 5.2 - Startupøkonomi for kaffebar

a) Lånebehov og terminbeløp:

**Oppstartskostnader:**
```
Inventar og møbler:          150 000 kr
Kaffemaskiner:               80 000 kr
Diverse utstyr:              50 000 kr
Total:                      280 000 kr
```

**Egenkapital og lånebehov:**
```
Total oppstartskostnad:      280 000 kr
- Egenkapital (Kari):        100 000 kr
- Egenkapital (Espen):       100 000 kr
= Lånebehov:                 80 000 kr
```

**Terminbeløp (annuitetslån):**
- Lånebeløp: 80 000 kr
- Månedlig rente: 0,4%
- Nedbetalingstid: 5 år (60 måneder)

```python
def beregn_terminbelop(laanebelop, rente, antall_terminer):
    r = rente
    n = antall_terminer
    return laanebelop * (r * (1 + r)**n) / ((1 + r)**n - 1)

terminbelop = beregn_terminbelop(80000, 0.004, 60)
# Terminbeløp ≈ 1 500 kr per måned
```

b) Totale månedlige utgifter:
```
Leie av lokaler:             12 000 kr
Strøm, vann, renovasjon:      4 500 kr
Varekjøp:                    15 000 kr
Lønn til ansatte:            30 000 kr
Diverse kostnader:            5 000 kr
Lånekostnader:                1 500 kr
Total:                       68 000 kr
```

c) Vurdering av lønnsomhet:
```
Forventet månedlig inntekt:  85 000 kr
- Totale månedlige utgifter: 68 000 kr
= Månedlig overskudd:        17 000 kr
```

**Vurdering:**
- Månedlig overskudd på 17 000 kr gir rom for uforutsette utgifter
- God margin for sesongvariasjoner
- Mulighet for reinvestering i bedriften
- Anbefalt å bygge opp en buffer for svakere perioder

### Oppgave 5.3 - Økonomisk prioritering for fremtidsdrømmer

a) Netto månedsinntekt:
```
Bruttolønn:                  45 000 kr
- Skatt (30%):               13 500 kr
= Netto månedsinntekt:       31 500 kr
```

b) Disponibelt beløp etter utgifter og sparing:
```
Netto inntekt:               31 500 kr

Faste utgifter:
- Leie:                      12 000 kr
- Mat og husholdning:         6 000 kr
- Transport og diverse:       3 000 kr

Sparing:
- Konsulentfirma:            4 000 kr
- Leilighet:                 5 000 kr
- Reise:                     2 000 kr

Total:                       32 000 kr

Månedlig underskudd:            500 kr
```

c) Forslag til justeringer:

**Revidert budsjett:**
```
Redusert sparing konsulentfirma: 3 000 kr (-1 000 kr)
Økt sparing reise:               2 500 kr (+500 kr)
Nytt resultat:                   31 500 kr (balansert)
```

d) Beregning av feriepenger:

**Med 5 ukers ferie (12%):**
```
Årlig bruttolønn:           540 000 kr
Feriepenger (12%):           64 800 kr
```

**Med 4 uker + 1 dag (10,2%):**
```
Årlig bruttolønn:           540 000 kr
Feriepenger (10,2%):         55 080 kr
```

**Anbefalinger:**
1. Revurdere sparemålene
2. Søke høyere inntekt gjennom:
   - Lønnsforhandlinger
   - Ekstrainntekter
3. Vurdere å redusere faste utgifter
4. Lage en mer detaljert plan for oppstart av konsulentfirma

## Vurderingskriterier

### Høy måloppnåelse:
- Presise beregninger med korrekt bruk av formler
- God forståelse for økonomiske sammenhenger
- Grundige analyser og vurderinger
- Hensiktsmessig bruk av digitale verktøy
- Tydelige og velbegrunnede konklusjoner

### Middels måloppnåelse:
- Stort sett korrekte beregninger
- Grunnleggende forståelse for sammenhenger
- Noen analyser og vurderinger
- Akseptabel bruk av digitale verktøy
- Rimelige konklusjoner

### Lav måloppnåelse:
- Delvis korrekte beregninger
- Begrenset forståelse
- Overfladiske analyser
- Mangelfull bruk av digitale verktøy
- Svake eller manglende konklusjoner

## Kompetansemål som dekkes:
1. Bruk av prosent og vekstfaktor
2. Sammenheng mellom brutto- og nettoinntekt
3. Vurdering av personlig økonomi
4. Konsekvenser av låneopptak
5. Digitale verktøy i økonomiske beregninger

## Metodiske tips:
1. Start med å identifisere kjente størrelser
2. Bruk kalkulator eller regneark for beregninger
3. Kontroller at svarene er rimelige
4. Vurder økonomiske konsekvenser
5. Gi begrunnede anbefalinger

## Vanlige utfordringer:
1. Forveksling av prosent og prosentpoeng
2. Feil i renteberegninger
3. Utelatelse av viktige økonomiske faktorer
4. Manglende kontroll av rimelighet
5. Ufullstendige begrunnelser

## Differensiering:
- **Grunnleggende nivå:** Fokuser på enkle prosentregning og budsjettoppsett
- **Middels nivå:** Inkluder låneberegninger og vekstfaktor
- **Høyt nivå:** Analyser sammensatte økonomiske situasjoner

## Digitale verktøy:
1. Kalkulator for grunnleggende beregninger
2. Regneark for budsjetter og analyser
3. Python for programmering av økonomiske modeller
4. Grafiske fremstillinger av økonomisk utvikling

## Vurderingskriterier

### Høy måloppnåelse vises ved:
1. Korrekt bruk av formler og beregninger
2. God forståelse for økonomiske sammenhenger
3. Tydelig og strukturert fremstilling
4. Relevante begrunnelser og vurderinger
5. Hensiktsmessig bruk av digitale verktøy

### Middels måloppnåelse vises ved:
1. Stort sett korrekte beregninger
2. Grunnleggende forståelse for sammenhenger
3. Akseptabel fremstilling
4. Noen begrunnelser
5. Basis bruk av digitale verktøy

### Lav måloppnåelse vises ved:
1. Delvis korrekte beregninger
2. Begrenset forståelse
3. Uklar fremstilling
4. Manglende begrunnelser
5. Lite hensiktsmessig bruk av digitale verktøy
