class Batteri:
    def __init__(self, batteriID: str, energiniva: float, energikapasitet: float):
        if energikapasitet <= 0:
            raise ValueError("Energikapasitet må være større enn 0")
        if energiniva > energikapasitet:
            raise ValueError("Energinivå kan ikke være større enn kapasitet")
        if energiniva < 0:
            raise ValueError("Energinivå kan ikke være negativt")

        self.__batteriID = batteriID
        self.__energiniva = energiniva
        self.__energikapasitet = energikapasitet

    def ladOpp(self, energi: float) -> None:
        if energi < 0:
            raise ValueError("Kan ikke lade med negativ energi")

        self.__energiniva = min(self.__energiniva + energi, self.__energikapasitet)

    def brukEnergi(self, energi: float) -> None:
        if energi < 0:
            raise ValueError("Kan ikke bruke negativ energi")

        if energi > self.__energiniva:
            raise ValueError("Ikke nok energi tilgjengelig")

        self.__energiniva -= energi

    def visEnerginiva(self) -> float:
        return self.__energiniva

