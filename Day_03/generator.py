# -*- coding: utf-8 -*-
"""
Created on Thu May  9 15:49:53 2019

@author: Administrator
"""
values = input('Enter comma separated values => ')

ls = list(values.split(', '))
tup = tuple(ls)

print('List :', ls)
print('Tuple :', tup)