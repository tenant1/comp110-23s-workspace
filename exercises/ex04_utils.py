"""EX04 - Utils."""
__author__ = "730489449"

#Given a list of ints and an int, all should return a bool 
# indicating whether or not all the ints in the list are the same as
#  the given int. 
def all(nums: list[int], k: int) -> bool:
    for num in nums: 
        if num != k: 
            return False
    return True  

#The max function is given a list of ints, max should return the 
# largest in the List.
def max(nums: list[int]) -> int:
    #If the list is empty, max should result in a ValueError. 
    if len(nums) == 0:
        raise ValueError ("max() arg is an empty list")
    
    result: int = nums[0]

    for num in nums: 
        if num > result: 
            result = num 

    return result

#Given two lists of int values, return True if every element at 
# every index is equal in both lists.
def is_equal(nums_1: list[int], nums_2: list[int]) -> bool:

    if len(nums_1) != len(nums_2): 
        return False 

    for i in range(len(nums_1)):
        if nums_1[i] != nums_2[i]: 
            return False 
        
    return True
    

print (all([1, 2, 3, 4,], 2)) 
print (max)