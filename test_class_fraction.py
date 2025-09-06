import class_fraction as cf
import pytest

@pytest.fixture
def f():
    return cf.Fraction(1, 1)

def test_add_one_plus_one(f):
    res = f.add(cf.Fraction(1, 1))
    assert (res.a, res.b) == (2, 1)

def test_add_one_plus_half(f):
    res = f.add(cf.Fraction(1, 2))
    assert (res.a, res.b) == (3, 2)

def test_add_one_plus_negative_third(f):
    res = f.add(cf.Fraction(-1, 3))
    assert (res.a, res.b) == (2, 3)

# ////////////////////////

def test_subtract_one_minus_one(f):
    res = f.subtract(cf.Fraction(1, 1))
    assert (res.a, res.b) == (0, 1)

def test_subtract_one_minus_half(f):
    res = f.subtract(cf.Fraction(1, 2))
    assert (res.a, res.b) == (1, 2)

def test_subtract_one_minus_negative_third(f):
    res = f.subtract(cf.Fraction(-1, 3))
    assert (res.a, res.b) == (4, 3)

# ////////////////////////

def test_multiply_one_multiply_one(f):
    res = f.multiply(cf.Fraction(1, 1))
    assert (res.a, res.b) == (1, 1)

def test_multiply_one_multiply_half(f):
    res = f.multiply(cf.Fraction(1, 2))
    assert (res.a, res.b) == (1, 2)

def test_multiply_one_multiply_negative_third(f):
    res = f.multiply(cf.Fraction(-1, 3))
    assert (res.a, res.b) == (-1, 3)

# ////////////////////////

def test_divide_one_divide_one(f):
    res = f.divide(cf.Fraction(1, 1))
    assert (res.a, res.b) == (1, 1)

def test_divide_one_divide_half(f):
    res = f.divide(cf.Fraction(1, 2))
    assert (res.a, res.b) == (2, 1)

def test_divide_one_divide_negative_third(f):
    res = f.divide(cf.Fraction(-1, 3))
    assert (res.a, res.b) == (3, -1)

def test_divide_by_zero():
    f1 = cf.Fraction(1, 2)
    f0 = cf.Fraction(0, 3)
    with pytest.raises(ZeroDivisionError):
        f1.divide(f0)