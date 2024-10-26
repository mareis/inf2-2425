# Løsningeforslag

**Innholdsfortegnelse**

1. [Prosentvis endring over tid](#prosentvis-endring-over-tid)
2. [Anuitetslån](#anuitetslan)
3. [Økonomi, budsjett og lønn](#okonomi-budsjett-og-lonn)
4. [Sparing](#sparing)
5. [Sammensatte oppgaver](#sammensatte-oppgaver)

## 1 Prosentvis endring over tid <a name="prosentvis-endring-over-tid"></a>

### Oppgave 1.1

En butikk øker prisen på en vare med 5 % hvert år. Prisen på varen er nå 1 000 kroner. Hva vil prisen være etter 2 år?

**Løsning:**

- Startverdi: 1 000 kr
- Vekstfaktor: 1 + 0,05 = 1,05
- Periode: 2 år

**Input i CAS:**  
`1000 * (1.05)^2`

**Output i CAS:**  
1102.50

**Svar:**  
Prisen vil være 1 102,50 kr etter 2 år.

---

### Oppgave 1.2

En bil mister 10 % av verdien sin hvert år. Bilen kostet opprinnelig 200 000 kroner. Hva vil verdien være etter 3 år?

**Løsning:**

- Startverdi: 200 000 kr
- Vekstfaktor: 1 - 0,1 = 0,90
- Periode: 3 år

**Input i CAS:**  
`200000 * 0.90^3`

**Output i CAS:**  
145800

**Svar:**  
Verdien til bilen vil være 145 800 kr etter 3 år.

---

### Oppgave 1.3

En investering har økt i verdi med 8 % per år i 10 år, og er nå verdt 320 000 kroner. Hva var verdien av investeringen for 10 år siden?

**Løsning:**

- Sluttverdi: 320 000 kr
- Vekstfaktor: 1 + 0,08 = 1,08
- Periode: 10 år



**Input i CAS:**  
`nløs(x * 1.08^10 = 320000)`

**Output i CAS:**  
x = 148221.92

**Svar:**  
Verdien var 148 221,92 kr for 10 år siden.

---

### Oppgave 1.4

En bedrift har hatt en total vekst i omsetningen fra 500 000 kroner til 750 000 kroner over en periode på 5 år. Hva var den gjennomsnittlige årlige prosentvise veksten?

**Løsning:**

- Startverdi: 500 000 kr
- Sluttverdi: 750 000 kr
- Periode: 5 år

**Input i CAS:**  
`nløs(500000 * x^5 = 750000)`

**Output i CAS:**  
1.0845

**Svar:**  
Den gjennomsnittlige årlige vekstfaktoren er ca. 1,0845, som tilsvarer en årlig vekstrate på ca. 8,45 %.

---

### Oppgave 1.5

Verdien på en eiendom har først økt med 12 % det første året og deretter falt med 7 % det andre året. Hva er den totale prosentvise endringen i verdien etter de to årene?

**Løsning:**

- Startverdi: 100 %
- Vekstfaktorer: 1,12 og 0,93

**Input i CAS:**  
`1.12 * 0.93`

**Output i CAS:**  
1.0416

**Svar:**  
Vekstfaktor på 1,0416, som tilsvarer en økning på 4,16 %.

---

### Oppgave 1.6

En aksje har hatt en økning på 55 % til sammen siste 5 år. Hva er den gjennomsnittlige prosentvise endringen?

**Løsning:**

- Startverdi: 100 %
- Sluttverdi: 155 % (fordi en økning på 55 % gir totalt 155 % av startverdien)
- Periode: 5 år

**Input i CAS:**  
`nløs(x^5 = 1.55)`

**Output i CAS:**  
x ≈ 1.0924

**Svar:**  
Den gjennomsnittlige årlige vekstfaktoren er ca. 1,0924, som tilsvarer en gjennomsnittlig årlig prosentvis vekst på ca. 9,24 %.


## 2 Anuitetslån <a name="anuitetslan"></a>

### Oppgave 2.1
Kari har tatt opp et lån på 3 000 000 kroner med en månedlig rente på 0,4 % og et gebyr på 75 kr per termin. Her er en oversikt over lånets utvikling de første tre årene (36 måneder):

```python
lån = 3_000_000
terminbeløp = 15_000
rente = 0.4 / 100
gebyr = 75
mnd = 0

while mnd < 36:
    renter = lån * rente
    avdrag = terminbeløp - renter - gebyr
    lån = lån - avdrag
    mnd += 1
    print(f'Måned: {mnd} Restlån: {lån:.2f} Avdrag: {avdrag:.2f}')
```


### Oppgave 2.1

**Problemstilling:**

Kari har tatt opp et lån på 3 000 000 kroner med en månedlig rente på 0,4 % og et gebyr på 75 kr per termin. Hun betaler et fast terminbeløp på 15 000 kr hver måned. Hvor mye vil hun ha nedbetalt av lånet etter de første tre årene (36 måneder), og hva vil restgjelden være etter denne perioden?

**Løsning:**

- **Lånebeløp:** 3 000 000 kr
- **Månedlig rente:** 0,4 % (0,004)
- **Terminbeløp:** 15 000 kr
- **Gebyr per termin:** 75 kr
- **Antall terminer:** 36 måneder

Vi beregner lånets utvikling over 36 måneder ved å kalkulere renter, avdrag og restlån for hver måned.

**Beregninger:**

```python
lån = 3_000_000
terminbeløp = 15_000
rente = 0.004  # 0,4 % månedlig rente
gebyr = 75
mnd = 0

total_renter = 0
total_avdrag = 0

print("Måned | Renter     | Avdrag     | Restlån")
print("-------------------------------------------")

while mnd < 36:
    renter = lån * rente
    avdrag = terminbeløp - renter - gebyr
    lån = lån - avdrag
    mnd += 1
    total_renter += renter
    total_avdrag += avdrag
    print(f"{mnd:5} | {renter:10.2f} | {avdrag:10.2f} | {lån:10.2f}")
```

**Resultat:**

Etter 36 måneder har Kari betalt totalt:

- **Totale renter betalt:** ca. 344 109 kr
- **Totale avdrag betalt:** ca. 195 891 kr
- **Restlån etter 36 måneder:** ca. 2 804 109 kr

**Konklusjon:**

Etter tre år har Kari redusert lånet sitt med ca. 195 891 kr. En stor del av terminbeløpene i starten går til å betale renter, men etter hvert vil en større andel gå til avdrag. Dette viser betydningen av rentekostnader over tid ved lån.


### Oppgave 2.2

**Problemstilling:**

Ola har tatt opp et lån på 1 800 000 kroner med en årlig rente på 5 %, tilsvarende en månedlig rente på ca. 0,4167 %. Han betaler et fast terminbeløp på 10 000 kr hver måned i to år (24 måneder). Hva vil restgjelden være etter disse to årene?

**Løsning:**

- **Lånebeløp:** 1 800 000 kr
- **Månedlig rente:** 0,4167 % (0,0041667)
- **Terminbeløp:** 10 000 kr
- **Antall terminer:** 24 måneder

Vi beregner lånets utvikling over 24 måneder ved å kalkulere renter, avdrag og restlån for hver måned.

```python
lån = 1_800_000
terminbeløp = 10_000
rente = 0.05 / 12  # 0,4167 % månedlig rente
mnd = 0

total_renter = 0
total_avdrag = 0

print("Måned | Renter     | Avdrag     | Restlån")
print("-------------------------------------------")

while mnd < 24:
    renter = lån * rente
    avdrag = terminbeløp - renter
    lån = lån - avdrag
    mnd += 1
    total_renter += renter
    total_avdrag += avdrag
    print(f"{mnd:5} | {renter:10.2f} | {avdrag:10.2f} | {lån:10.2f}")
```
**Resultat:**

Etter 24 måneder har Ola betalt:

- **Totale renter betalt:** ca. 176 036 kr
- **Totale avdrag betalt:** ca. 63 964 kr
- **Restlån etter 24 måneder:** ca. 1 736 036 kr

**Konklusjon:**

Ola har etter to år redusert lånet med ca. 63 964 kr. Mye av terminbeløpene har gått til å betale renter. Han bør vurdere å øke terminbeløpet eller nedbetale ekstra for å redusere rentekostnadene over tid.

### Oppgave 2.3

**Problemstilling:**

Emma har tatt opp et lån på 2 200 000 kroner med en månedlig rente på 0,45 % og et gebyr på 100 kroner per termin. Hun betaler et fast terminbeløp på 12 500 kr per måned de første 18 månedene. Hvor mye vil restgjelden være etter disse 18 månedene, og hvor mye har hun betalt i renter og avdrag?

**Løsning:**

- **Lånebeløp:** 2 200 000 kr
- **Månedlig rente:** 0,45 % (0,0045)
- **Terminbeløp:** 12 500 kr
- **Gebyr per termin:** 100 kr
- **Antall terminer:** 18 måneder

Vi beregner lånets utvikling over 18 måneder ved å kalkulere renter, avdrag og restlån for hver måned.

```python
lån = 2_200_000
terminbeløp = 12_500
rente = 0.0045  # 0,45 % månedlig rente
gebyr = 100
mnd = 0

total_renter = 0
total_avdrag = 0

print("Måned | Renter     | Avdrag     | Restlån")
print("-------------------------------------------")

while mnd < 18:
    renter = lån * rente
    avdrag = terminbeløp - renter - gebyr
    lån = lån - avdrag
    mnd += 1
    total_renter += renter
    total_avdrag += avdrag
    print(f"{mnd:5} | {renter:10.2f} | {avdrag:10.2f} | {lån:10.2f}")
```
**Resultat:**

Etter 18 måneder har Emma betalt:

- **Totale renter betalt:** ca. 171 990 kr
- **Totale avdrag betalt:** ca. 53 510 kr
- **Restlån etter 18 måneder:** ca. 2 146 490 kr

**Konklusjon:**

Emma har etter 18 måneder redusert restgjelden til ca. 2 146 490 kr. En stor del av terminbeløpene har gått til å dekke rentekostnader og gebyrer. Hun bør vurdere om terminbeløpet bør økes for raskere nedbetaling og mindre rentebelastning over tid.


### Oppgave 2.4

**Problemstilling:**

Jonas har tatt opp et lån på 4 000 000 kroner med en månedlig rente på 0,35 % og et gebyr på 50 kroner per termin. Han betaler et fast terminbeløp på 20 000 kroner per måned. Hvor lang tid vil det ta før restlånet hans er under 3 000 000 kroner?

**Løsning:**

- **Lånebeløp:** 4 000 000 kr
- **Månedlig rente:** 0,35 % (0,0035)
- **Terminbeløp:** 20 000 kr
- **Gebyr per termin:** 50 kr

Vi beregner hvor mange måneder det vil ta før lånet er redusert til under 3 000 000 kr, ved å kalkulere renter, avdrag og restlån for hver måned.

```python
lån = 4_000_000
terminbeløp = 20_000
rente = 0.0035  # 0,35 % månedlig rente
gebyr = 50
mnd = 0

print("Måned | Renter     | Avdrag     | Restlån")
print("-------------------------------------------")

while lån >= 3_000_000:
    renter = lån * rente
    avdrag = terminbeløp - renter - gebyr
    lån = lån - avdrag
    mnd += 1
    print(f"{mnd:5} | {renter:10.2f} | {avdrag:10.2f} | {lån:10.2f}")

print(f'\nDet tar {mnd} måneder før restlånet er under 3 000 000 kroner.')
```
**Resultat:**

Etter 48 måneder (4 år) vil restlånet være under 3 000 000 kr. 

**Konklusjon:**

Jonas vil bruke 48 måneder på å redusere lånet til under 3 000 000 kr ved å betale 20 000 kr per måned. Dette gir ham en klar tidsramme for å nå sitt mål om å redusere gjelden betydelig. Dette viser viktigheten av å planlegge finansielle mål og å forstå hvordan terminbeløp, renter og lånetid påvirker total kostnad av et lån.

### Oppgave 2.5

**Problemstilling:**

Mari har tatt opp et lån på 5 000 000 kroner som skal tilbakebetales over 20 år med en månedlig rente på 0,3 % og et gebyr på 60 kroner. Hva er det månedlige terminbeløpet hun må betale hvis lånet er et annuitetslån?

**Løsning:**

- **Lånebeløp:** 5 000 000 kr
- **Månedlig rente:** 0,3 % (0,003)
- **Lånets varighet:** 20 år (240 måneder)
- **Gebyr per termin:** 60 kr

For å beregne det månedlige terminbeløpet for et annuitetslån, bruker vi formelen:

\[ M = \frac{r \cdot S}{1 - (1 + r)^{-n}} \]

hvor:
- \( M \) er det månedlige terminbeløpet
- \( r \) er den månedlige rentesatsen
- \( S \) er lånebeløpet
- \( n \) er antall terminer

```python
S = 5_000_000  # lånebeløp
r = 0.003  # månedlig rente
n = 20 * 12  # antall terminer (20 år)

M = (r * S) / (1 - (1 + r) ** -n)
terminbeløp = M + 60  # Legger til gebyr på terminbeløpet

print(f'Terminbeløpet Mari må betale hver måned er: {terminbeløp:.2f} kroner')
```
**Konklusjon:**

Dette terminbeløpet dekker både avdrag og renter for lånet, og gebyret er inkludert for å dekke administrasjonskostnadene. Med denne betalingsplanen vil Mari kunne tilbakebetale hele lånet over en periode på 20 år. Dette eksemplet viser hvordan man bruker matematiske modeller til å løse praktiske økonomiske problemstillinger, som å beregne betalinger på et annuitetslån.


## 3 Økonomi, budsjett og lønn <a name="okonomi-budsjett-og-lonn"></a>

### Oppgave 3.1: Lønn og Feriepenger

**Gitt informasjon:**
- Månedslønn: 25 000 kr
- Arbeidsperiode: 2 måneder (juli og august)
- Frikort: Ingen skatt
- Feriepengesats: 12 %

---

#### a) Hvor mye vil du tjene totalt etter 2 måneder?

Siden du tjener 25 000 kr per måned og jobber i 2 måneder:

$$
25\ 000\ \text{kr} \times 2 = 50\ 000\ \text{kr}
$$

**Totallønn etter 2 måneder:** 50 000 kr

---

#### b) I henhold til ferieloven er satsen for feriepenger 12 % av det du tjente året før (forutsett at dette er din eneste inntekt dette året). Beregn hvor mye du vil få i feriepenger året etter basert på lønnen fra denne jobben.

Feriepengene beregnes som 12 % av lønnen tjent året før. Siden totallønnen for sommerjobben var 50 000 kr:

$$
50\ 000\ \text{kr} \times 0,12 = 6\ 000\ \text{kr}
$$

**Feriepenger:** 6 000 kr

---

#### c) Hvor mye vil du totalt ha tjent inkludert feriepenger?

Summen av totallønn og feriepenger:

$$
50\ 000\ \text{kr} + 6\ 000\ \text{kr} = 56\ 000\ \text{kr}
$$

**Totalt opptjent:** 56 000 kr

---

#### d) Hva tror du kan være fordeler og ulemper med å få feriepenger året etter, sammenlignet med å få en høyere lønn med en gang?

**Fordeler:**
- Feriepenger gir en ekstra utbetaling året etter, noe som kan være nyttig som en "bonus" uten at man trenger å jobbe.
- Feriepengene beskattes ofte lavere eller ikke i det hele tatt (spesielt når de utbetales med frikort).

**Ulemper:**
- Man må vente et helt år på å få feriepengene, i stedet for å få hele lønnen med en gang.
- Hvis man trenger pengene umiddelbart, kan det føles mer nyttig å få en høyere månedslønn nå.

---


### Oppgave 3.2: Anna's økonomi
Anna vil bruke SIFO sitt referansebudsjett for å få en bedre oversikt over økonomien sin. Se nedenfor.

**Person: Kvinne 30 til 50 år.**

| Individspesifikke utgifter | Kostnad (kr) |
| -------------------------- | ------------ |
| Mat og drikke              | 5 300        |
| Klær og sko                | 1 200        |
| Personlig pleie            | 900          |
| Lek og mediebruk           | 1 400        |
| Reise (kollektivt)         | 1 000        |
| **Sum**                    | **9 800**    |

| Husholdspesifikke utgifter | Kostnad (kr) |
| -------------------------- | ------------ |
| Andre dagligvarer          | 450          |
| Husholdningsartikler       | 600          |
| Møbler                     | 700          |
| Mediebruk og fritid        | 1 900        |
| **Sum**                    | **3 650**    |

I tillegg til utgiftene som er representert i dette budsjettet, bruker Anna 1 800 kroner per måned til nedbetaling av kredittkortgjeld og 1 500 kroner per måned til forsikringer.

Anna har en brutto månedslønn på 58 000 kroner. Hun betaler 1 % av brutto månedslønn i fagforeningskontingent og 3 % til pensjonssparing. Hun har et skattetrekk på 35 %.

---

#### a) Regn ut Annas totale månedlige utgifter basert på referansebudsjettet og de ekstra utgiftene hennes.

**Individspesifikke utgifter:**
- Sum: 9 800 kr

**Husholdspesifikke utgifter:**
- Sum: 3 650 kr

**Ekstra utgifter:**
- Nedbetaling av kredittkortgjeld: 1 800 kr
- Forsikringer: 1 500 kr

**Totale månedlige utgifter:**


$$9\ 800 + 3\ 650 + 1\ 800 + 1\ 500 = 16\ 750\ \text{kr}$$

**Totale månedlige utgifter:** 16 750 kr

---


#### b) Hvor mye netto (etter skatt) sitter Anna igjen med av månedslønnen sin?

| **Beskrivelse**             | **Beløp (kr)**      |
|-----------------------------|---------------------|
| Bruttolønn                  | 58 000              |
| Fagforeningskontingent (1 %) | -580               |
| Pensjonssparing (3 %)       | -1 740               |
| **Trekkgrunnlag**          | 55 680              |
| Skatt (35 %)                | 19 488              |
| **Netto månedslønn**       | 36 192              |

---

**Netto månedslønn:** 36 192 kr

---

### c) Regn ut hvor mye Anna sitter igjen med etter å ha dekket alle utgiftene.

**Sitte igjen etter utgifter:**
$$36\ 192 - 16\ 750 = 19\ 442\ \text{kr}$$

**Beløp etter utgifter:** 19 442 kr

---

#### d) Vurder om Anna har råd til å kjøpe en hytte til 3 500 000 kroner, gitt at hun må betale 15 000 kroner i månedlige lånekostnader.

**Månedlig disponibel inntekt etter utgifter:**
- 19 442 kr

**Månedlige lånekostnader:**
- 15 000 kr

**Disponibel inntekt etter lånekostnader:**
$$19\ 442 - 15\ 000 = 4\ 442\ \text{kr}$$

**Vurdering:**
Anna har 4 442 kr igjen etter å ha betalt lånekostnadene, noe som kan være tilstrekkelig for hennes øvrige utgifter. Dette indikerer at hun kan ha råd til å kjøpe hytten, men hun bør vurdere om hun har nok til å dekke andre faste utgifter og eventuelle uforutsette kostnader.

---

## **4 Sparing** <a name="sparing"></a>

### Oppgave 4.1

Det er andre nyttårsdag, og John Steinar fikk 3 000 kroner i julegave som han vil sette inn på en ny sparekonto. John Steinar får vanligvis penger fra flere slektninger til jul. Han tror han kan sette inn penger fra julegaver i 5 år til, fram til han er ferdig med videregående skole.

For å finne ut hvor mye han vil ha på kontoen om 5 år, regner han med at han vil få omtrent 500 kroner mer i julegave hvert år. Han har en sparekonto som gir 4 prosent rente hvert år.

---

#### a) Regn ut hvor mye John Steinar vil sette inn om to år, basert på den årlige økningen i julegaven.

**Startbeløp:** 3 000 kr

**Årlig økning i julegave:** 500 kr

**Innskudd de neste årene:**
- År 1: 3 000 kr
- År 2 : 3 000 + 500 = 3 500 kr

**Innskudd etter 2 år:** 3 500 kr

---

#### b) Lag et regneark som viser hvor mye John Steinar setter inn hvert år fra nå og de neste 5 årene.

| **År** | **Innskudd (kr)** |
|--------|-------------------|
| 1      | 3 000             |
| 2      | 3 500             |
| 3      | 4 000             |
| 4      | 4 500             |
| 5      | 5 000             |

---

#### c) Fullfør regnearket med en spareplan som viser både innskudd, renter og totalsaldo etter hvert år. Lag et diagram som viser utviklingen i sparepengene, og regn ut forskjellen mellom det totale beløpet han har satt inn og hvor mye han har på kontoen etter 5 år. Altså hvor mye som er renter.

**Spareplan:**

##### Gitt Informasjon:
- **Startinnskudd:** 3 000 kr (andre nyttårsdag)
- **Årlig økning i julegave:** 500 kr
- **Årlig rente:** 4 % (0,04)
- **Spareperiode:** 5 år

##### Beregninger per År:

| **År** | **Innskudd (kr)** | **Renter (kr)** | **Totalsaldo (kr)** |
|--------|-------------------|------------------|----------------------|
| 1      | 3 000             | 120.00           | 3 120.00             |
| 2      | 3 500             | 264.80           | 6 384.80             |
| 3      | 4 000             | 535.39           | 11 920.19            |
| 4      | 4 500             | 476.81           | 16 452.99            |
| 5      | 5 000             | 679.92           | 22 311.12            |


**Totalt innskudd etter 5 år:**

$$3\ 000 + 3\ 500 + 4\ 000 + 4\ 500 + 5\ 000 = 20\ 000\ \text{kr}$$

**Beløp på kontoen etter 5 år:** 22 623.78 kr

**Renter:**
$$22\ 623.78 - 20\ 000 = 2\ 623.78\ \text{kr}$$

---

#### d) Lag en sammenligning i regnearket for å se hvordan spareplanen utvikler seg med forskjellige renter og julegavebeløp. Se på hvordan spareplanen utvikler seg hvis renten eller økningen i julegaven er annerledes (for eksempel 5 % rente og 300 kroner økning i året).

**Alternativ spareplan:**

| **År** | **Innskudd (kr)** | **Renter (5%)** | **Totalsaldo (kr)** |
|--------|-------------------|------------------|----------------------|
| 1      | 3 000             | 150              | 3 150                |
| 2      | 3 300             | 207.5            | 6 657.5              |
| 3      | 3 600             | 276.88           | 10 534.38            |
| 4      | 3 900             | 358.66           | 14 793.04            |
| 5      | 4 200             | 453.36           | 19 446.40            |

---

#### e) Lag spareplanen i Python. Lag et program som regner ut hvor mye John Steinar setter inn hvert år, hvor mye renter han får, og hvor mye han har på kontoen etter hvert år i 5 år.

```python
# Definer variabler
start_innskudd = 3000        # Startinnskudd i første år
økning_julegave = 500        # Årlig økning i julegave
rente = 0.04                  # Årlig rente (4%)
år = 5                        # Antall år

# Startsaldo
saldo = 0

# Innskudd for første år
innskudd = start_innskudd

# Skriv ut overskrifter for utskrift
print("År | Innskudd (kr) | Renter (kr) | Saldo (kr)")
print("---------------------------------------------")

# Regn ut innskudd, renter og saldo for hvert år
for i in range(1, år + 1):
    saldo += innskudd                     # Legg til innskuddet til saldoen
    rente_beløp = saldo * rente            # Beregn renter på saldoen
    saldo += rente_beløp                   # Legg til renter til saldoen

    # Skriv ut resultatene for hvert år
    print(f"{i}  | {innskudd:<13} | {rente_beløp:<11.2f} | {saldo:.2f}")

    # Oppdater innskuddet for neste år
    innskudd += økning_julegave
```

År | Innskudd (kr) | Renter (kr) | Saldo (kr)
---|---------------|-------------|----------
1  | 3000          | 120.00      | 3120.00
2  | 3500          | 264.80      | 6884.80
3  | 4000          | 435.39      | 11320.19
4  | 4500          | 632.81      | 16452.99
5  | 5000          | 858.12      | 22311.12


Forklaring

##### 1. Definer Variabler:
- **start_innskudd:** Hvor mye John setter inn det første året (3 000 kr).
- **økning_julegave:** Hvor mye julegaven øker hvert år (500 kr).
- **rente:** Årlig rente på sparekontoen (4 %, eller 0,04).
- **år:** Hvor mange år spareplanen skal kjøres (5 år).

##### 2. Initialisering:
- **saldo:** Starter på 0 kr. Dette vil holde oversikt over pengene på kontoen.
- **innskudd:** Setter innskuddet for det første året til `start_innskudd` (3 000 kr).

##### 3. Utskrift av Overskrifter:
- Skriver ut kolonneoverskriftene for å vise år, innskudd, renter og saldo.

#### 4. For-Løkke for Beregninger:
- Looper gjennom hvert år (1 til 5):
  - **Legg til Innskudd:** Øker saldo med innskudd.
  - **Beregn Renter:** Beregner renter som `saldo * rente`.
  - **Legg til Renter:** Øker saldo med de beregnede rentene.
  - **Skriv ut Resultater:** Viser året, innskuddet, rentene og den nye saldoen.
  - **Oppdater Innskudd:** Øker innskudd med `økning_julegave` for neste år.


  
  
## 5 Sammensatte oppgaver <a name="sammensatte-oppgaver"></a>

### Oppgave 5.1: Familieøkonomi og fremtidig planlegging

Familien Berg skal planlegge sin økonomi for det neste året. Familien består av to voksne, Marie og Arne, begge 40 år, og barna deres, Ida (8 år) og Lars (13 år). Se utgiftene nedenfor.

| **Utgifter**                           | **Kostnad (kr) per måned** |
| -------------------------------------- | -------------------------- |
| Mat og drikke                          | 12 000                     |
| Klær og sko                            | 3 000                      |
| Personlig pleie                        | 1 500                      |
| Lek og fritidsaktiviteter              | 4 000                      |
| Transport (kollektivt)                 | 1 500                      |
| Bilkostnader                           | 2 500                      |
| Forsikringer                           | 3 200                      |
| Barnehage og skolefritidsordning (SFO) | 1 200                      |

Marie og Arne tjener henholdsvis 52 000 og 48 000 kroner brutto per måned. Begge betaler 1 % i fagforeningskontingent, og de setter av 2,5 % av inntekten til pensjonssparing. Familien har også et boliglån på 3 000 000 kroner med månedlige terminbeløp på 15 000 kroner og et administrasjonsgebyr på 100 kroner per termin. De betaler 30 % skatt hver.

---

#### a) Regn ut familiens totale månedlige utgifter.

##### Gitt Utgifter:

| **Utgifter**                           | **Kostnad (kr) per måned** |
| -------------------------------------- | -------------------------- |
| Mat og drikke                          | 12 000                     |
| Klær og sko                            | 3 000                      |
| Personlig pleie                        | 1 500                      |
| Lek og fritidsaktiviteter              | 4 000                      |
| Transport (kollektivt)                 | 1 500                      |
| Bilkostnader                           | 2 500                      |
| Forsikringer                           | 3 200                      |
| Barnehage og skolefritidsordning (SFO) | 1 200                      |
| **Sum daglige utgifter**               | **28 900 kr**              |
| Boliglån (terminbeløp)                 | 15 000                     |
| Administrasjonsgebyr                   | 100                        |
| **Totale utgifter per måned**          | **44 000 kr**              |

##### Beregning:

$$
\begin{align*}
\text{Totale utgifter} &= \text{Daglige utgifter} + \text{Boliglån} + \text{Administrasjonsgebyr} \\
&= 28\,900 + 15\,000 + 100 \\
&= 44\,000\ \text{kr}
\end{align*}
$$

**Totale månedlige utgifter:** **44 000 kr**

---

#### b) Beregn netto månedsinntekt etter skatt, fagforeningskontingent og pensjonssparing for Marie og Arne.

##### Gitt Inntekt og Fradrag:

| **Person** | **Brutto månedslønn (kr)** | **Fagforeningskontingent (1%)** | **Pensjonssparing (2,5%)** | **Trekkgrunnlag (kr)** | **Skatt (30%)** | **Netto Inntekt (kr)** |
|------------|---------------------------|-------------------------------|---------------------------|----------------------|----------------|-----------------------|
| Marie      | 52 000                    | 520                           | 1 300                     | 50 180               | 15 054         | 35 126                |
| Arne       | 48 000                    | 480                           | 1 200                     | 46 320               | 13 896         | 32 424                |
| **Totalt** | **100 000 kr**            | **1 000 kr**                  | **2 500 kr**              | **96 500 kr**        | **28 950 kr**  | **67 550 kr**         |

##### Beregning av Skatt:

Skatt beregnes på **trekkgrunnlag**, som er inntekt etter fagforeningskontingent og pensjonssparing.

$$
\text{Trekkgrunnlag} = \text{Brutto inntekt} - \text{Fagforeningskontingent} - \text{Pensjonssparing}
$$

###### For Marie:

$$
\begin{align*}
\text{Trekkgrunnlag (Marie)} &= 52\,000 - 520 - 1\,300 \\
&= 50\,180\ \text{kr} \\
\text{Skatt (Marie)} &= 50\,180 \times 0.30 = 15\,054\ \text{kr}
\end{align*}
$$

##### For Arne:

$$
\begin{align*}
\text{Trekkgrunnlag (Arne)} &= 48\,000 - 480 - 1\,200 \\
&= 46\,320\ \text{kr} \\
\text{Skatt (Arne)} &= 46\,320 \times 0.30 = 13\,896\ \text{kr}
\end{align*}
$$

##### Netto Inntekt:

$$
\text{Netto Inntekt} = \text{Brutto inntekt} - \text{Fagforeningskontingent} - \text{Pensjonssparing} - \text{Skatt}
$$

#### For Marie:

$$
\begin{align*}
\text{Netto Inntekt (Marie)} &= 52\,000 - 520 - 1\,300 - 15\,054 \\
&= 35\,126\ \text{kr}
\end{align*}
$$

##### For Arne:

$$
\begin{align*}
\text{Netto Inntekt (Arne)} &= 48\,000 - 480 - 1\,200 - 13\,896 \\
&= 32\,424\ \text{kr}
\end{align*}
$$

#### Oppsummering:

| **Person** | **Brutto Inntekt (kr)** | **Fagforeningskontingent (kr)** | **Pensjonssparing (kr)** | **Trekkgrunnlag (kr)** | **Skatt (kr)** | **Netto Inntekt (kr)** |
|------------|---------------------------|-------------------------------|---------------------------|----------------------|----------------|-----------------------|
| Marie      | 52 000                    | 520                           | 1 300                     | 50 180               | 15 054         | 35 126                |
| Arne       | 48 000                    | 480                           | 1 200                     | 46 320               | 13 896         | 32 424                |
| **Totalt** | **100 000 kr**            | **1 000 kr**                  | **2 500 kr**              | **96 500 kr**        | **28 950 kr**  | **67 550 kr**         |

---

#### c) Hvor mye har familien til overs etter å ha betalt alle utgiftene sine?

##### Beregning:

$$
\begin{align*}
\text{Total Netto Inntekt} &= 35\,126 + 32\,424 = 67\,550\ \text{kr} \\
\text{Totale Utgifter} &= 44\,000\ \text{kr} \\
\text{Til Overs} &= 67\,550 - 44\,000 = 23\,550\ \text{kr}
\end{align*}
$$

**Familien har 23 550 kr til overs per måned etter å ha betalt alle utgifter.**

---

## d) Familien vurderer å ta opp et nytt lån for å kjøpe en hytte til 2 500 000 kroner. Beregn hvor mye de har til rådighet hver måned etter å ha betalt et anslått terminbeløp på 10 000 kroner. Kan familien ta opp lånet uten å få et for stramt budsjett?

##### Gitt Nytt Lån:

- **Hyttepris:** 2 500 000 kr
- **Terminbeløp:** 10 000 kr per måned

##### Beregning:

$$
\begin{align*}
\text{Til Overs uten nytt lån} &= 23\,550\ \text{kr} \\
\text{Til Overs med nytt lån} &= 23\,550 - 10\,000 = 13\,550\ \text{kr}
\end{align*}
$$


##### Oppsummering av Familie Bergs Økonomi:

| **Kategori**                   | **Beløp (kr)**       |
|--------------------------------|----------------------|
| **Total Netto Inntekt**        | 67 550               |
| **Totale Utgifter**            | 44 000               |
| **Til Overs uten nytt lån**    | 23 550               |
| **Nytt Terminbeløp (hytte)**   | 10 000               |
| **Til Overs med nytt lån**     | 13 550               |

---

### Konklusjon

Etter å ha inkludert boliglånsutgiftene i de totale månedlige utgiftene, ser vi at familien har 23 550 kr til overs per måned. Med det nye hyttekjøpet og et ekstra terminbeløp på 10 000 kr, reduseres dette beløpet til 13 550 kr. Dette gir familien mindre økonomisk fleksibilitet.

Familien bør vurdere:

- Om 13 550 kr per måned er nok til å dekke uforutsette utgifter, ekstra sparing, og eventuelle prisøkninger.
- Om de føler seg komfortable med et strammere budsjett.
- Muligheten for å justere andre utgifter eller øke inntektene for å få større økonomisk handlingsrom.

---

# Anbefalinger

1. **Lag et detaljert budsjett:** Gå gjennom alle utgifter og inntekter for å se hvor det er mulig å spare eller kutte kostnader.
2. **Vurder risiko:** Ta hensyn til potensielle renteøkninger som kan øke terminbeløpene på lånene.
3. **Opprett en bufferkonto:** Sørg for å ha en nødfond som dekker minst 3-6 måneders utgifter.
4. **Snakk med en finansrådgiver:** Få profesjonell veiledning for å vurdere økonomien i hyttekjøpet.

---

### Oppgave 5.2: Startupøkonomi for kaffebar

Kari og Espen planlegger å starte en kaffebar i hjembyen sin. For å gjøre dette trenger de å ha kontroll på både oppstartskostnader og forventede månedlige utgifter. Se informasjonen nedenfor:

- **Oppstartskostnader:**
  - Inventar og møbler: 150 000 kr
  - Kaffemaskiner: 80 000 kr
  - Diverse utstyr: 50 000 kr
- **Startkapital:**
  - Kari og Espen har spart opp 100 000 kroner hver, totalt 200 000 kr.
  - De må ta opp et lån for å dekke resten av oppstartskostnadene. De får et lån med månedlig rente på 0,4 % over en periode på 5 år.
- **Månedlige driftskostnader:**
  - Leie av lokaler: 12 000 kr
  - Strøm, vann og renovasjon: 4 500 kr
  - Varekjøp (kaffe, melk, kaker, etc.): 15 000 kr
  - Lønn til ansatte: 30 000 kr
  - Diverse andre kostnader: 5 000 kr

---

##### a) Hvor stort lån trenger Kari og Espen å ta opp for å dekke oppstartskostnadene, og hva blir terminbeløpet hver måned?

##### Beregning av Lånebehov:

**Totale oppstartskostnader:**

$$
\begin{align*}
\text{Totale oppstartskostnader} &= \text{Inventar og møbler} + \text{Kaffemaskiner} + \text{Diverse utstyr} \\
&= 150\,000 + 80\,000 + 50\,000 \\
&= 280\,000\ \text{kr}
\end{align*}
$$

**Egenkapital:**

$$
\text{Egenkapital} = 100\,000\ \text{kr (Kari)} + 100\,000\ \text{kr (Espen)} = 200\,000\ \text{kr}
$$

**Lånebehov:**

$$
\begin{align*}
\text{Lånebehov} &= \text{Totale oppstartskostnader} - \text{Egenkapital} \\
&= 280\,000 - 200\,000 \\
&= 80\,000\ \text{kr}
\end{align*}
$$

##### Beregning av Terminbeløp for Annuitetslån:

**Gitte Verdier:**

- **Lånebeløp (L):** 80 000 kr
- **Månedlig rente (r):** 0,4 % = 0,004
- **Antall terminer (n):** 5 år × 12 måneder = 60 måneder

$$
A = L \times \frac{r \times (1 + r)^n}{(1 + r)^n - 1}
$$


**Beregning av terminbeløp (A):**

$$
\begin{align*}
A &= 80\,000 \times \frac{0,004 \times (1 + 0,004)^{60}}{(1 + 0,004)^{60} - 1} \\
&= 1\,500,08\ \text{kr}
\end{align*}
$$

**Terminbeløpet per måned er cirka 1 500 kr.**

---

##### b) Regn ut de totale månedlige utgiftene inkludert driftskostnadene og lånekostnadene.

##### Månedlige Driftskostnader:

| **Utgiftspost**                | **Beløp (kr)** |
|--------------------------------|----------------|
| Leie av lokaler                | 12 000         |
| Strøm, vann og renovasjon      | 4 500          |
| Varekjøp                       | 15 000         |
| Lønn til ansatte               | 30 000         |
| Diverse andre kostnader        | 5 000          |
| **Sum driftskostnader**        | **66 500 kr**  |

##### Lånekostnader:

- **Terminbeløp:** 1 500 kr (fra del a)

##### Totale Månedlige Utgifter:

$$
\begin{align*}
\text{Totale månedlige utgifter} &= \text{Driftskostnader} + \text{Lånekostnader} \\
&= 66\,500 + 1\,500 \\
&= 68\,000\ \text{kr}
\end{align*}
$$

---

##### c) Kari og Espen har en forventet månedlig inntekt på 85 000 kroner. Vurder om de har god nok margin til å dekke alle kostnadene sine og om det er rom for overskudd.

##### Beregning av Overskudd:

**Forventet månedlig inntekt:**

$$
\text{Inntekt} = 85\,000\ \text{kr}
$$

**Totale månedlige utgifter:**

$$
\text{Utgifter} = 68\,000\ \text{kr}
$$

**Månedlig overskudd:**

$$
\begin{align*}
\text{Overskudd} &= \text{Inntekt} - \text{Utgifter} \\
&= 85\,000 - 68\,000 \\
&= 17\,000\ \text{kr}
\end{align*}
$$


---

##### Oppsummering

- **Lånebehov:** 80 000 kr
- **Månedlig terminbeløp:** Ca. 1 500 kr
- **Totale månedlige utgifter:** 68 000 kr
- **Forventet månedlig inntekt:** 85 000 kr
- **Månedlig overskudd:** 17 000 kr

---

##### Konklusjon

Kari og Espen har planlagt økonomien for kaffebaren på en god måte. Med et forventet månedlig overskudd på 17 000 kr har de både rom for å håndtere uforutsette utgifter og mulighet til å investere i videre vekst. Det er viktig at de fortsetter å overvåke både inntekter og utgifter nøye, spesielt i oppstartsfasen, for å sikre bærekraftig drift.

---


### Oppgave 5.3: Økonomisk prioritering for fremtidsdrømmer

Peter er 25 år gammel og drømmer om å gjøre tre store ting de neste fem årene: kjøpe en leilighet, starte et eget konsulentfirma, og reise på en seks måneder lang reise til Sør-Amerika. For å gjøre dette må han planlegge økonomien sin nøye. Se informasjonen nedenfor:

- **Månedsinntekt:** 45 000 kr brutto, med 30 % skatt.
- **Månedlige faste utgifter:**
  - Leie av leilighet: 12 000 kr
  - Mat og husholdning: 6 000 kr
  - Transport og diverse: 3 000 kr
  - Sparing til konsulentfirma: 4 000 kr
- **Sparekonto for leilighet:** Peter setter av 5 000 kr hver måned til kjøp av egen leilighet. Han ønsker å ha minst 300 000 kroner i egenkapital om fem år.
- **Sparing til reise:** Peter ønsker å spare 2 000 kr i måneden til sin drømmereise. Han forventer at reisen vil koste rundt 150 000 kroner totalt.

---

#### a) Beregn hvor mye netto månedsinntekt Peter har etter skatt.

##### Beregning:

- **Brutto månedsinntekt:** 45 000 kr
- **Skatt (30 %):**
  $$
  45\,000 \times 0,30 = 13\,500\ \text{kr}
  $$
- **Netto månedsinntekt:**
  $$
  \text{Netto inntekt} = 45\,000\ \text{kr} - 13\,500\ \text{kr} = 31\,500\ \text{kr}
  $$

**Svar:** Peter har en netto månedsinntekt på **31 500 kr** etter skatt.

---

#### b) Hvor mye sitter Peter igjen med etter alle faste utgifter, sparing til konsulentfirmaet og sparing til leilighet og reise?

##### Månedlige utgifter og sparing:

1. **Faste utgifter:**
   - Leie av leilighet: 12 000 kr
   - Mat og husholdning: 6 000 kr
   - Transport og diverse: 3 000 kr

2. **Sparing:**
   - Sparing til konsulentfirma: 4 000 kr
   - Sparing til leilighet: 5 000 kr
   - Sparing til reise: 2 000 kr

**Totale månedlige utgifter og sparing:**

$$
\begin{align*}
\text{Totale utgifter} &= 12\,000 + 6\,000 + 3\,000 + 4\,000 + 5\,000 + 2\,000 \\
&= 32\,000\ \text{kr}
\end{align*}
$$

**Netto inntekt:** 31 500 kr

**Beløp til overs:**

$$
\text{Til overs} = \text{Netto inntekt} - \text{Totale utgifter} = 31\,500\ \text{kr} - 32\,000\ \text{kr} = -500\ \text{kr}
$$

**Svar:** Peter går **500 kr i minus** hver måned etter alle utgifter og sparing.

---

#### c) Vurder om Peter har økonomi til å nå sine mål om å kjøpe en leilighet, starte firma og reise. Hva må han eventuelt justere på for å få råd til alt?

### Vurdering:

Peter har et månedlig underskudd på 500 kr. For å nå sine mål må han enten øke inntekten eller redusere utgifter/sparing.

##### Sparing over fem år (60 måneder):

1. **Sparing til leilighet:**

   - Månedlig sparing: 5 000 kr
   - Total sparing:
     $$
     5\,000\ \text{kr/mnd} \times 60\ \text{mnd} = 300\,000\ \text{kr}
     $$
   - **Mål:** 300 000 kr
   - **Resultat:** Han når målet.

2. **Sparing til reise:**

   - Månedlig sparing: 2 000 kr
   - Total sparing:
     $$
     2\,000\ \text{kr/mnd} \times 60\ \text{mnd} = 120\,000\ \text{kr}
     $$
   - **Mål:** 150 000 kr
   - **Resultat:** Mangler 30 000 kr.

   - **Nødvendig månedlig sparing:**
     $$
     \text{Månedlig sparing} = \frac{150\,000\ \text{kr}}{60\ \text{mnd}} = 2\,500\ \text{kr/mnd}
     $$
   - **Behov for å øke sparingen med 500 kr per måned.**

3. **Sparing til konsulentfirma:**

   - Månedlig sparing: 4 000 kr
   - Total sparing:
     $$
     4\,000\ \text{kr/mnd} \times 60\ \text{mnd} = 240\,000\ \text{kr}
     $$
   - **Er dette tilstrekkelig?** Må vurderes opp mot oppstartskostnader.

##### Justeringer:

- **Øke inntekt:**

  - Vurdere ekstrajobb eller lønnsforhandling for å øke nettoinntekten.

- **Redusere utgifter:**

  - **Leie:** Finne en rimeligere bolig eller dele leilighet.
  - **Mat og husholdning:** Kutte ned på matbudsjettet.
  - **Transport og diverse:** Redusere transportkostnader.

- **Justere sparing:**

  - **Sparing til konsulentfirma:** Redusere fra 4 000 kr til 3 000 kr per måned.
  - **Sparing til reise:** Øke fra 2 000 kr til 2 500 kr per måned.

##### Nytt budsjett etter justeringer:

**Nye månedlige utgifter og sparing:**

1. **Faste utgifter:**
   - Leie av leilighet: 12 000 kr
   - Mat og husholdning: 6 000 kr
   - Transport og diverse: 3 000 kr

2. **Justert sparing:**
   - Sparing til konsulentfirma: 3 000 kr
   - Sparing til leilighet: 5 000 kr
   - Sparing til reise: 2 500 kr

**Nye totale utgifter:**

$$
\begin{align*}
\text{Totale utgifter} &= 12\,000 + 6\,000 + 3\,000 + 3\,000 + 5\,000 + 2\,500 \\
&= 31\,500\ \text{kr}
\end{align*}
$$

**Beløp til overs:**

$$
\text{Til overs} = 31\,500\ \text{kr} - 31\,500\ \text{kr} = 0\ \text{kr}
$$

- **Resultat:** Budsjettet balanserer.

**Ny total sparing over fem år:**

1. **Sparing til reise:**

   $$
   2\,500\ \text{kr/mnd} \times 60\ \text{mnd} = 150\,000\ \text{kr}
   $$

2. **Sparing til konsulentfirma:**

   $$
   3\,000\ \text{kr/mnd} \times 60\ \text{mnd} = 180\,000\ \text{kr}
   $$

   - **Vurdering:** Peter må vurdere om 180 000 kr er tilstrekkelig for å starte firmaet.

#### Konklusjon:

- **Peter må justere budsjettet** ved å redusere sparingen til konsulentfirmaet med 1 000 kr og øke sparingen til reisen med 500 kr.
- **Budsjettet balanserer**, men han har ingen økonomisk buffer for uforutsette utgifter.
- **Anbefalinger:**
  - **Vurdere å redusere andre utgifter** for å skape en buffer.
  - **Øke inntekten** gjennom ekstra arbeid eller lønnsforhandlinger.
  - **Revurdere prioriteringer** hvis nødvendige midler ikke kan oppnås.

---


#### d) Peter ønsker å beregne hvor mye feriepenger han vil få utbetalt neste år. Beregn feriepengene basert på hans inntekt og relevante satser.**


##### Beregning av Feriepenger:

I Norge beregnes feriepenger som en prosentandel av feriepengegrunnlaget fra foregående år. Standard sats er 10,2 % for arbeidstakere med 4 uker og 1 dag ferie (25 virkedager), og 12 % for de med 5 ukers ferie (30 virkedager).

###### 1. Finn Peters feriepengegrunnlag:

- **Månedlig bruttoinntekt:** 45 000 kr
- **Årlig bruttoinntekt:**

  $$
  \text{Årlig bruttoinntekt} = 45\,000 \times 12 = 540\,000\ \text{kr}
  $$

###### 2. Beregn feriepenger:

- **Med 4 uker og 1 dag ferie (10,2 %):**

  $$
  \text{Feriepenger} = 540\,000 \times 10,2\% = 540\,000 \times 0,102 = 55\,080\ \text{kr}
  $$

- **Med 5 ukers ferie (12 %):**

  $$
  \text{Feriepenger} = 540\,000 \times 12\% = 540\,000 \times 0,12 = 64\,800\ \text{kr}
  $$

##### Svar:

- **Hvis Peter har rett til 4 uker og 1 dag ferie, vil han få 55 080 kr i feriepenger.**
- **Hvis han har rett til 5 ukers ferie, vil han få 64 800 kr i feriepenger.**

##### Vurdering:

- **Planlegging:** Peter kan ta hensyn til feriepengene i sin økonomiske planlegging.
- **Ekstra inntekt:** Feriepengene kan brukes til å øke sparingen eller dekke uforutsette utgifter.
- **Skatt på feriepenger:** Vær oppmerksom på at skattetrekket kan variere på feriepenger.

---

##### Konklusjon

Ved å justere budsjettet og vurdere ekstra inntektskilder, kan Peter nå sine økonomiske mål. Beregningen av feriepenger gir ham også en bedre oversikt over tilgjengelige midler i fremtiden.

---

##### Anbefalinger

1. **Bufferkonto:** Sett av et månedlig beløp til en buffer for uforutsette utgifter.
2. **Gjennomgå utgifter:** Se etter muligheter for å redusere faste kostnader.
3. **Ekstra inntekt:** Vurder deltidsjobb eller freelance-oppdrag.
4. **Feriepenger:** Inkluder feriepengene i den langsiktige økonomiske planen.

---