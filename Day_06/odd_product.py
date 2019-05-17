# -*- coding: utf-8 -*-
"""
Created on Tue May 14 14:25:35 2019

@author: Administrator
"""

from functools import reduce
numbers = list(map(int, input('Enter space separated integers : ').split()))
product_odd = reduce(lambda x, y : x * y, list(filter(lambda x: x % 2 != 0, numbers)))
print('product of odd numbers :', product_odd)