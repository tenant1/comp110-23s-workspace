"""EX05 - List Utility Functions"""

__author__ = "730489449"

#Given a list of ints, only_evens should return a new list containing only the elements of the input list that were even.
def only_evens(nums_1: list[int]) -> list[int]: 
    """Given a list of ints, only_evens should return a new list 
    containing only the elements of the input list that were even."""
    result: list[int] = []
    for num in nums_1:
        if num % 2 == 0: 
            result.append(num)
    
    return result


#Given two Lists of ints, concat should generate a new List which contains all of the elements of the first list followed by all 
# of the elements of the second list.
def concat(nums_1: list[int], nums_2: list[int]) -> list[int]: 
    """Given two Lists of ints, concat should generate a new List 
    which contains all of the elements of the first list followed by 
    all of the elements of the second list."""
    result: list[int] = []
    for num in nums_1: 
        result.append(num)
    for num in nums_2:
        result.append(num)

    return result

#Given a list of ints, a start index, and an end index (not inclusive), sub should generate a List which is a subset of the given list, 
# between the specified start index and the end index - 1.        
def sub(nums_1: list[int], f: int, e: int) -> list[int]: 
    """Given a list of ints, a start index, and an end index 
    (not inclusive), sub should generate a List which is a subset of 
    the given list, iven a list of ints, a start index, and an end 
    index (not inclusive), sub should generate a List which is a 
    subset of the given list, """
    result: list[int] = []
    if f >= len(nums_1):
        return result
    if e < 0: 
        return result
    if f >= e: 
        return result
    if len(nums_1) == 0:
        return result 
    if f < 0: 
        f = 0
    if e >= len(nums_1):
        e = len(nums_1) 
    for i in range(f,e): 
        result.append(nums_1[i])

    return result