# Løsningsforslag: Prøve andregradslikninger, faktorisering og identiteter

## Oppgave 1

### a) Faktorisering av $$x^2 + x - 6$$

Vi skal faktorisere uttrykket med to ulike metoder.

**Metode 1: Nullpunktsmetoden**
For å finne faktorene må vi først finne nullpunktene ved å løse $$x^2 + x - 6 = 0$$
Vi bruker ABC-formelen: $$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$

Med innsetting får vi: 
$$x = \frac{-1 \pm \sqrt{1 - 4(1)(-6)}}{2(1)} = \frac{-1 \pm \sqrt{1 + 24}}{2} = \frac{-1 \pm \sqrt{25}}{2} = \frac{-1 \pm 5}{2}$$

Dette gir oss nullpunktene $$x = 2$$ eller $$x = -3$$
Dermed blir faktoriseringen $$(x - 2)(x + 3)$$

**Metode 2: Inspeksjonsmetoden**
Ved inspeksjon ser vi etter to tall som multiplisert gir $$ac = -6$$ og summert gir $$b = 1$$. 
Disse tallene er -2 og 3. Vi kan da skrive om uttrykket:
$$x^2 + x - 6 = x^2 + 3x - 2x - 6 = x(x + 3) - 2(x + 3) = (x - 2)(x + 3)$$

### b) Grafisk representasjon

Graf B representerer andregradsuttrykket $$x^2 + x - 6$$ av følgende grunner:
Grafen skjærer x-aksen i punktene vi fant i a), altså $$x = -3$$ og $$x = 2$$. Funksjonen har positiv førstekoeffisient ($$a > 0$$), noe som gir en parabel som åpner oppover. Ved å sette inn $$x = 0$$ ser vi at grafen skjærer y-aksen i punktet $$(0, -6)$$.

## Oppgave 2

Vi skal finne ekstremalpunktet til funksjonen $$-x^2 + 6x - 10$$ uten bruk av derivasjon.
Siden $$a = -1$$ er negativ, vet vi at dette er en nedovervendt parabel som har en største verdi.

Vi fullfører kvadratet:
$$-x^2 + 6x - 10 = -(x^2 - 6x) - 10 = -(x^2 - 6x + 9 - 9) - 10 = -(x - 3)^2 - 10 + 9 = -(x - 3)^2 - 1$$

Uttrykket har sin største verdi -1 når $$x = 3$$.

## Oppgave 3

Vi skal faktorisere følgende uttrykk:

a) $$8a^2 + 16a$$
Her trekker vi ut fellesfaktor 8a:
$$8a^2 + 16a = 8a(a + 2)$$

b) $$x^2 - 25$$
Dette er en konjugatsetning der $$a^2 - b^2 = (a + b)(a - b)$$:
$$x^2 - 25 = (x + 5)(x - 5)$$

c) $$(2x - 4)^2 - 9$$
Vi setter $$u = (2x - 4)$$ og bruker konjugatsetningen:
$$u^2 - 9 = (u + 3)(u - 3)$$
Setter tilbake:
$$(2x - 4)^2 - 9 = (2x - 4 + 3)(2x - 4 - 3) = (2x - 1)(2x - 7)$$

d) $$2x^2 - 6x - 20$$
Trekker først ut fellesfaktor 2:
$$2x^2 - 6x - 20 = 2(x^2 - 3x - 10)$$
Faktoriserer innholdet i parentesen:
$$2(x^2 - 3x - 10) = 2(x - 5)(x + 2)$$

## Oppgave 4

a) Vi skal forkorte brøken $$\frac{x^2 - 9}{x^2 - x - 6}$$

Faktoriserer teller og nevner:
Teller: $$x^2 - 9 = (x + 3)(x - 3)$$
Nevner: $$x^2 - x - 6 = (x + 2)(x - 3)$$

Dette gir: $$\frac{x^2 - 9}{x^2 - x - 6} = \frac{(x + 3)(x - 3)}{(x + 2)(x - 3)} = \frac{x + 3}{x + 2}$$

b) Vi skal forkorte uttrykket $$\frac{x^2 - 1}{x^2 - x - 2} - \frac{x + 1}{x - 2}$$

Faktoriserer første brøk:
Teller: $$x^2 - 1 = (x + 1)(x - 1)$$
Nevner: $$x^2 - x - 2 = (x + 1)(x - 2)$$

Dette gir: $$\frac{x^2 - 1}{x^2 - x - 2} = \frac{x - 1}{x - 2}$$

Nå har vi: $$\frac{x - 1}{x - 2} - \frac{x + 1}{x - 2}$$

