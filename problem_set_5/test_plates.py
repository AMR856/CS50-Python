from plates_main import is_valid

def test_normal():
    assert is_valid('CS50') == True
    assert is_valid('CS05') == False
    assert is_valid('CS50P') == False
    assert is_valid('PI3.14') == False
    assert is_valid('H') == False
    assert is_valid('OUTATIME') == False

def test_weird_numbers():
    assert is_valid('3333') == False
    assert is_valid('AAAA22') == True
    assert is_valid('AAA380') == True


def test_weird_conditions():
    assert is_valid('AmrAln') == True
    assert is_valid('') == False
    assert is_valid('11AA1A') == False
    assert is_valid('Am1101') == True
