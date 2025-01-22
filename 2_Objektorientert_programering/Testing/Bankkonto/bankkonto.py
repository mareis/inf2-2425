class Bankkonto:
    def __init__(self, konto_id:str, kredittgrense: float):
        if not isinstance(konto_id, str):
            raise TypeError('KontoID must be of type str')

        if not isinstance(kredittgrense, float):
            raise TypeError("kredittgrense must be of type float")

        self.kontoID = konto_id
        self.saldo = 0
        self.kredittgrense = kredittgrense

    def settInn(self, belop:float):
        self.saldo += belop

    def taUt(self, belop:float):
        if belop > self.saldo+self.kredittgrense:
            raise ValueError("Uttak overskrider saldo + kredittgrense")

        if belop < 0:
            raise ValueError("Negative uttak er ikke mulig")

        self.saldo -= belop

    def visSaldo(self):
        return self.saldo