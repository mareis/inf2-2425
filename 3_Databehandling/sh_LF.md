# Løsningsforslag - Prøve i Matematikk 2P

## Oppgave 1: Prosentvis endring og vekstfaktor

### 1.1 Endring i salg og omsetning

**a) Sjokoladeplater etter tre år**

Utregning:
* Startverdi = 50 000 plater
* Vekstfaktor = 1 + 0,20 = 1,20
* Antall etter tre år = 50 000 × 1,20³

Excel:
```
Startantall:           50000
Vekstfaktor:          1.2
Antall etter 3 år:    =A1*A2^3
```

Svar: Etter tre år vil sjokoladeprodusenten selge 86 400 sjokoladeplater.

**b) Omsetning om fire år**

Utregning:
* Nåværende omsetning = 2 000 000 kr
* Vekstfaktor = 1 - 0,05 = 0,95
* Omsetning om fire år = 2 000 000 × 0,95⁴

Excel:
```
Nåværende omsetning:    2000000
Vekstfaktor:           0.95
Omsetning etter 4 år:  =A1*A2^4
```

Svar: Om fire år vil bedriftens omsetning være 1 629 000 kroner.

**c) Omsetning for tre år siden**

Utregning:
* Nåværende omsetning = 2 000 000 kr
* For å finne tidligere verdi må vi dele på vekstfaktoren tre ganger
* Omsetning for tre år siden = 2 000 000 ÷ 0,95³

Excel:
```
Nåværende omsetning:      2000000
Vekstfaktor:             0.95
Omsetning 3 år siden:    =A1/A2^3
```

Svar: For tre år siden var bedriftens omsetning 2 332 700 kroner.

### 1.2 Sammensatte endringer

**a) Samlet årlig endring**

Utregning:
* Vårøkning: 1 + 0,08 = 1,08
* Høstreduksjon: 1 - 0,02 = 0,98
* Samlet vekstfaktor = 1,08 × 0,98 = 1,0584
* Prosentvis endring = (1,0584 - 1) × 100 = 5,84

Excel:
```
Vårfaktor:              1.08
Høstfaktor:             0.98
Samlet vekstfaktor:     =A1*A2
Prosentvis endring:     =(A3-1)*100
```

Svar: Den samlede årlige endringen er en økning på 5,84 %.

**b) Antall trær etter 5 år**

Utregning:
* Startantall = 10 000 trær
* Årlig vekstfaktor = 1,0584
* Antall etter 5 år = 10 000 × 1,0584⁵

Excel:
```
Startantall:           10000
Vekstfaktor:          1.0584
Antall etter 5 år:    =A1*A2^5
```

Svar: Etter 5 år vil det være 13 277 trær i skogen.

## Oppgave 2: Brutto- og nettoinntekt

### 2.1 Lønn

**a) Sofies månedlige nettoinntekt**

Utregning:
1. Trekk før skatt:
   * Fagforeningskontingent: 500 kr
   * Pensjonstrekk: 540 000 × 0,02 = 10 800 kr
   * Sum trekk før skatt = 11 300 kr

2. Trekkgrunnlag for skatt:
   * Trekkgrunnlag = 540 000 - 11 300 = 528 700 kr
   * Skatt = 528 700 × 0,34 = 179 758 kr

3. Total beregning:
   * Bruttolønn: 540 000 kr
   * - Fagforeningskontingent: 500 kr
   * - Pensjonstrekk: 10 800 kr
   * - Skatt: 179 758 kr
   * = Årlig nettoinntekt: 348 942 kr

4. Månedlig nettoinntekt: 348 942 ÷ 12 = 29 079 kr

Excel:
```
Årslønn:                     540000
Fagforeningskontingent:      500
Pensjonstrekk:              =A1*0.02
Sum trekk før skatt:        =A2+A3
Trekkgrunnlag:              =A1-A4
Skatt:                      =A5*0.34
Årlig nettoinntekt:         =A1-A2-A3-A6
Månedlig nettoinntekt:      =A7/12
```

