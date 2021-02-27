import pytest

def test_in():
    a = "hello"
    b = "he"
    assert b in a

def test_not_in():
    a = "hello"
    b = "hi"
    assert b not in a

def test_true_1():
    assert id(13)

def test_true_2():
    assert True is not False




pytest.main()
    
