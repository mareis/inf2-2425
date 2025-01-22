import pytest
from batteri2 import Batteri

def test_gyldig_initialisering():
    batteri = Batteri("B001", 50.0, 100.0)
    assert batteri.visEnerginiva() == 50.0

def test_energinivå_større_enn_null():
    with pytest.raises(ValueError):
        batteri = Batteri("B001", -50.0, 100.0)


def test_energiniva_type():
    with pytest.raises(TypeError):
        batteri = Batteri("B001", 40, 100.0)





