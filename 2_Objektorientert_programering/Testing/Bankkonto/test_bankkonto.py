from bankkonto import Bankkonto
import pytest


def test_kredittgrense_type():
    with pytest.raises(TypeError):
        konto = Bankkonto("7sdghsud", "Mikkel")

def test_kontoID_type():
    with pytest.raises(TypeError):
        konto = Bankkonto(1, 10_000.00)

def test_taUt_for_mye():
    konto = Bankkonto("sadjb", 10_000.00)
    with pytest.raises(ValueError):
        konto.taUt(20_000.00)

def test_taUt_nagative_verdier():
    konto = Bankkonto("sadjb", 10_000.00)
    with pytest.raises(ValueError):
        konto.taUt(-5_000.00)


#teste feil:
def test_visSaldo():
    konto = Bankkonto("sadjb", 10_000.00)
    assert konto.visSaldo() == 0









