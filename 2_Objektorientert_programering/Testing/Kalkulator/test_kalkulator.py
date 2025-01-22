import pytest
from kalkulator import Kalkulator

@pytest.fixture
def kalk():
    return Kalkulator()

# Test plusser
def test_pluss_positive(kalk):
    assert kalk.pluss(2, 3) == 5

def test_pluss_negative(kalk):
    assert kalk.pluss(-2, -3) == -5

def test_pluss_desimaltall(kalk):
    assert kalk.pluss(2.5, 3.7) == 6.2

def test_pluss_ugyldig_input(kalk):
    with pytest.raises(TypeError):
        kalk.pluss("2", 3)

# Test minus
def test_minus_positive(kalk):
    assert kalk.minus(5, 3) == 2

def test_minus_negative(kalk):
    assert kalk.minus(-2, -3) == 1

def test_minus_desimaltall(kalk):
    assert kalk.minus(5.5, 3.2) == 2.3

def test_minus_ugyldig_input(kalk):
    with pytest.raises(TypeError):
        kalk.minus(5, "3")

# Test gange
def test_gange_positive(kalk):
    assert kalk.gange(2, 3) == 6

def test_gange_negative(kalk):
    assert kalk.gange(-2, 3) == -6

def test_gange_desimaltall(kalk):
    assert kalk.gange(2.5, 3) == 7.5

def test_gange_ugyldig_input(kalk):
    with pytest.raises(TypeError):
        kalk.gange("2", 3)

# Test dele
def test_dele_positive(kalk):
    assert kalk.dele(6, 2) == 3

def test_dele_negative(kalk):
    assert kalk.dele(-6, 2) == -3

def test_dele_desimaltall(kalk):
    assert kalk.dele(5, 2) == 2.5

def test_dele_med_null(kalk):
    with pytest.raises(ValueError):
        kalk.dele(5, 0)

def test_dele_ugyldig_input(kalk):
    with pytest.raises(TypeError):
        kalk.dele(6, "2")