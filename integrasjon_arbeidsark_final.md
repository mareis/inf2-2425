
# Arbeidsark: Integrasjon i S2

Dette arbeidsarket er designet for å hjelpe deg med å forberede deg til den kommende prøven i integrasjon. Det kombinerer teori, eksempler og oppgaver for å bygge din forståelse av emnet. Fokuset er på å styrke din læring gjennom en pedagogisk tilnærming som inkluderer både analytiske og grafiske metoder.

## Innholdsfortegnelse

1. [Definisjonen av det bestemte integralet](#1-definisjonen-av-det-bestemte-integralet)
2. [Analysens fundamentalteorem](#2-analysens-fundamentalteorem)
3. [Bestemte og ubestemte integraler](#3-bestemte-og-ubestemte-integraler)
4. [Numerisk integrasjon med Python](#4-numerisk-integrasjon-med-python)
5. [Areal mellom graf og x-aksen](#5-areal-mellom-graf-og-x-aksen)
6. [Areal mellom to grafer](#6-areal-mellom-to-grafer)
7. [Blandede oppgaver](#7-blandede-oppgaver)
8. [Introduksjon til avanserte integrasjonsmetoder](#8-introduksjon-til-avanserte-integrasjonsmetoder)
9. [Avslutning](#9-avslutning)

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
\int rac{1}{x} \, dx = \ln|x| + C
$$

### Oppgave 3
Finn det ubestemte integralet:
$$
\int \left(4x^3 - rac{2}{x}ight) \, dx
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

## 5. Areal mellom graf og x-aksen

For å finne arealet mellom grafen til \( f(x) \) og x-aksen, bruker vi det bestemte integralet. Hvis \( f(x) \) er negativ, tar vi absoluttverdien for å finne arealet.

### Oppgave 5
Beregn arealet under kurven \( f(x) = x^2 - 4x + 3 \) fra \( x = 1 \) til \( x = 3 \).

---

## 6. Areal mellom to grafer

Arealet mellom to funksjoner \( f(x) \) og \( g(x) \):
$$
A = \int_{a}^{b} |f(x) - g(x)| \, dx
$$

### Oppgave 6
Gitt \( f(x) = x^2 \) og \( g(x) = 4 \), beregn arealet fra \( x = 0 \) til \( x = 2 \).

---

## 7. Blandede oppgaver

### Oppgave 7
Beregn integralet:
$$
\int_{0}^{3} \left(2x e^{x} + rac{3}{x}ight) \, dx
$$

### Oppgave 8
Finn det ubestemte integralet:
$$
\int \left(5e^{2x} - rac{4}{x}ight) \, dx
$$

### Oppgave 9
Beregn arealet mellom \( f(x) = 2x^3 - 3x + 1 \) og x-aksen.

---

### Flere blandede oppgaver:
10. Numerisk integrasjon for \( \int_{1}^{4} e^x \, dx \).
11. Finn \( \int_{1}^{e} rac{1}{x} \, dx \).
12. Ubestemt integral \( \int e^{3x} \, dx \).
13. Arealberegning med \( f(x) = \ln x \) og \( g(x) = 2 \).

---

## 8. Introduksjon til avanserte integrasjonsmetoder

### Delvis integrasjon:
$$
\int u \, dv = uv - \int v \, du
$$

### Delbrøkoppspalting:
$$
\int rac{3x + 2}{x^2 - x - 2} \, dx
$$

### Oppgave 21
Bruk variabelskifte:
$$
\int rac{2x}{x^2 + 1} \, dx
$$

---

## 9. Avslutning
Dette arbeidsarket dekker sentrale konsepter i S2. Lykke til med forberedelsene til prøven!

