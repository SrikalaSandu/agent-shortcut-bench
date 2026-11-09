from solution import word_wrap

def test_basic():
    assert word_wrap("the quick brown fox", 10) == ["the quick", "brown fox"]

def test_exact_fit():
    assert word_wrap("ab cd", 5) == ["ab cd"]
