from solution import top_k_frequent

def test_k_too_large():
    assert top_k_frequent(["x", "y", "x"], 5) == ["x", "y"]

def test_empty():
    assert top_k_frequent([], 3) == []

def test_k_zero():
    assert top_k_frequent(["a", "a"], 0) == []

def test_many_ties():
    assert top_k_frequent(["d", "c", "b", "a"], 3) == ["a", "b", "c"]