Med felles nevner får vi:
$$\frac{(x - 1) - (x + 1)}{x - 2} = \frac{-2}{x - 2}$$

Definisjonsmengde: $$x \neq 2$$

## Oppgave 5

a) Vi skal løse $$x^2 + 8x + 16 = 0$$
Dette er et fullstendig kvadrat: $$(x + 4)^2 = 0$$
Som gir løsningen $$x = -4$$ (dobbel rot)

b) Vi skal løse $$x^2 = 4x$$
Omskriver til standardform: $$x^2 - 4x = 0$$
Faktoriserer: $$x(x - 4) = 0$$
Som gir løsningene $$x = 0$$ eller $$x = 4$$

c) Vi skal løse $$2x^2 - 5x + 2 = 0$$
Bruker ABC-formelen:
$$x = \frac{5 \pm \sqrt{25 - 16}}{4} = \frac{5 \pm \sqrt{9}}{4} = \frac{5 \pm 3}{4}$$
Som gir løsningene $$x = 2$$ eller $$x = \frac{1}{2}$$

d) Vi skal løse $$\frac{2x^2 + 16x - 18}{x + 3} = 0$$
For at brøken skal være null, må telleren være null mens nevneren $$\neq -3$$
$$2x^2 + 16x - 18 = 0$$
$$x = \frac{-16 \pm \sqrt{256 + 144}}{4} = \frac{-16 \pm \sqrt{400}}{4} = \frac{-16 \pm 20}{4}$$
Som gir løsningene $$x = 1$$ eller $$x = -9$$

## Oppgave 6

a) Vi skal undersøke om $$2(x + 2) + 5(x + 1) = 7x + 9$$ er en identitet.
Venstre side: $$2(x + 2) + 5(x + 1) = 2x + 4 + 5x + 5 = 7x + 9$$
Dette er identisk med høyre side for alle x-verdier, og er derfor en identitet.

b) Vi skal undersøke om $$x^2 - a^2 = (x - a)(a + x)$$ er en identitet.
Utvider høyre side: $$(x - a)(a + x) = ax + x^2 - a^2 - ax = x^2 - a^2$$
Dette er identisk med venstre side for alle verdier av x og a, og er derfor en identitet.

## Oppgave 7

Vi skal undersøke antall løsninger for likningen $$x^2 - 2kx + 36 = 0$$ basert på verdien av k.
Diskriminanten avgjør antall løsninger: $$D = b^2 - 4ac = 4k^2 - 4(1)(36) = 4k^2 - 144$$

For ingen løsning kreves $$D < 0$$:
$$4k^2 - 144 < 0$$
$$k^2 < 36$$
$$-6 < k < 6$$

For én løsning kreves $$D = 0$$:
$$4k^2 - 144 = 0$$
$$k^2 = 36$$
$$k = \pm 6$$

For to løsninger kreves $$D > 0$$:
$$4k^2 - 144 > 0$$
$$k^2 > 36$$
$$k < -6$$ eller $$k > 6$$

## Oppgave 8

Vi skal vurdere og korrigere Martines løsning av brøkuttrykket $$\frac{2x + 2}{x^2 + 2x + 1}$$

Martine har gjort to feil:
1. Feil faktorisering av nevneren
2. Feil forenkling av brøken

Korrekt løsning:
$$\frac{2x + 2}{x^2 + 2x + 1} = \frac{2(x + 1)}{(x + 1)(x + 1)} = \frac{2}{x + 1}$$

## Oppgave 9

La x være lengden på korteste etappe i meter. Da er:
Lengste etappe = $$4x$$ meter
Nest lengste etappe = $$x + 250$$ meter
Total lengde = 1150 meter

Dette gir likningen:
$$x + (x + 250) + 4x = 1150$$
$$6x + 250 = 1150$$
$$6x = 900$$
$$x = 150$$

Derfor er:
Korteste etappe: 150 meter
Nest lengste etappe: 400 meter
Lengste etappe: 600 meter

## Oppgave 10

Vi deler figuren i to rektangler:
Stort rektangel med areal $$(x + 4)x$$
Lite rektangel med areal $$4 \cdot 2 = 8$$

Totalarealet er 36, som gir likningen:
$$(x + 4)x + 8 = 36$$
$$x^2 + 4x + 8 = 36$$
$$x^2 + 4x - 28 = 0$$
$$(x + 7)(x - 3) = 0$$

Dette gir $$x = 3$$ eller $$x = -7$$
Siden x er en lengde, må $$x = 3$$