from seasons import is_valid, get_difference, get_words_from_seconds

def test_is_valid():
    assert is_valid('1999-12-03') == True
    assert is_valid('2024-05-01') == True

def test_get_words_from_seconds():
    ...
