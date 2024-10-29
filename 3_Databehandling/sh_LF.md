[Previous solutions remain the same through 3.2...]

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
