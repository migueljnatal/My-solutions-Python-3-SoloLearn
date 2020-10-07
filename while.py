# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 23:57:26 2020

@author: MIGUEL
"""


n = int(input())

sum = 0

resto = 0

while n > 0:
   resto = n % 10
   n = n//10
   sum += resto
    
print(sum)
