# Løsningsforslag: Prøve andregradslikninger, faktorisering og identiteter

## Oppgave 1

### a) Faktorisering av $x^2 + x - 6$

**Metode 1: Nullpunktsmetoden**
1. Finn nullpunktene ved å løse $x^2 + x - 6 = 0$
   - ABC-formelen: $x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$
   - $x = \frac{-1 \pm \sqrt{1 - 4(1)(-6)}}{2(1)}$
   - $x = \frac{-1 \pm \sqrt{1 + 24}}{2}$
   - $x = \frac{-1 \pm \sqrt{25}}{2}$
   - $x = \frac{-1 \pm 5}{2}$
   - $x = 2$ eller $x = -3$
2. Faktorene blir: $(x - 2)(x + 3)$

**Metode 2: Inspeksjonsmetoden**
1. Vi leter etter to tall som:
   - Har produkt = -6 (fordi $ac = -6$)
   - Har sum = 1 (fordi $b = 1$)
2. Tallene er -2 og 3
3. Omskriving: 
   $x^2 + x - 6 = x^2 + 3x - 2x - 6 = x(x + 3) - 2(x + 3) = (x - 2)(x + 3)$

### b) Grafisk representasjon

Graf B viser $x^2 + x - 6$ fordi:
1. Grafen skjærer x-aksen i $x = -3$ og $x = 2$ (nullpunktene vi fant i a)
2. Den har positiv førstekoeffisient ($a > 0$), som gir en parabel som åpner oppover
3. Grafen skjærer y-aksen i -6 (sett inn $x = 0$ i uttrykket)

## Oppgave 2

For å finne ekstremalpunkt i $-x^2 + 6x - 10$ uten derivasjon:

1. Dette er en nedovervendt parabel ($a < 0$), så den har en største verdi
2. Omskriv til standardform ved å fullføre kvadratet:
   - $-x^2 + 6x - 10$
   - $-(x^2 - 6x) - 10$
   - $-(x^2 - 6x + 9 - 9) - 10$
   - $-(x - 3)^2 - 10 + 9$
   - $-(x - 3)^2 - 1$
3. Største verdi er -1, når $x = 3$

## Oppgave 3

a) $8a^2 + 16a$
   - Faktoriser ut fellesfaktor
   - $8a(a + 2)$

b) $x^2 - 25$
   - Konjugatsetningen: $a^2 - b^2 = (a + b)(a - b)$
   - $= (x + 5)(x - 5)$

c) $(2x - 4)^2 - 9$
   - La $u = (2x - 4)$
   - $u^2 - 9 = (u + 3)(u - 3)$
   - $= (2x - 4 + 3)(2x - 4 - 3)$
   - $= (2x - 1)(2x - 7)$

d) $2x^2 - 6x - 20$
   1. Fellesfaktor 2: $2(x^2 - 3x - 10)$
   2. Finn faktorer av -10 som gir sum -3: -5 og 2
   3. $= 2(x - 5)(x + 2)$

## Oppgave 4

a) $\frac{x^2 - 9}{x^2 - x - 6}$
   1. Faktoriser teller og nevner:
      - Teller: $x^2 - 9 = (x + 3)(x - 3)$
      - Nevner: $x^2 - x - 6 = (x + 2)(x - 3)$
   2. Forkorte: $\frac{(x + 3)(x - 3)}{(x + 2)(x - 3)} = \frac{x + 3}{x + 2}$

b) $\frac{x^2 - 1}{x^2 - x - 2} - \frac{x + 1}{x - 2}$
   1. Faktoriser begge brøkene:
      - Første brøk:
        * Teller: $x^2 - 1 = (x + 1)(x - 1)$
        * Nevner: $x^2 - x - 2 = (x + 1)(x - 2)$
        * Etter forenkling: $\frac{x - 1}{x - 2}$
      - Andre brøk: $\frac{x + 1}{x - 2}$
   2. Fellesnevner $(x - 2)$:
      $\frac{x - 1}{x - 2} - \frac{x + 1}{x - 2}$
   3. Trekk sammen:
      $\frac{(x - 1) - (x + 1)}{x - 2} = \frac{-2}{x - 2}$

