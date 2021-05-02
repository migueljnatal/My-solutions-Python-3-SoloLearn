# -*- coding: utf-8 -*-
"""
Created on Sat May  1 23:58:50 2021

@author: MIGUEL
"""

text = input()
dict = {}


for char in text:

  if char not in dict:

    dict[char] = 1

  else:

    dict[char] = dict[char] + 1

print(dict)
