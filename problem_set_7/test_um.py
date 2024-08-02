from um import count

def test_normal():
    assert count('um') == 1
    assert count('um um um um') == 4
    assert count('mmhhum') == 0
    assert count('What are you umming about') == 0
    assert count('UM UM') == 2
    assert count("Um, we're going down in an earlier round UMmUM") == 1

def test_missing():
    assert count('') == 0
    assert count('My name is amr') == 0
    assert count('UMUMUMUMUMUMUMUMUM') == 0
    assert count('umming the ummer to be a better ummer') == 0
