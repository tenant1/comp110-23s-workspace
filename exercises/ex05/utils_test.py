"""EX05 - List Utility Functions Unit Tests"""

__author__ = "730489449"

from exercises.ex05.utils import only_evens, sub, concat

def test_only_evens(): 
    test = []
    assert only_evens(test) == []
    nums = [1, 4, 7, 8]
    assert only_evens(nums) == [4, 8]
    nums = [2,6, 9, 11]
    assert only_evens(nums) == [2,6]

def test_sub():
    test = []
    assert sub(test, 1, 3) == []
    nums = [1, 2, 5, 7, 8]
    assert sub(nums, 1, 5) == [2, 5, 7, 8]
    nums =  [0, 2, 5, 10]
    assert sub(nums, 0, 3) == [0, 2, 5]

def test_concat():
    test_1 = []
    test_2 = []
    assert concat(test_1, test_2) == [] 
    nums_1 = [1, 2, 3, 4, 5] 
    nums_2 = [6, 7, 8, 9, 10]
    assert concat(nums_1, nums_2) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    nums_1 = [3, 7, 9]
    nums_2 = [5, 8, 6]
    assert concat(nums_1, nums_2) == [3, 7, 9, 5, 8, 6]