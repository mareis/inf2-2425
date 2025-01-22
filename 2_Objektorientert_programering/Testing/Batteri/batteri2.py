class Batteri:
    def __init__(self, batteriID: str, energiniva: float, energikapasitet: float):
        if not isinstance(energiniva, (float)) or not isinstance(energikapasitet, (float)):
            raise TypeError("Energinivå og energikapasitet må være desimaltall")

        if not isinstance(batteriID, (str)):
            raise TypeError("BatterID må være str")

        if energiniva < 0:
            raise ValueError("Energinivå må være større enn 0")

        self.__batteriID = batteriID
        self.__energiniva = energiniva
        self.__energikapasitet = energikapasitet

    def ladOpp(self, energi: float) -> None:
        self.__energiniva = min(self.__energiniva + energi, self.__energikapasitet)

    def brukEnergi(self, energi: float) -> None:
        self.__energiniva -= energi

    def visEnerginiva(self) -> float:
        return self.__energiniva

