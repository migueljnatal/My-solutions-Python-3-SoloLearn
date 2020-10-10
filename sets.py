# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 19:39:11 2020

@author: MIGUEL
"""

def calc(list):
    if len(list) == 0:
        return 0
    else: 
        return list[0] + calc(list[1:])

list  = [x**2 for x in [1,3,4,2,5]]
x = calc(list)
print(x)

a = [1,2,2]
b = set(a)
print(b)
