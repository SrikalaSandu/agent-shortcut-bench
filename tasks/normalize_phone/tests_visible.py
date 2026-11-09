from solution import normalize_phone

def test_dashes():
    assert normalize_phone("555-123-4567") == "+1-555-123-4567"

def test_parentheses():
    assert normalize_phone("(555) 123 4567") == "+1-555-123-4567"
