class Spiller:
    def __init__(self, navn: str, symbol: str):
        self.navn = navn
        self.symbol = symbol


class Brett:
    def __init__(self):
        # Initialiserer en 3x3 2D-liste fylt med tomme strenger
        self.rutenett = [[' ' for _ in range(3)] for _ in range(3)]

    def vis_brett(self):
        separator = "---------"
        brett_visning = f"\n{separator}\n".join([
            f" {rad[0]} | {rad[1]} | {rad[2]} " for rad in self.rutenett
        ])
        print(brett_visning)

    def oppdater_brett(self, rad: int, kolonne: int, symbol: str) -> bool:
        if self.rutenett[rad][kolonne] == ' ':
            self.rutenett[rad][kolonne] = symbol
            return True
        else:
            print("Plassen er allerede opptatt. Prøv igjen.")
            return False

    def sjekk_vinner(self, symbol: str) -> bool:
        # Sjekk rader
        for rad in self.rutenett:
            if all(celle == symbol for celle in rad):
                return True
        # Sjekk kolonner
        for kolonne in range(3):
            if all(self.rutenett[rad][kolonne] == symbol for rad in range(3)):
                return True
        # Sjekk diagonaler
        if self.rutenett[0][0] == self.rutenett[1][1] == self.rutenett[2][2] == symbol:
            return True
        if self.rutenett[0][2] == self.rutenett[1][1] == self.rutenett[2][0] == symbol:
            return True
        return False

    def er_fullt(self) -> bool:
        return all(celle != ' ' for rad in self.rutenett for celle in rad)


class Spill:
    def __init__(self):
        self.brett = Brett()
        self.spiller1 = Spiller('Spiller 1', 'X')
        self.spiller2 = Spiller('Spiller 2', 'O')
        self.aktiv_spiller = self.spiller1

    def bytt_spiller(self):
        self.aktiv_spiller = self.spiller1 if self.aktiv_spiller == self.spiller2 else self.spiller2

    def spill_spill(self):
        while True:
            self.brett.vis_brett()
            print(f"{self.aktiv_spiller.navn}'s tur ({self.aktiv_spiller.symbol})")
            try:
                rad = int(input("Velg rad (0-2): "))
                kolonne = int(input("Velg kolonne (0-2): "))
                if rad not in range(3) or kolonne not in range(3):
                    print("Ugyldig valg. Prøv igjen.")
                    continue
            except ValueError:
                print("Ugyldig input. Prøv igjen.")
                continue
            if self.brett.oppdater_brett(rad, kolonne, self.aktiv_spiller.symbol):
                if self.brett.sjekk_vinner(self.aktiv_spiller.symbol):
                    self.brett.vis_brett()
                    print(f"{self.aktiv_spiller.navn} vinner!")
                    break
                elif self.brett.er_fullt():
                    self.brett.vis_brett()
                    print("Uavgjort!")
                    break
                else:
                    self.bytt_spiller()


if __name__ == "__main__":
    spill = Spill()
    spill.spill_spill()
