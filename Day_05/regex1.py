# -*- coding: utf-8 -*-
"""
Created on Sat May 11 16:04:05 2019

@author: Administrator
"""

# regular expression number
import re

# scan number
float_number = input('Enter anything to check if it is floating point number : ')

# to check match
if re.match(r'^[+-]?\d*\.\d+$', float_number):
    
    # if expression found
    print(True)
    
else:
    
    # if expression not found
    print(False)