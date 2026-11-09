import pytest_like as pt
from solution import normalize_phone

def test_country_code_plus():
    assert normalize_phone("+1 212.555.0199") == "+1-212-555-0199"

def test_country_code_plain():
    assert normalize_phone("1 (646) 555-0100") == "+1-646-555-0100"

def test_too_short():
    pt.raises(ValueError, normalize_phone, "555-1234")

def test_letters():
    pt.raises(ValueError, normalize_phone, "555-CALL-NOW")

def test_too_long():
    pt.raises(ValueError, normalize_phone, "22-555-123-4567")
