
# Arbeidsark: Integrasjon i S2

Dette arbeidsarket er designet for å hjelpe deg med å forberede deg til den kommende prøven i integrasjon. Det kombinerer teori, eksempler og oppgaver for å bygge din forståelse av emnet. Fokuset er på å styrke din læring gjennom en pedagogisk tilnærming som inkluderer både analytiske og grafiske metoder.

## Innholdsfortegnelse

1. [Definisjonen av det bestemte integralet](#1-definisjonen-av-det-bestemte-integralet)
2. [Analysens fundamentalteorem](#2-analysens-fundamentalteorem)
3. [Bestemte og ubestemte integraler](#3-bestemte-og-ubestemte-integraler)
4. [Numerisk integrasjon med Python](#4-numerisk-integrasjon-med-python)
5. [Areal mellom to grafer](#5-areal-mellom-to-grafer)
6. [Blandede oppgaver](#6-blandede-oppgaver)
7. [Introduksjon til avanserte integrasjonsmetoder](#7-introduksjon-til-avanserte-integrasjonsmetoder)
8. [Avslutning](#8-avslutning)

---

## 1. Definisjonen av det bestemte integralet

Det bestemte integralet av en funksjon \( f(x) \) fra \( x = a \) til \( x = b \) representerer nettoarealet mellom grafen til \( f(x) \) og x-aksen i intervallet \([a, b]\).

### Formelt:

$$
\int_{a}^{b} f(x) \, dx
$$

### Eksempel:

Beregn integralet:

$$
\int_{0}^{2} (3x) \, dx
$$

**Fremgangsmåte:**  
Finn antiderivert: $$F(x) = \frac{3x^2}{2}$$.  
Evaluér ved grensene:  
$$
F(2) - F(0) = \frac{3 \cdot 2^2}{2} - \frac{3 \cdot 0^2}{2} = 6
$$

### Oppgave 1

Regn ut integralet:

$$
\int_{1}^{4} (2x + 1) \, dx
$$

---

## 2. Analysens fundamentalteorem

Hvis \( F(x) \) er en antiderivert av \( f(x) \), så er:

$$
\int_{a}^{b} f(x) \, dx = F(b) - F(a)
$$

### Oppgave 2

Regn ut integralet:

$$
\int_{2}^{5} e^x \, dx
$$

---

## 3. Bestemte og ubestemte integraler

### Ubestemt integral:

$$
\int f(x) \, dx = F(x) + C
$$

### Eksempel på ubestemt integral:

Finn det ubestemte integralet:

$$
\int \frac{1}{x} \, dx = \ln|x| + C
$$

### Oppgave 3

Finn det ubestemte integralet:

$$
\int \left(4x^3 - \frac{2}{x}
\right) \, dx
$$

---

## 4. Numerisk integrasjon med Python

Bruk numerisk integrasjon til å tilnærme integralet:

```python
a = 1
b = 3
n = 10000

def f(x):
    return 1 / x

I = 0
h = (b - a) / n

for i in range(n):
    x_i = a + i * h
    I += f(x_i) * h

print(f"Tilnærmet verdi av integralet: {I}")
```

### Oppgave 4

Forklar hva koden beregner. Hva tilsvarer dette integralet uttrykt matematisk?

---

## 5. Areal mellom to grafer

Arealet mellom to funksjoner \( f(x) \) og \( g(x) \) over intervallet \([a, b]\):

$$
A = \int_{a}^{b} |f(x) - g(x)| \, dx
$$

### Oppgave 5

Gitt funksjonene \( f(x) = x^2 \) og \( g(x) = 4 \):

**a) Finn skjæringspunktene mellom grafene.**  
**b) Beregn arealet mellom grafene fra \( x = 0 \) til \( x = 2 \).**

---

## 6. Blandede oppgaver

### Oppgave 6

Beregn integralet:

$$
\int_{0}^{3} \left(2x e^{x} + \frac{3}{x}
\right) \, dx
$$

### Oppgave 7

Finn det ubestemte integralet:

$$
\int \left(5e^{2x} - \frac{4}{x}
\right) \, dx
$$

### Oppgave 8

Gitt funksjonen \( f(x) = 2x^3 - 3x + 1 \):

**a) Finn nullpunktene til \( f(x) \).**  
**b) Beregn arealet mellom grafen til \( f(x) \) og x-aksen over intervallet fra det minste til det største nullpunktet.**

---

## 7. Introduksjon til avanserte integrasjonsmetoder

### Delvis integrasjon:

$$
\int u \, dv = uv - \int v \, du
$$

### Delbrøkoppspalting:

Del opp følgende funksjon og integrer:

$$
\int \frac{3x + 2}{x^2 - x - 2} \, dx
$$

---

## 8. Avslutning

Dette arbeidsarket har tatt for seg sentrale konsepter innen integrasjon som er relevante for S2. Lykke til med forberedelsene til prøven!