Svar: Sofies månedlige nettoinntekt blir 29 079 kroner.

**b) Sofies feriepenger**

Utregning:
* Årslønn = 540 000 kr
* Feriepengesats = 10,2 %
* Feriepenger = 540 000 × 0,102

Excel:
```
Årslønn:             540000
Feriepengesats:      0.102
Feriepenger:         =A1*A2
```

Svar: Sofies feriepenger blir 55 080 kroner.

### 2.2 Lønnsendring og skatt

Utregning:
1. Gammel situasjon:
   * Bruttolønn = 450 000 kr
   * Skattesats = 30 %
   * Nettoinntekt = 450 000 × (1 - 0,30) = 315 000 kr

2. Ny situasjon:
   * Ny bruttolønn = 450 000 × 1,04 = 468 000 kr
   * Ny skattesats = 31 %
   * Ny nettoinntekt = 468 000 × (1 - 0,31) = 322 920 kr

3. Endring i nettoinntekt:
   * 322 920 - 315 000 = 7 920 kr

Excel:
```
Gammel bruttolønn:        450000
Gammel skattesats:        0.30
Gammel nettoinntekt:      =A1*(1-A2)

Ny bruttolønn:           =A1*1.04
Ny skattesats:           0.31
Ny nettoinntekt:         =A4*(1-A5)

Endring:                 =A6-A3
```

Svar: Arbeidstakerens årlige nettoinntekt vil øke med 7 920 kroner.

## Oppgave 3: Lån og renter

### 3.1 Annuitetslån

**a) Forklaring annuitetslån**

Dette er et annuitetslån fordi det månedlige terminbeløpet er konstant (2 387 kr) gjennom hele nedbetalingstiden. I hver termin vil en større andel av terminbeløpet gå til avdrag og en mindre andel til renter etterhvert som lånet nedbetales.

**b) Restgjeld etter 12 måneder**

```python
lånebeløp = 120000
månedrente = 0.00599
terminbeløp = 2387

restgjeld = lånebeløp
sum_renter = 0
måned = 1

while måned <= 12:
    rente = restgjeld * månedrente
    avdrag = terminbeløp - rente
    restgjeld = restgjeld - avdrag
    sum_renter = sum_renter + rente
    måned = måned + 1

print(f"Restgjeld etter 12 måneder: {restgjeld:.0f} kr")
print(f"Betalte renter første år: {sum_renter:.0f} kr")
```

Svar: Etter 12 måneder vil restgjelden være 99 502 kroner.

**c) Totale rentekostnader**

```python
lånebeløp = 120000
månedrente = 0.00599
terminbeløp = 2387

restgjeld = lånebeløp
totale_renter = 0
måned = 1

while måned <= 60:
    rente = restgjeld * månedrente
    avdrag = terminbeløp - rente
    restgjeld = restgjeld - avdrag
    totale_renter = totale_renter + rente
    måned = måned + 1

print(f"Totale rentekostnader: {totale_renter:.0f} kr")
```

Svar: De totale rentekostnadene over hele låneperioden blir 23 220 kroner.

### 3.2 Kredittkortgjeld

Utregning:
* Lånebeløp = 15 000 kr
* Årlig nominell rente = 20 % = 0,20
* Periode = 6 måneder
* Rentekostnad = 15 000 × ((1 + 0,20)^(6/12) - 1)

Excel:
```
Lånebeløp:              15000
Årlig rente:            0.20
Antall måneder:         6
Rentekostnad:          =A1*((1+A2)^(A3/12)-1)
```

Svar: Rentekostnadene etter 6 måneder vil være 1 558 kroner.

## Oppgave 4: Familieøkonomi og budsjett

### 4.1 Budsjettanalyse

**a) Budsjett for familien**

