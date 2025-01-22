import pytest
from batteri import Batteri

def test_gyldig_initialisering():
    batteri = Batteri("B001", 50.0, 100.0)
    assert batteri.visEnerginiva() == 50.0

def test_ladOpp():
    batteri = Batteri("B001", 50.0, 100.0)
    batteri.ladOpp(20.0)
    assert batteri.visEnerginiva() == 70.0