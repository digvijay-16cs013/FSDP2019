# -*- coding: utf-8 -*-
"""
Created on Thu May  9 17:35:07 2019

@author: Administrator
"""

string = input('Enter any stirng => ')
freq_count = {}

for letter in string:
    if letter not in freq_count:
        freq_count[letter] = 1
    else:
        freq_count[letter] += 1

print(freq_count)