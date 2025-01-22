# et banksystem med kunder, kontoer og uttak
import random

bankkontonr = [x for x in range(343214543, 343214634)]

class Kunde:
    def __init__(self, navn):
        self.navn = navn

    def kundeinfo(self):
        print(self.navn)

class Konto:
    def __init__(self, eier):
        self.eier = eier
        self.saldo = 0
        self.kontonr = self.nytt_kontonummer()

    def nytt_kontonummer(self):
        i = random.randint(0,len(bankkontonr))
        return bankkontonr.pop(i)

    def få_saldo(self):
        return self.saldo

    def innskudd(self, beløp):
        self.saldo += beløp
        print(f"Du satt inn {beløp} kr på kontoen din.")

    def uttak(self, uttak):
        if uttak > self.saldo:
            print(f"Du oversteg saldoen!")
        else:
            self.saldo -= uttak

    def info(self):
        print(f"Eier: {self.eier.navn}\nSaldo: {self.saldo}\nKontonummer: {self.kontonr} ")



class Bank:
    def __init__(self, navn):
        self.navn = navn
        self.kunder = []

    def ny_kunde(self, navn):
        kunde = Kunde(navn)
        self.kunder.append(kunde)
        return kunde

    def konto_info(self, konto):
        print(f"Konto: {konto.info()}")

