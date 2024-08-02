from numb3rs import validate

def test_normal():
    assert validate('275.3.6.28') == False
    assert validate('192.168.1.123') == True
    assert validate('8.8.8.8') == True
    assert validate('0.0.0.0') == True

def test_missing():
    assert validate('1.0.1') == False
    assert validate('1') == False
    assert validate('') == False
    assert validate('Cat') == False
