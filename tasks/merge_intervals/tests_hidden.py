from solution import merge_intervals

def test_unsorted_input():
    assert merge_intervals([[8, 10], [1, 3], [2, 6]]) == [[1, 6], [8, 10]]

def test_empty():
    assert merge_intervals([]) == []

def test_nested():
    assert merge_intervals([[1, 10], [2, 3], [4, 5]]) == [[1, 10]]

def test_does_not_mutate():
    data = [[5, 6], [1, 2]]
    merge_intervals(data)
    assert data == [[5, 6], [1, 2]]

def test_single_points():
    assert merge_intervals([[4, 4], [4, 4], [7, 7]]) == [[4, 4], [7, 7]]
