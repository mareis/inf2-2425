class Batteri:
    def __init__(self, batteriID: str, energinivå: float, energikapasitet: float):
        self.batteriID = batteriID
        self.energinivå = energinivå
        self.energikapasitet = energikapasitet

    def ladOpp(self, energi: float):
        if energi <= 0:
            raise ValueError("Energi kan ikke være negativ.")
        self.energinivå += energi

    def brukEnergi(self, energi: float):
        if energi <= 0:
            raise ValueError("Energi kan ikke være negativ.")
        if energi > self.energinivå:
            raise ValueError("Ikke nok energi til å bruke.")
        self.energinivå -= energi

    def visEnerginivå(self):
        return self.energinivå
