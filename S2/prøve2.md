# **Matematikk S2 – Prøve i Integrasjon**

**Tid:** 90 minutter  
**Ingen hjelpemidler tillatt**

---

### **Oppgave 1 – Grunnleggende integrasjon**

For å hjelpe deg i gang, her er noen grunnleggende integraler:

a) Finn det ubestemte integralet:

$$
\int 3x^2 \, dx
$$

*Tips:* Husk at $\int x^n \, dx = \frac{x^{n+1}}{n+1} + C$, der $ C $ er konstanten for integrasjon.

---

b) Finn det ubestemte integralet:

$$
\int (2x^5 + 5 - \sqrt{x} + e^x) \, dx
$$

*Tips:* Integrer hvert ledd separat.


### **Oppgave 2 – Bestemt integral**

a) Beregn det bestemte integralet:

$$
\int_{0}^{2} (4x - 1) \, dx
$$

*Tips:* Finn det ubestemte integralet først, og bruk deretter de øvre og nedre grensene.

---

b) Beregn:

$$
\int_{1}^{e} \frac{1}{x} \, dx
$$

---

### **Oppgave 3 – Areal mellom graf og x-akse**

Funksjonen $ f(x) = 2x - 4 $ er gitt.

a) Finn nullpunktet til $ f(x) $.

*Tips:* Sett $ f(x) = 0 $ og løs for $ x $.

---

b) Bestem arealet mellom grafen til $ f(x) $ og x-aksen fra $ x = 0 $ til $ x = 4 $.

*Tips:* Tegn grafen for å se hvor funksjonen ligger over eller under x-aksen. Del opp integralet hvis nødvendig og forklar valgene dine.

---

### **Oppgave 4 – Areal mellom to grafer**

Gitt funksjonene $ f(x) = x + 2 $ og $ g(x) = x^2 $.


Beregn arealet mellom grafene til $ f(x) $ og $ g(x) $ i intervallet $-1\leq x \leq 2$ .

---

### **Oppgave 5 – Samlet mengde**

En vannkran lekker slik at vann renner ut med en hastighet gitt ved funksjonen $ v(t) = 0{,}5t $, der $ v(t) $ er i liter per time og $ t $ er tiden i timer.

a) Hvor mye vann har lekket ut etter 4 timer?

b) Hvor lang tid tar det før totalt 10 liter har lekket ut?

---
### **Oppgave 6 – Tolking av Python-kode og trappesummer**

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
    x = -a + i * dx
    total += f(x) * dx

print(total)
```

a) Forklar med egne ord hva denne koden gjør.

b) Beregn verdien som skrives ut av programmet.

c) Bestem arealet mellom grafen og x-aksen i intervallet eleven bruker


