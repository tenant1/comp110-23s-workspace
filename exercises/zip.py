"""CQ04 - Dict Function Writing"""

__author__ = "730489449"

def zip(list_1: list[str], list_2: list[int]) -> dict[str,int]: 
    zip = {}
    if len(list_1) == len(list_2) and len(list_1)!=0 and len(list_2)!=0: 
         for i in range(0, len(list_1)):
             zip[list_1[i]]=list_2[i] 
    if len(list_1)!=len(list_2): 
        return dict()
    return zip 
