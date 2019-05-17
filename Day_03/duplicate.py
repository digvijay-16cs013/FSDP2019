# -*- coding: utf-8 -*-
"""
Created on Thu May  9 18:23:47 2019

@author: Administrator
"""

list1 = [12,24,35,24,88,120,155,88,120,155]

found = []

for item in list1:
    if item not in found:
        found.append(item)
 
print(found[::-1])