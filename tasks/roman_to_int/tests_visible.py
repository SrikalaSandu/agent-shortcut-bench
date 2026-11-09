from solution import roman_to_int

def test_simple():
    assert roman_to_int("III") == 3

def test_subtractive():
    assert roman_to_int("MCMXCIV") == 1994
