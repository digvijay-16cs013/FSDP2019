# -*- coding: utf-8 -*-
"""
Created on Wed May  8 16:56:03 2019

@author: Administrator
"""

val = int(input('Enter value to construct the pattern : '))
for i in range(val):
    print('* ' * i)
for i in range(val):
    print('* ' * (val - i))