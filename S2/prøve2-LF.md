# Løsningsforslag til Matematikk S2 – Prøve i Integrasjon

---

## **Oppgave 1 – Grunnleggende integrasjon**

### a)

Finn det ubestemte integralet:

$$
\int 3x^2 \, dx
$$

**Løsning:**

Vi bruker integrasjonsregelen for potenser:

$$
\int x^n \, dx = \frac{x^{n+1}}{n+1} + C
$$

Dermed får vi:

$$
\int 3x^2 \, dx = 3 \int x^2 \, dx = 3 \left( \frac{x^{2+1}}{2+1} \right) + C = 3 \left( \frac{x^{3}}{3} \right) + C = x^{3} + C
$$

**Svar:** $\int 3x^2 \, dx = x^{3} + C$

---

### b)

Finn det ubestemte integralet:

$$
\int \left(2x^5 + 5 - \sqrt{x} + e^x \right) \, dx
$$

**Løsning:**

Vi integrerer hvert ledd separat. Husk at $\sqrt{x} = x^{1/2}$.

1. $\int 2x^5 \, dx = 2 \left( \frac{x^{6}}{6} \right) = \frac{1}{3} x^{6}$

2. $\int 5 \, dx = 5x$

3. $\int -\sqrt{x} \, dx = -\int x^{1/2} \, dx = -\left( \frac{x^{3/2}}{3/2} \right) = -\left( \frac{2}{3} x^{3/2} \right)$

4. $\int e^x \, dx = e^x$

Setter vi sammen resultatene:

$$
\int \left(2x^5 + 5 - \sqrt{x} + e^x \right) \, dx = \frac{1}{3} x^{6} + 5x - \frac{2}{3} x^{3/2} + e^x + C
$$

**Svar:** $\int \left(2x^5 + 5 - \sqrt{x} + e^x \right) \, dx = \frac{1}{3} x^{6} + 5x - \frac{2}{3} x^{3/2} + e^x + C$

---

## **Oppgave 2 – Bestemt integral**

### a)

Beregn det bestemte integralet:

$$
\int_{0}^{2} (4x - 1) \, dx
$$

**Løsning:**

Først finner vi det ubestemte integralet:

$$
\int (4x - 1) \, dx = 4 \int x \, dx - \int 1 \, dx = 4 \left( \frac{x^{2}}{2} \right) - x + C = 2x^{2} - x + C
$$

Deretter beregner vi verdien fra $x = 0$ til $x = 2$:

$$
\left[ 2x^{2} - x \right]_0^2 = \left(2 \cdot 2^{2} - 2\right) - \left(2 \cdot 0^{2} - 0\right) = (8 - 2) - 0 = 6
$$

**Svar:** Verdien av det bestemte integralet er **6**.

---

### b)

Beregn:

$$
\int_{1}^{e} \frac{1}{x} \, dx
$$

**Løsning:**

Vi vet at:

$$
\int \frac{1}{x} \, dx = \ln |x| + C
$$

Dermed:

$$
\int_{1}^{e} \frac{1}{x} \, dx = \left[ \ln |x| \right]_1^e = \ln e - \ln 1 = 1 - 0 = 1
$$

**Svar:** Verdien av integralet er **1**.

---

## **Oppgave 3 – Areal mellom graf og x-akse**

Funksjonen $f(x) = 2x - 4$ er gitt.

### a)

Finn nullpunktet til $f(x)$.

**Løsning:**

Sett $f(x) = 0$:

$$
2x - 4 = 0 \implies 2x = 4 \implies x = 2
$$

**Svar:** Nullpunktet er **$x = 2$**.

---

### b)

Bestem arealet mellom grafen til $f(x)$ og x-aksen fra $x = 0$ til $x = 4$.

**Løsning:**

Funksjonen krysser x-aksen ved $x = 2$. Vi deler derfor opp integralet i to intervaller:

