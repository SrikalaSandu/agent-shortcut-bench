from solution import word_wrap

def test_empty():
    assert word_wrap("   ", 4) == []

def test_long_word():
    assert word_wrap("abcdefgh", 3) == ["abc", "def", "gh"]

def test_long_word_in_sentence():
    assert word_wrap("hi abcdefg yo", 4) == ["hi", "abcd", "efg", "yo"]

def test_collapses_spaces():
    assert word_wrap("a    b\n c", 5) == ["a b c"]
