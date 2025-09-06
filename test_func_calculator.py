import func_calculator as fc
import pytest

@pytest.fixture
def c():
    return fc.Calculator()


def test_add_simple():
    c = fc.Calculator()
    assert c.add(2,3) == 5

def test_add_zeros():
    c = fc.Calculator()
    assert c.add(0,0) == 0

def test_add_negative():
    c = fc.Calculator()
    assert c.add(2, 3) != 6

# ///////////////

def test_substract_simple():
    c = fc.Calculator()
    assert c.substract(2,3) == -1

def test_substract_zeros():
    c = fc.Calculator()
    assert c.substract(0,0) == 0

def test_substract_negative():
    c = fc.Calculator()
    assert c.substract(2, 3) != -2

# ///////////////

def test_multiply_simple():
    c = fc.Calculator()
    assert c.multiply(2,3) == 6

def test_multiply_zero():
    c = fc.Calculator()
    assert c.multiply(2,0) == 0

def test_multiply_negative():
    c = fc.Calculator()
    assert c.multiply(3, 3) != 10

# ///////////////

def test_devide_simple():
    c = fc.Calculator()
    assert c.devide(3,3) == 1.0

def test_devide_minus():
    c = fc.Calculator()
    assert c.devide(-2,1) == -2.0

def test_devide_negative():
    c = fc.Calculator()
    assert c.devide(100, 10) != 9.0


# ///////////////

def test_max_simple():
    c = fc.Calculator()
    assert c.max(3, 10) == 10

def test_max_equel():
    c = fc.Calculator()
    assert c.max(10, 10) == 10

def test_max_negative():
    c = fc.Calculator()
    assert c.max(-2, -1) == -1

# ///////////////

def test_min_simple():
    c = fc.Calculator()
    assert c.min(1, 2) == 1

def test_min_negative():
    c = fc.Calculator()
    assert c.min(-5, 2) == -5

def test_min_equal():
    c = fc.Calculator()
    assert c.min(2, 2) == 2

# ///////////////

def test_percentage_fractional():
    c = fc.Calculator()
    assert c.percentage(7, 2) == 0.14

def test_percentage_simple():
    c = fc.Calculator()
    assert c.percentage(50, 10) == 5.0

def test_percentage_negative():
    c = fc.Calculator()
    assert c.percentage(-50, 10) == -5.0

# ///////////////

def test_exp_simple():
    c = fc.Calculator()
    assert c.exp(2, 3) == 8

def test_exp_fractional():
    c = fc.Calculator()
    assert c.exp(2, -3) == 0.125

def test_exp_negative():
    c = fc.Calculator()
    assert c.exp(-2, 3) == -8

# ///////////////

@pytest.fixture(params=[(-2, -3, -5), (-2, 3, 1)])
def additional_info(request):
    return request.param

@pytest.fixture(params=[(-2, 3, -5)])
def subtractional_info(request):
    return request.param

def test_add_with_fixtures(c, additional_info):
    a, b, expected = additional_info
    assert c.add(a, b) == expected

def test_add_with_fixtures_second(c, additional_info):
    a, b, expected = additional_info
    assert c.add(a, b) == expected

def test_substract_with_fixture(c, subtractional_info):
    a, b, expected = subtractional_info
    assert c.substract(a, b) == expected