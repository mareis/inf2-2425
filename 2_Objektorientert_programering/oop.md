Selvfølgelig! Nedenfor finner du løsningsforslag for de oppgitte objektorienterte programmeringsovervakningene. Kodeeksemplene er skrevet i Python.

### Oppgave 1: Bok-klassen

```python
class Bok:
    def __init__(self, tittel, forfatter, antall_sider):
        self.tittel = tittel
        self.forfatter = forfatter
        self.antall_sider = antall_sider

    def vis_info(self):
        print(f"Tittel: {self.tittel}")
        print(f"Forfatter: {self.forfatter}")
        print(f"Antall sider: {self.antall_sider}")

    def oppdater_antall_sider(self, nye_sider):
        self.antall_sider = nye_sider
        print(f"Antall sider er nå oppdatert til: {self.antall_sider}")

# Eksempel på bruk
bok1 = Bok("Harry Potter", "J.K. Rowling", 309)
bok1.vis_info()
bok1.oppdater_antall_sider(350)
```

### Oppgave 2: Konto-klassen

```python
class Konto:
    def __init__(self, kontonummer, saldo=0):
        self.kontonummer = kontonummer
        self.saldo = saldo

    def sett_inn(self, belop):
        if belop > 0:
            self.saldo += belop
            print(f"Sette inn {belop} kroner. Ny saldo: {self.saldo}")
        else:
            print("Beløpet må være over null.")

    def ta_ut(self, belop):
        if belop > 0 and self.saldo >= belop:
            self.saldo -= belop
            print(f"Tatt ut {belop} kroner. Ny saldo: {self.saldo}")
        else:
            print("Ugyldig beløp eller saldo for lav.")

    def vis_saldo(self):
        print(f"Saldo på konto {self.kontonummer}: {self.saldo}")

# Eksempel på bruk
konto1 = Konto("123456789")
konto1.vis_saldo()
konto1.sett_inn(1000)
konto1.ta_ut(250)
```

### Oppgave 3: Rektangel- og Firkant-klassen

```python
class Rektangel:
    def __init__(self, bredde, hoyde):
        self.bredde = bredde
        self.hoyde = hoyde

    def areal(self):
        return self.bredde * self.hoyde

    def omskrevet_krets(self):
        return 2 * (self.bredde + self.hoyde)

class Firkant(Rektangel):
    def __init__(self, side):
        super().__init__(side, side)

# Eksempel på bruk
rektangel1 = Rektangel(4, 6)
print("Rektangel:")
print(f"Areal: {rektangel1.areal()}")
print(f"Omskrevet krets: {rektangel1.omskrevet_krets()}")

firkant1 = Firkant(5)
print("Firkant:")
print(f"Areal: {firkant1.areal()}")
print(f"Omskrevet krets: {firkant1.omskrevet_krets()}")
```

### Oppgave 4: Student- og Kurs-klassen

```python
class Student:
    def __init__(self, navn, studentnummer):
        self.navn = navn
        self.studentnummer = studentnummer
        self.kursliste = []

    def registrer_kurs(self, kurs):
        if kurs not in self.kursliste:
            self.kursliste.append(kurs)
            print(f"{self.navn} er nå registrert på {kurs.navn}.")
        else:
            print(f"{self.navn} er allerede registrert på {kurs.navn}.")

    def vis_kurs(self):
        if self.kursliste:
            print(f"{self.navn} er registrert på følgende kurs:")
            for kurs in self.kursliste:
                print(f"- {kurs.navn}")
        else:
            print(f"{self.navn} er ikke registrert på noen kurs.")

class Kurs:
    def __init__(self, navn, kode):
        self.navn = navn
        self.kode = kode
        self.studentliste = []

    def registrer_student(self, student):
        if student not in self.studentliste:
            self.studentliste.append(student)
            print(f"{student.navn} er nå registrert på {self.navn}.")
        else:
            print(f"{student.navn} er allerede registrert på {self.navn}.")

    def vis_studenter(self):
        if self.studentliste:
            print(f"Følgende studenter er registrert på {self.navn}:")
            for student in self.studentliste:
                print(f"- {student.navn} (Studentnummer: {student.studentnummer})")
        else:
            print(f"Ingen studenter er registrert på {self.navn}.")

# Eksempel på bruk
student1 = Student("Ola Nordmann", "123456")
kurs1 = Kurs("Programmering 1", "INF100")

student1.registrer_kurs(kurs1)
kurs1.vis_studenter()
student1.vis_kurs()
```

### Oppgave 5: Annenkostnad-klassen

```python
class Annenkostnad:
    def __init__(self, beskrivelse, prosent):
        self.beskrivelse = beskrivelse
        self.prosent = prosent

    def beregn_kostnad(self, belop):
        return belop * (self.prosent / 100)

# Eksempel på bruk
skatt = Annenkostnad("Skatteprosent", 25)
rente = Annenkostnad("Rentekostnad", 3)

belop = 1000
print(f"Skatteprosent: {skatt.beregn_kostnad(belop)} kroner")
print(f"Rentekostnad: {rente.beregn_kostnad(belop)} kroner")
```

Disse løsningsforslagene gir et grunnleggende forslag til hvordan man kan implementere de forskjellige oppgavene ved hjelp av objektorientert programmering i Python.