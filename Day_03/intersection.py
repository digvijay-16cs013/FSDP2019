# -*- coding: utf-8 -*-
"""
Created on Thu May  9 18:06:31 2019

@author: Administrator
"""

ls1 = input('Enter space separated inputs for list 1 : ').split()
ls2 = input('Enter space separated inputs for list 2: ').split()

set1 = set(ls1)
set2 = set(ls2)

intersect = set1.intersection(set2)
new_list = []

for val in intersect:
    new_list.append(int(val))

print(sorted(new_list))
