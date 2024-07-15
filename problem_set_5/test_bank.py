#!/usr/bin/python3from bank_main import value # type: ignore
import pytest

def test_normal():
    assert value('Hello') == 0
    assert value('Hello, Amr') == 0
    assert value('How you doin?') == 20
    assert value("What's going on here") == 100

def test_all():
    assert value('hello hello hello') == 0
    assert value('Amr, Hi') == 100
    assert value('Here you go') == 20

def test_numbers():
    assert value('130213232, amr') == 100
    with pytest.raises(AttributeError):
        value(8434343433) 
        value(477)
