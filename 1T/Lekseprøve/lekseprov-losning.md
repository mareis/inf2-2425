# Løsningsforslag: Funksjonsuttrykk og Lineære Funksjoner

Som matematikklærer vil jeg gi en grundig gjennomgang av hvert spørsmål med matematiske begrunnelser og forklaringer.

## 1. Identifisering av funksjonsuttrykk (1 poeng)
**Riktig svar: c) x = y² + 2**

**Matematisk begrunnelse:**
En funksjon $$f: A \rightarrow B$$ er en regel som tilordner hvert element $$x$$ i definisjonsmengden $$A$$ nøyaktig én verdi $$f(x)$$ i verdimengden $$B$$. I et funksjonsuttrykk må derfor:
- Den avhengige variabelen (y eller f(x)) være uttrykt ved den uavhengige variabelen (x)
- Hver x-verdi gi nøyaktig én y-verdi

Alternativ c) bryter med dette prinsippet fordi:
- x er uttrykt ved y (motsatt av det som kreves)
- For én x-verdi kan det finnes to y-verdier (siden uttrykket inneholder y²)

## 2. Nullpunkt i lineær funksjon (1 poeng)
**Riktig svar: c) x = 2**

**Matematisk utledning:**
For funksjonen $$f(x) = 3x - 6$$:
1. Nullpunktet er der $$f(x) = 0$$
2. Setter opp likning: $$3x - 6 = 0$$
3. Adderer 6 på begge sider: $$3x = 6$$
4. Dividerer med 3 på begge sider: $$x = 2$$

**Geometrisk tolkning:**
Nullpunktet er der grafen krysser x-aksen, altså der y-koordinaten er 0.

## 3. Stigningstall i lineær funksjon (1 poeng)
**Riktig svar: c) Endringen i y når x øker med 1**

**Matematisk definisjon:**
For en lineær funksjon $$f(x) = ax + b$$ er stigningstallet $$a$$ definert som:
$$a = \frac{\Delta y}{\Delta x} = \frac{y_2 - y_1}{x_2 - x_1}$$

Dette betyr at for enhver endring i x ($$\Delta x = 1$$):
$$\Delta y = a \cdot 1 = a$$

## 4. Parallelle linjer (1 poeng)
**Riktig svar: a) De er like**

**Matematisk bevis:**
To lineære funksjoner $$f(x) = a_1x + b_1$$ og $$g(x) = a_2x + b_2$$ er parallelle hvis og bare hvis:
$$a_1 = a_2$$

Dette følger av at stigningstallet representerer linjens vinkel med x-aksen:
$$\tan \theta = a$$

Parallelle linjer har samme vinkel med x-aksen, derfor må stigningstallene være like.

## 5. Skjæringspunkt med y-aksen (1 poeng)
**Riktig svar: b) 5**

**Matematisk begrunnelse:**
For funksjonen $$f(x) = -2x + 5$$:
- Skjæringspunktet med y-aksen er punktet der $$x = 0$$
- Setter inn $$x = 0$$ i funksjonsuttrykket:
$$f(0) = -2(0) + 5 = 5$$

## 6. Analyse av lineær funksjon $$f(x) = 4x - 9$$ (5 poeng)

### a) Finn f(2) (2 poeng)
**Utregning:**
$$f(2) = 4(2) - 9 = 8 - 9 = -1$$

### b) Løs f(x) = 7 (2 poeng)
**Matematisk utledning:**
1. $$4x - 9 = 7$$
2. $$4x = 16$$ (adderer 9 på begge sider)
3. $$x = 4$$ (dividerer med 4 på begge sider)

**Verifisering:**
$$f(4) = 4(4) - 9 = 16 - 9 = 7$$

### c) Grafisk skisse (1 poeng)
Grafen kan tegnes ved å bruke:
- Stigningstall: $$a = 4$$ (positiv, bratt stigning)
- y-akseskjæring: $$b = -9$$ (startpunkt)
- Nullpunkt: $$x = \frac{9}{4}$$ (der grafen krysser x-aksen)

## 7. Bestem funksjonsuttrykk (2 poeng)
**Gitt:**
- Stigningstall $$a = 2$$
- Punkt $$(2, 5)$$

**Matematisk utledning:**
1. Bruker formen $$y = ax + b$$
2. Setter inn punkt og stigningstall:
   $$5 = 2(2) + b$$
3. Løser for b:
   $$5 = 4 + b$$
   $$b = 1$$
4. Funksjonsuttrykket blir: $$f(x) = 2x + 1$$

## 8. Finn funksjonsuttrykk gjennom to punkter (4 poeng)
**Gitt punkter:** $$(-1, 5)$$ og $$(2, -1)$$

**Matematisk utledning:**
1. Finner stigningstallet:
   $$a = \frac{y_2 - y_1}{x_2 - x_1} = \frac{-1 - 5}{2 - (-1)} = \frac{-6}{3} = -2$$

2. Bruker punkt-stigningstallformen:
   $$y - y_1 = a(x - x_1)$$
   $$y - 5 = -2(x - (-1))$$
   $$y - 5 = -2(x + 1)$$
   $$y - 5 = -2x - 2$$
   $$y = -2x + 3$$

3. Verifisering:
   - Setter inn $$(-1, 5)$$: $$5 = -2(-1) + 3 = 5$$ ✓
   - Setter inn $$(2, -1)$$: $$-1 = -2(2) + 3 = -1$$ ✓

## 9. Verdimengde (2 poeng)
**Gitt:** $$h(x) = 2x + 1, x \in [-2, 2]$$

**Matematisk analyse:**
1. Finner endepunktene:
   - For $$x = -2: h(-2) = 2(-2) + 1 = -4 + 1 = -3$$
   - For $$x = 2: h(2) = 2(2) + 1 = 4 + 1 = 5$$

2. Siden funksjonen er:
   - Lineær (kontinuerlig)
   - Strengt stigende (stigningstall = 2 > 0)
   vil verdimengden være det lukkede intervallet $$[-3, 5]$$

## 10. Praktisk anvendelse (4 poeng)

### a) Funksjonsuttrykk (2 poeng)
**Matematisk modellering:**
- Alternativ A (el-sykkel): 
  $$f(x) = 50 + 20x$$
  - Fast kostnad: 50 kr
  - Variabel kostnad: 20 kr/km
  
- Alternativ B (buss): 
  $$g(x) = 150$$ (konstant funksjon)

### b) Skjæringspunkt (2 poeng)
**Matematisk løsning:**
1. Setter uttrykkene like hverandre:
   $$50 + 20x = 150$$
2. Løser for x:
   $$20x = 100$$
   $$x = 5$$

**Praktisk tolkning:**
- Ved 5 km er kostnadene like (150 kr)
- For turen til Varden (4 km):
  - El-sykkel: $$f(4) = 50 + 20(4) = 130$$ kr
  - Buss: $$g(4) = 150$$ kr
  - El-sykkel er 20 kr billigere

**Grafisk tolkning:**
- $$f(x)$$ er en stigende lineær funksjon
- $$g(x)$$ er en horisontal linje
- Skjæringspunktet (5, 150) representerer distansen der kostnadene er like