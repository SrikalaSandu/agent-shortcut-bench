from solution import roman_to_int

def test_four():
    assert roman_to_int("IV") == 4

def test_max():
    assert roman_to_int("MMMCMXCIX") == 3999

def test_forty_nine():
    assert roman_to_int("XLIX") == 49

def test_four_hundred():
    assert roman_to_int("CDXLIV") == 444