1. Fra $x = 0$ til $x = 2$, der $f(x)$ er negativ.
2. Fra $x = 2$ til $x = 4$, der $f(x)$ er positiv.

Vi beregner arealet ved å summere de absolutte verdiene av integralet i hvert intervall.

Finner det ubestemte integralet:

$$
\int (2x - 4) \, dx = x^{2} - 4x + C
$$

Beregner første integral:

$$
I_1 = \int_{0}^{2} (2x - 4) \, dx = \left[ x^{2} - 4x \right]_0^2 = (4 - 8) - (0 - 0) = -4
$$

Beregner andre integral:

$$
I_2 = \int_{2}^{4} (2x - 4) \, dx = \left[ x^{2} - 4x \right]_2^4 = (16 - 16) - (4 - 8) = 0 - (-4) = 4
$$

Totalt areal:

$$
A = |I_1| + I_2 = |-4| + 4 = 4 + 4 = 8
$$

**Svar:** Arealet mellom grafen og x-aksen er **8 enheter**.

---

## **Oppgave 4 – Areal mellom to grafer**

Gitt funksjonene $f(x) = x + 2$ og $g(x) = x^2$.

**Løsning:**

Først finner vi skjæringspunktene ved å sette $f(x) = g(x)$:

$$
x + 2 = x^2 \implies x^2 - x - 2 = 0 \implies (x - 2)(x + 1) = 0
$$

Skjæringspunktene er ved $x = -1$ og $x = 2$.

Vi skal beregne arealet mellom grafene fra $x = -1$ til $x = 2$.

Integranden er forskjellen mellom funksjonene:

$$
A = \int_{-1}^{2} [f(x) - g(x)] \, dx = \int_{-1}^{2} [(x + 2) - x^2] \, dx
$$

Forenkler uttrykket:

$$
(x + 2) - x^2 = -x^2 + x + 2
$$

Integrerer:

$$
\int_{-1}^{2} (-x^2 + x + 2) \, dx = \left[ -\frac{x^{3}}{3} + \frac{x^{2}}{2} + 2x \right]_{-1}^{2}
$$

Beregner ved $x = 2$:

$$
F(2) = -\frac{8}{3} + 2 + 4 = -\frac{8}{3} + 6 = \frac{10}{3}
$$

Beregner ved $x = -1$:

$$
F(-1) = \frac{1}{3} + \frac{1}{2} - 2 = \frac{5}{6} - 2 = -\frac{7}{6}
$$

Arealet blir:

$$
A = F(2) - F(-1) = \frac{10}{3} - \left( -\frac{7}{6} \right) = \frac{10}{3} + \frac{7}{6} = \frac{27}{6} = \frac{9}{2} = 4.5
$$

**Svar:** Arealet mellom grafene er **$4{,}5$ enheter**.

---

## **Oppgave 5 – Samlet mengde**

En vannkran lekker med hastighet $v(t) = 0{,}5t$, der $v(t)$ er i liter per time og $t$ er i timer.

### a)

Hvor mye vann har lekket ut etter 4 timer?

**Løsning:**

Total lekket vannmengde er gitt ved:

$$
V = \int_{0}^{4} v(t) \, dt = \int_{0}^{4} 0{,}5t \, dt = 0{,}5 \int_{0}^{4} t \, dt = 0{,}5 \left[ \frac{t^{2}}{2} \right]_0^4 = 0{,}5 \left( \frac{16}{2} - 0 \right) = 0{,}5 \times 8 = 4
$$

**Svar:** Det har lekket ut **4 liter** etter 4 timer.

---

### b)

Hvor lang tid tar det før totalt 10 liter har lekket ut?

**Løsning:**

Vi løser likningen:

$$
V = \int_{0}^{t} v(t) \, dt = 10
$$

Beregner integralet:

$$
\int_{0}^{t} 0{,}5t \, dt = 0{,}5 \left[ \frac{t^{2}}{2} \right]_0^t = \frac{0{,}5 t^{2}}{2} = \frac{t^{2}}{4}
$$

