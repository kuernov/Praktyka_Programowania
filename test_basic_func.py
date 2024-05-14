import pytest
import utils

def test_sum_numbers():
    assert utils.sum_numbers(2, 3) == 5
    assert utils.sum_numbers(-1, 1) == 0
    assert utils.sum_numbers(0, 0) == 0

def test_is_even():
    assert utils.is_even(4) == True
    assert utils.is_even(7) == False
    assert utils.is_even(0) == True

def test_reverse_string():
    assert utils.reverse_string("hello") == "olleh"
    assert utils.reverse_string("12345") == "54321"
    assert utils.reverse_string("") == ""

def test_is_odd():
    assert utils.is_odd(4) == False
    assert utils.is_odd(7) == True
    assert utils.is_odd(0) == False