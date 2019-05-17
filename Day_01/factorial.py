# -*- coding: utf-8 -*-
"""
Created on Tue May  7 17:12:40 2019

@author: Administrator
"""

# importing factorial method from math module
from math import factorial as fact

# Value from user
val = int(input('Enter a value to find factorial : '))

# Calculating factorial
f = fact(val)

# Printing factorial
print('Factorial is', f)
