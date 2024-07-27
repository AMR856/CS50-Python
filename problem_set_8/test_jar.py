from jar import Jar
import pytest

def test_init():
    jar = Jar(capacity=15)
    jar1 = Jar()
    assert jar.capacity == 15
    assert jar1.capacity == 12

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5
    with pytest.raises(ValueError):
        jar.deposit(10)
        jar.deposit(15)
    assert jar.size == 5
    jar.deposit(3)
    assert jar.size == 8


def test_withdraw():
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5
    with pytest.raises(ValueError):
        jar.withdraw(8)
        jar.deposit(15)
    assert jar.size == 5
    jar.withdraw(3)
    assert jar.size == 2
