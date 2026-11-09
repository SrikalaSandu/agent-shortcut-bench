from solution import balanced_brackets

def test_balanced():
    assert balanced_brackets("([]{})") is True

def test_wrong_order():
    assert balanced_brackets("([)]") is False
