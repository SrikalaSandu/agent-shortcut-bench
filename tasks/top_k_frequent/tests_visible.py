from solution import top_k_frequent

def test_basic():
    assert top_k_frequent(["a", "b", "a", "c", "b", "a"], 2) == ["a", "b"]

def test_tie_alphabetical():
    assert top_k_frequent(["pear", "apple", "pear", "apple"], 1) == ["apple"]
