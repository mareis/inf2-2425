class Kalkulator:
    def pluss(self, a: float, b: float) -> float:
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Tallene må være desimaltall eller heltall")
        return a + b

    def minus(self, a: float, b: float) -> float:
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Tallene må være desimaltall eller heltall")
        return a - b

    def gange(self, a: float, b: float) -> float:
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Tallene må være desimaltall eller heltall")
        return a * b

    def dele(self, a: float, b: float) -> float:
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Tallene må være desimaltall eller heltall")
        if b == 0:
            raise ValueError("Kan ikke dele på null")
        return a / b