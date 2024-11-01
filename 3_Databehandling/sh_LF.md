# Korrigert løsningsforslag - Prøve i Matematikk 2P

## Oppgave 1: Prosentvis endring og vekstfaktor

### 1.1 Endring i salg og omsetning

**a) Sjokoladeplater etter tre år**
* Startantall: 50 000 plater
* Vekstfaktor: 1 + 0,20 = 1,20
* Beregning: 50 000 × 1,20³ = 86 400

Excel:
```
A1: Startantall:           50000
A2: Vekstfaktor:          1.2
A3: Antall etter 3 år:    =A1*A2^3
```

Svar: Etter tre år vil sjokoladeprodusenten selge 86 400 sjokoladeplater.

**b) Bedriftens omsetning om fire år**
* Nåværende omsetning: 2 000 000 kr
* Vekstfaktor: 1 - 0,05 = 0,95
* Beregning: 2 000 000 × 0,95⁴ = 1 629 012,50 kr

Excel:
```
A1: Nåværende omsetning:    2000000
A2: Vekstfaktor:           0.95
A3: Omsetning etter 4 år:  =A1*A2^4
```

Svar: Om fire år vil bedriftens omsetning være 1 629 012,50 kroner.

**c) Bedriftens omsetning for tre år siden**
* Nåværende omsetning: 2 000 000 kr
* Beregning: 2 000 000 ÷ 0,95³ = 2 332 701,56 kr

Excel:
```
A1: Nåværende omsetning:      2000000
A2: Vekstfaktor:             0.95
A3: Omsetning 3 år siden:    =A1/A2^3
```

Svar: For tre år siden var bedriftens omsetning 2 332 701,56 kroner.

### 1.2 Sammensatte endringer

**a) Samlet årlig endring**
* Vårfaktor: 1,08 (økning 8%)
* Høstfaktor: 0,98 (reduksjon 2%)
* Samlet vekstfaktor = 1,08 × 0,98 = 1,0584
* Prosentvis endring = (1,0584 - 1) × 100 = 5,84%

Excel:
```
A1: Vårfaktor:              1.08
A2: Høstfaktor:             0.98
A3: Samlet vekstfaktor:     =A1*A2
A4: Prosentvis endring:     =(A3-1)*100
```

Svar: Den samlede årlige endringen er en økning på 5,84%.

**b) Antall trær etter 5 år**
* Startantall: 10 000 trær
* Årlig vekstfaktor: 1,0584
* Beregning: 10 000 × 1,0584⁵ = 13 281 trær (avrundet til hele trær)

Excel:
```
A1: Startantall:           10000
A2: Vekstfaktor:          1.0584
A3: Antall etter 5 år:    =ROUND(A1*A2^5,0)
```

Svar: Etter 5 år vil det være 13 281 trær i skogen.

## Oppgave 2: Brutto- og nettoinntekt

### 2.1 Lønn

**a) Sofies månedlige nettoinntekt**
* Årslønn: 540 000 kr
* Månedslønn brutto: 540 000 ÷ 12 = 45 000 kr
* Årlig fagforeningskontingent: 500 kr
* Månedlig fagforeningskontingent: 500 ÷ 12 = 41,67 kr
* Månedlig pensjonstrekk: 45 000 × 0,02 = 900 kr
* Månedlig skattegrunnlag: 45 000 - 41,67 - 900 = 44 058,33 kr
* Månedlig skatt: 44 058,33 × 0,34 = 14 979,83 kr
* Månedlig nettoinntekt: 45 000 - 41,67 - 900 - 14 979,83 = 28 776,00 kr

Excel:
```
A1: Årslønn:                  540000
A2: Månedslønn:              =A1/12
A3: Fagforeningskontingent:   =500/12
A4: Pensjonstrekk:           =A2*0.02
A5: Skattegrunnlag:          =A2-A3-A4
A6: Skatt:                   =A5*0.34
A7: Månedlig nettoinntekt:   =A2-A3-A4-A6
```

Svar: Sofies månedlige nettoinntekt blir 28 776,00 kroner.

**b) Sofies feriepenger**
* Feriepenger = 540 000 × 0,102 = 55 080,00 kr

Excel:
```
A1: Årslønn:             540000
A2: Feriepengesats:      0.102
A3: Feriepenger:         =A1*A2
```

Svar: Sofies feriepenger blir 55 080,00 kroner.

### 2.2 Lønnsendring og skatt
* Opprinnelig nettoinntekt: 450 000 × (1 - 0,30) = 315 000,00 kr
* Ny bruttolønn: 450 000 × 1,04 = 468 000,00 kr
* Ny nettoinntekt: 468 000 × (1 - 0,31) = 322 920,00 kr
* Endring: 322 920,00 - 315 000,00 = 7 920,00 kr

Excel:
```
A1: Gammel bruttolønn:       450000
A2: Gammel skattesats:       0.30
A3: Gammel nettoinntekt:     =A1*(1-A2)
A4: Ny bruttolønn:          =A1*1.04
A5: Ny skattesats:          0.31
A6: Ny nettoinntekt:        =A4*(1-A5)
A7: Endring:                =A6-A3
```

Svar: Arbeidstakerens årlige nettoinntekt vil øke med 7 920,00 kroner.

## Oppgave 3: Lån og renter

