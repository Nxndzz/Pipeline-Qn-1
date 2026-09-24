from app import square,is_even
def test_square():
    assert square(5) == 25
    assert square(4) == 16

def test_is_even():
    assert is_even(4) is True
    assert is_even(5) is False