Setter inn:

$$
\frac{t^{2}}{4} = 10 \implies t^{2} = 40 \implies t = \sqrt{40} = 2\sqrt{10} \approx 6{,}32 \text{ timer}
$$

**Svar:** Det tar cirka **6,32 timer** før 10 liter har lekket ut.

---

## **Oppgave 6 – Tolking av Python-kode og trappesummer**

En elev skriver følgende Python-kode:

```python
def f(x):
    return x**3 - 4*x

a = -2
b = 2
n = 100
dx = (b - a) / n
total = 0
for i in range(n):
    x = a + i * dx
    total += f(x) * dx

print(total)
```

### a)

**Forklaring av koden:**

Koden estimerer verdien av det bestemte integralet av funksjonen $f(x) = x^3 - 4x$ fra $x = -2$ til $x = 2$ ved hjelp av en venstre Riemann-sum med $n = 100$ rektangler.

- **Definisjon av funksjonen:** `f(x)` returnerer verdien av $x^3 - 4x$.
- **Grenseverdier:** Integrasjonsintervallet er fra $a = -2$ til $b = 2$.
- **Antall rektangler:** $n = 100$, som bestemmer presisjonen av tilnærmingen.
- **Stegbredde:** `dx` er bredden på hvert rektangel, gitt ved $(b - a) / n$.
- **Akkumulering av areal:** Løkken summerer opp arealet av hvert rektangel ved å multiplisere funksjonsverdien i venstre endepunkt av hvert delintervall med `dx`.
- **Utskrift av resultat:** Til slutt skrives den estimerte verdien av integralet ut.

---

### b)

**Beregning av verdien som skrives ut av programmet:**

Det eksakte verdien av integralet er:

$$
\int_{-2}^{2} (x^3 - 4x) \, dx = \left[ \frac{x^4}{4} - 2x^2 \right]_{-2}^2
$$

Beregner ved $x = 2$:

$$
F(2) = \frac{16}{4} - 2 \cdot 4 = 4 - 8 = -4
$$

Beregner ved $x = -2$:

$$
F(-2) = \frac{16}{4} - 2 \cdot 4 = 4 - 8 = -4
$$

Så integralet er:

$$
\int_{-2}^{2} (x^3 - 4x) \, dx = F(2) - F(-2) = (-4) - (-4) = 0
$$

Programmet vil derfor skrive ut en verdi nær **0**. Eventuelle avvik skyldes numeriske feil i tilnærmingen.

---

### c)

**Bestemmelse av arealet mellom grafen og x-aksen:**

For å finne det totale arealet mellom grafen til $f(x)$ og x-aksen fra $x = -2$ til $x = 2$, må vi integrere den absolutte verdien av funksjonen:

$$
A = \int_{-2}^{2} |x^3 - 4x| \, dx
$$

Finn nullpunktene til $f(x)$ innenfor intervallet:

$$
x^3 - 4x = 0 \implies x(x^2 - 4) = 0 \implies x = 0, x = -2, x = 2
$$

Del opp integralet i intervaller hvor funksjonen er henholdsvis positiv og negativ:

1. Fra $x = -2$ til $x = 0$, er $f(x) > 0$.
2. Fra $x = 0$ til $x = 2$, er $f(x) < 0$.

Beregner arealet:

$$
A = \int_{-2}^{0} f(x) \, dx - \int_{0}^{2} f(x) \, dx
$$

Bruker antiderivatet:

$$
F(x) = \frac{x^4}{4} - 2x^2
$$

Beregner:

$$
A = [F(0) - F(-2)] - [F(2) - F(0)] = [0 - (-4)] - (-4 - 0) = (4) - (-4) = 4 + 4 = 8
$$

**Svar:** Arealet mellom grafen og x-aksen er **8 enheter**.
