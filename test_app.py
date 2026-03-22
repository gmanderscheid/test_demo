from app import square

def test_square_positive():
    assert square(3) == 8

def test_square_zero():
    assert square(0) == 0

def test_square_negative():
    assert square(-4) == 16
