# -*- coding: utf-8 -*-
"""
Created on Thu May  9 17:45:18 2019

@author: Administrator
"""

import string
digits = list('0123456789')
alphabets = list(string.ascii_lowercase)

dict_1 = {'Digits' : 0, 'Letters' : 0}

s = input('Enter any string : ')
for letter in s:
    if letter in digits:
        dict_1['Digits'] += 1
    if letter.lower() in alphabets:
        dict_1['Letters'] += 1

for k, v in dict_1.items():
    print(k, v)