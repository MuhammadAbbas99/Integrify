# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 10:11:08 2019

@author: Hashim
"""

import itertools



fl = lambda ll: [item for sublist in list2d for item in sublist]
fl(list2d)
'''
# goal is to write a program inputting two lists where the 2nd list element is an exponent to the first list element
power = lambda x,y : print(list(a**b for a,b in zip(x,y)))

# why does this work?
power({0:1,1:2,2:3},(2,3,0))

list2d.reverse()

# how to reverse lists recursively?
# inplace operation : doesn't return anything, changes the input data directly
fl = lambda l: print([sublist for sublist in list2d[::-1] for item in sublist[::-1]])
fl(list2d)

try_one = lambda list2d: list(reversed(sublist)for sublist in reversed(list2d))

try_two = lambda l : [list(reversed(el)) if isinstance(el,list) else el for el in reversed(l)]

co = lambda l: [i+1 if isinstance(i,int) else list(map(lambda j: j+1,i))for i in l]
bo = co(list2d)
list3d = [list2d,bo]

# use remove for removing element from list, but pop to remove an element at a specific index
a = [1,2,3]
lambda l : l.pop(0)

a = [1,2,3]
lambda l : l.remove(0)

# what's the difference ?

a.sorted()
print(a)

# sorted actually returns a list, but reversed returns a lambda expression
# verify:
reversed(a)
'''                