from solution import merge_intervals

def test_basic_overlap():
    assert merge_intervals([[1, 3], [2, 6], [8, 10]]) == [[1, 6], [8, 10]]

def test_touching():
    assert merge_intervals([[1, 3], [3, 5]]) == [[1, 5]]
