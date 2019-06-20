# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 10:34:45 2019

@author: Hashim
"""

##############
### Bhuwan's solution

def rev(arr):
    new_arr = []
    for i in arr:
        if isinstance(i,list):
            new_arr.append(rev(i))
        else:
            new_arr.append(i)
    new_arr.reverse()
    return new_arr

list1 = [1,2]
list2 = [4,5]
list2d = [list1, list2]

a1 = rev(list2d)
print(a1)