Definisjonsmengde: $x \neq 2$

## Oppgave 5

a) $x^2 + 8x + 16 = 0$
   1. Fullstendig kvadrat: $(x + 4)^2 = 0$
   2. $x = -4$ (dobbel rot)

b) $x^2 = 4x$
   1. $x^2 - 4x = 0$
   2. $x(x - 4) = 0$
   3. $x = 0$ eller $x = 4$

c) $2x^2 - 5x + 2 = 0$
   1. ABC-formelen: $x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$
   2. $x = \frac{5 \pm \sqrt{25 - 16}}{4}$
   3. $x = \frac{5 \pm 3}{4}$
   4. $x = 2$ eller $x = \frac{1}{2}$

d) $\frac{2x^2 + 16x - 18}{x + 3} = 0$
   1. Teller må være 0 (nevner $\neq -3$)
   2. $2x^2 + 16x - 18 = 0$
   3. $x = \frac{-16 \pm \sqrt{256 + 144}}{4}$
   4. $x = \frac{-16 \pm \sqrt{400}}{4}$
   5. $x = \frac{-16 \pm 20}{4}$
   6. $x = 1$ eller $x = -9$

## Oppgave 6

a) $2(x + 2) + 5(x + 1) = 7x + 9$
   1. Venstre side: $2x + 4 + 5x + 5 = 7x + 9$
   2. Dette er en identitet fordi det er sant for alle x-verdier

b) $x^2 - a^2 = (x - a)(a + x)$
   1. Høyre side $= ax + x^2 - a^2 - ax = x^2 - a^2$
   2. Dette er en identitet fordi det er sant for alle x- og a-verdier

## Oppgave 7

For $x^2 - 2kx + 36 = 0$:

1. Diskriminanten bestemmer antall løsninger:
   $D = b^2 - 4ac = 4k^2 - 4(1)(36) = 4k^2 - 144$

2. a) Ingen løsning: $D < 0$
   - $4k^2 - 144 < 0$
   - $k^2 < 36$
   - $-6 < k < 6$

3. b) Én løsning: $D = 0$
   - $4k^2 - 144 = 0$
   - $k^2 = 36$
   - $k = \pm 6$

4. c) To løsninger: $D > 0$
   - $4k^2 - 144 > 0$
   - $k^2 > 36$
   - $k < -6$ eller $k > 6$

## Oppgave 8

Martines feil:
1. Hun forkorter ikke riktig i andre steg
2. Hun får feil faktorisering i nevneren

Riktig løsning:
1. $\frac{2x + 2}{x^2 + 2x + 1}$
2. $= \frac{2(x + 1)}{(x + 1)(x + 1)}$
3. $= \frac{2}{x + 1}$

## Oppgave 9

La x være lengden på korteste etappe.
1. Lengste etappe $= 4x$
2. Nest lengste etappe $= x + 250$
3. Sum = 1150
4. Sett opp likning: $x + (x + 250) + 4x = 1150$
5. $6x + 250 = 1150$
6. $6x = 900$
7. $x = 150$

Derfor:
- Korteste etappe: 150 m
- Nest lengste etappe: 400 m
- Lengste etappe: 600 m

## Oppgave 10

1. Del figuren i to rektangler:
   - Stort rektangel: $(x + 4) \times x$
   - Lite rektangel: $4 \times 2$
2. Totalareal = 36
3. Sett opp likning: $x^2 + 4x + 8 = 36$
4. $x^2 + 4x - 28 = 0$
5. $(x + 7)(x - 3) = 0$
6. $x = 3$ eller $x = -7$
7. Siden x er en lengde, må $x = 3$

Svar: $x = 3$