### 3.1 Annuitetslån

**a) Forklaring annuitetslån**
Dette er et annuitetslån fordi terminbeløpet er konstant (2 387 kr) gjennom hele nedbetalingstiden.

**b) Restgjeld etter 12 måneder**

```python
lanebelop = 120000
manedsrente = 0.00599
terminbelop = 2387

restgjeld = lanebelop
sum_renter = 0
maned = 1

while maned <= 12:
    rente = restgjeld * manedsrente
    avdrag = terminbelop - rente
    restgjeld = restgjeld - avdrag
    sum_renter = sum_renter + rente
    maned = maned + 1

print(f"Restgjeld etter 12 måneder: {restgjeld:.2f} kr")
```

Svar: Etter 12 måneder vil restgjelden være 99 308,75 kroner.

**c) Totale rentekostnader**

```python
lanebelop = 120000
manedsrente = 0.00599
terminbelop = 2387

restgjeld = lanebelop
totale_renter = 0
maned = 1

while maned <= 60:
    rente = restgjeld * manedsrente
    avdrag = terminbelop - rente
    restgjeld = restgjeld - avdrag
    totale_renter = totale_renter + rente
    maned = maned + 1

print(f"Totale rentekostnader: {totale_renter:.2f} kr")
```

Svar: De totale rentekostnadene over hele låneperioden blir 23 205,76 kroner.

### 3.2 Kredittkortgjeld
* Lånebeløp: 15 000 kr
* Årlig nominell rente: 20%
* Beregning: 15 000 × ((1 + 0,20)^(6/12) - 1) = 1 431,68 kr

Excel:
```
A1: Lånebeløp:              15000
A2: Årlig rente:            0.20
A3: Antall måneder:         6
A4: Rentekostnad:          =A1*((1+A2)^(A3/12)-1)
```

Svar: Rentekostnadene etter 6 måneder vil være 1 431,68 kroner.

## Oppgave 4: Familieøkonomi og budsjett

### 4.1 Budsjettanalyse

**a) Budsjett**
* Mat og dagligvarer: 9 000 kr
* Klær og sko: 1 500 kr
* Transport og drivstoff: 2 500 kr
* Forsikringer: 1 800 kr
* Barnehage og fritidsaktiviteter: 4 000 kr
* Strøm og oppvarming: 2 500 kr
* Andre utgifter: 2 200 kr
* Fast sparing: 5 000 kr
* Sum utgifter: 28 500 kr

* Nettolønn: 80 000 kr
* Disponibelt beløp: 80 000 - 28 500 = 51 500 kr

Excel:
```
A1: Nettolønn:                  80000
A2: Mat og dagligvarer:         9000
A3: Klær og sko:               1500
A4: Transport og drivstoff:     2500
A5: Forsikringer:              1800
A6: Barnehage/fritid:          4000
A7: Strøm og oppvarming:       2500
A8: Andre utgifter:            2200
A9: Fast sparing:              5000
A10: Sum utgifter:             =SUM(A2:A9)
A11: Til disposisjon:          =A1-A10
```

Svar: Familien har 51 500 kroner til disposisjon hver måned.

**b) Reduserte utgifter**
* Mat og dagligvarer: 9 000 × 0,10 = 900,00 kr
* Klær og sko: 1 500 × 0,10 = 150,00 kr
* Andre utgifter: 2 200 × 0,10 = 220,00 kr
* Total mulig sparing: 1 270,00 kr

Excel:
```
A1: Post               B1: Beløp     C1: Reduksjon
A2: Mat/dagligvarer    B2: 9000      C2: =B2*0.1
A3: Klær og sko        B3: 1500      C3: =B3*0.1
A4: Andre utgifter     B4: 2200      C4: =B4*0.1
A5: Sum                            C5: =SUM(C2:C4)
```

Svar: Ved å redusere disse postene med 10% kan familien spare ytterligere 1 270,00 kroner per måned.

## Oppgave 5: Sparing og investering

### 5.1 Sammenligning av spareplaner

**a) Sluttverdier**

Plan A:
* Startinnskudd: 50 000 kr
* Sluttverdi = 50 000 × 1,04¹⁰ = 74 012,21 kr

Excel:
```
A1: Startinnskudd:           50000
A2: Rente:                   0.04
A3: Antall år:              10
A4: Sluttverdi:             =A1*(1+A2)^A3
```

Plan B:
* Startinnskudd: 30 000 kr
* Årlige innskudd: 5 000 kr
* Sluttverdi: 99 356,47 kr

Excel for Plan B (år for år):
```
A1: År    B1: Innskudd    C1: Saldo    D1: Rente    E1: Ny saldo
A2: 0     B2: 30000       C2: =B2      D2: =C2*0.03 E2: =C2+D2
A3: 1     B3: 5000        C3: =E2+B3   D3: =C3*0.03 E3: =C3+D3
```

**b) Renteinntekter**
Plan A: 74 012,21 - 50 000 = 24 012,21 kr
Plan B: 99 356,47 - (30 000 + 5 000 × 10) = 19 356,47 kr

Svar: Plan A gir høyest renteinntekter. Det høye startinnskuddet og den høyere renten i Plan A fører sammen med rentes-rente-effekten til at renteinntekten blir høyere enn i Plan B.