from .twttr_main import shorten # type: ignore

def test_normal():
    assert shorten('Twitter') == 'Twttr'
    assert shorten('twitter') == 'twttr'
    assert shorten('Google') == 'Ggl'
    assert shorten('YouTube') == 'YTb'

def test_all():
    assert shorten('aaaeeeiiiooo') == ''
    assert shorten('iiiiiiiiiiiiii') == ''
    assert shorten('Amr') == 'mr'

def test_punctuation():
    assert shorten('Amr@gmail') == 'mr@gml'
    assert shorten('@email.com') == '@ml.cm'

def test_numbers():
    assert shorten('3432434343') == '3432434343'
    assert shorten('@34343343') == '@34343343'
