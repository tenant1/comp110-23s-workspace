"""EX07 - Dictionary Functions (Test Cases)."""
from dictionary import invert, count, favorite_color
import pytest 


def test_invert1():
    """For the invert function you are to define at least 3x unit test functions. Remember that a unit test function starts with test_."""
    assert invert({'a': 'b', 'c': 'd'}) == {'b': 'a', 'd': 'c'}

    with pytest.raises(KeyError): 
        invert({'key1': 'val1', 'key2': 'val1'})
    
    assert invert({}) == {}


def test_favorite_color(): 
    """For the favorite_color function you are to define at least 3x unit test functions. Remember that a unit test function starts with test_."""
    assert favorite_color({'a': 'red', 'b': 'red', 'c': 'blue'}) == 'red'
    assert favorite_color({'a': 'red', 'b': 'red', 'c': 'blue', 'd': 'blue'}) == 'red'
    assert favorite_color({}) == ''


def test_count():
    """For the count function you are to define at least 3x unit test functions. Remember that a unit test function starts with test_."""
    assert count(['a', 'a', 'b', 'a', 'b', 'c']) == {'a': 3, 'b': 2, 'c': 1}
    assert count([]) == {}       
    assert count(['b', 'a', 'c', 'a']) == {'b': 1, 'a': 2, 'c': 1}