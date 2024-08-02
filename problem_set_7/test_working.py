from working import convert
import pytest

def test_normal():
    assert convert('09:00 AM to 5:00 PM') == '09:00 to 17:00'
    assert convert('9 AM to 5 PM') == '09:00 to 17:00'
    assert convert('10 AM to 8:50 PM') == '10:00 to 20:50'
    assert convert('10:30 PM to 8 AM') == '22:30 to 08:00'

def test_errors():
    with pytest.raises(ValueError):
        convert('9:60 AM to 5:60 PM')
    with pytest.raises(ValueError):
        convert('9 AM - 5 PM')
    with pytest.raises(ValueError):
        convert('09:00 AM - 17:00 PM')
    with pytest.raises(ValueError):
        convert('0')
    with pytest.raises(ValueError):
        convert('9AM to 9PM')
    with pytest.raises(ValueError):
        convert('Hi dude')
    with pytest.raises(ValueError):
        convert("Rooftop tonight we're the skylines, collecting shooting stars wishes in a jar")
    with pytest.raises(ValueError):
        convert('13:60 AM to 12:65 PM')
    with pytest.raises(ValueError):
        convert('5:80 AM to 14:02 PM')
    with pytest.raises(ValueError):
        convert('9AM5PM')