Utregning:
1. Sum faste månedlige utgifter:
   * Mat og dagligvarer: 9 000 kr
   * Klær og sko: 1 500 kr
   * Transport og drivstoff: 2 500 kr
   * Forsikringer: 1 800 kr
   * Barnehage og fritidsaktiviteter: 4 000 kr
   * Strøm og oppvarming: 2 500 kr
   * Andre utgifter: 2 200 kr
   * Fast sparing: 5 000 kr
   * Sum utgifter: 28 500 kr

2. Disponibelt beløp:
   * Nettolønn: 80 000 kr
   * Minus utgifter: 28 500 kr
   * Til disposisjon: 51 500 kr

Excel:
```
INNTEKTER
Nettolønn:                  80000

UTGIFTER
Mat og dagligvarer:         9000
Klær og sko:               1500
Transport og drivstoff:     2500
Forsikringer:              1800
Barnehage/fritid:          4000
Strøm og oppvarming:       2500
Andre utgifter:            2200
Fast sparing:              5000
Sum utgifter:              =SUM(A4:A11)

Til disposisjon:           =A1-A12
```

Svar: Familien har 51 500 kroner til disposisjon hver måned etter at alle faste utgifter er betalt.

**b) Beregning av ekstra sparing ved reduserte utgifter**

Utregning:
* Mat og dagligvarer: 9 000 × 0,10 = 900 kr
* Klær og sko: 1 500 × 0,10 = 150 kr
* Andre utgifter: 2 200 × 0,10 = 220 kr

Excel:
```
Opprinnelig    Reduksjon     Sparing
9000           10%           =A1*B1
1500           10%           =A2*B2
2200           10%           =A3*B3
Total sparing:              =SUM(C1:C3)
```

Svar: Ved å redusere disse postene med 10 % kan familien spare ytterligere 1 270 kroner per måned.

## Oppgave 5: Sparing og investering

### 5.1 Sammenligning av spareplaner

**a) Beregning av sluttverdi**

Plan A:
* Startinnskudd: 50 000 kr
* Årlig rente: 4 %
* Ingen flere innskudd

Utregning Plan A:
* Sluttverdi = 50 000 × 1,04¹⁰

Excel:
```
Startinnskudd:           50000
Rente:                   4%
Antall år:              10
Sluttverdi:             =A1*(1+A2)^A3
```

Svar Plan A: Sluttverdien etter 10 år blir 74 012 kroner.

Plan B:

Excel:

```
A          B        C         D          E          F
1    År    Innskudd   Saldo    Rente 3%   Ny saldo   Totalt innbetalt
2    0      35000     35000     1050      36050          35000
3    1       5000     41050     1232      42282          40000
4    2       5000     47282     1418      48700          45000
5    3       5000     53700     1611      55311          50000
6    4       5000     60311     1809      62120          55000
7    5       5000     67120     2014      69134          60000
8    6       5000     74134     2224      76358          65000
9    7       5000     81358     2441      83799          70000
10   8       5000     88799     2664      91463          75000
11   9       5000     96463     2894      99357          80000
12   10      0        99357     2981      102338         80000

Formler:
B2: =30000+5000 (startinnskudd + første årlige innskudd)
C2: =B2
D2: =C2*0.03
E2: =C2+D2
F2: =B2

C3: =E2+B3 (forrige saldo + nytt innskudd)
D3: =C3*0.03
E3: =C3+D3
F3: =F2+B3
```

Svar Plan B: Sluttverdien etter 10 år blir 100 565 kroner.

**b) Analyse av renteinntekter**

Excel:
```
Plan B:
Totalt innbetalt:       80000
Sluttverdi:            102338
Renteinntekter:        =B2-B1    (22338)
```

Svar: Beregningen viser at:
* Plan A gir renteinntekter på 24 012 kroner (som før)
* Plan B gir renteinntekter på 22 338 kroner
