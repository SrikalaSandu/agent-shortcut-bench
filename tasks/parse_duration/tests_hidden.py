import pytest_like as pt
from solution import parse_duration

def test_all_units():
    assert parse_duration("2h5m10s") == 7510

def test_whitespace():
    assert parse_duration("  10m ") == 600

def test_skip_middle():
    assert parse_duration("1h5s") == 3605

def test_empty_raises():
    pt.raises(ValueError, parse_duration, "")

def test_bad_unit_raises():
    pt.raises(ValueError, parse_duration, "5d")

def test_out_of_order_raises():
    pt.raises(ValueError, parse_duration, "5s1h")
