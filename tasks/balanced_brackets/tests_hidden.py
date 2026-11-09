from solution import balanced_brackets

def test_empty():
    assert balanced_brackets("") is True

def test_with_text():
    assert balanced_brackets("f(a[0]) { return x; }") is True

def test_unclosed():
    assert balanced_brackets("((") is False

def test_extra_close():
    assert balanced_brackets("())") is False

def test_only_close():
    assert balanced_brackets("]") is False
