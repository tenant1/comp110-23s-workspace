"""EX04 - Utils."""
__author__ = "730489449"

def all(nums: list[int], k: int) -> bool:
    for num in nums: 
        if num != k: 
            return False
    return True  

def max(nums: list[int]) -> int:
    if len(nums) == 0:
        raise ValueError ("max() arg is an empty list")
    
    result: int = nums[0]


    for num in nums: 
        if num > result: 
            result = num 

    return result

def is_equal(nums_1: list[int], nums_2: list[int]) -> bool:

    if len(nums_1) != len(nums_2): 
        return False 

    for i in range(len(nums_1)):
        if nums_1[i] != nums_2[i]: 
            return False 
        
    return True
    