# -*- coding: utf-8 -*-
"""
Created on Wed May  8 17:45:17 2019

@author: Administrator
"""
import string 
alphabets = list(string.ascii_lowercase)
found = []

string = input('Enter any string : ')

for letter in string:
    if letter in alphabets:
        if letter not in found:
            found.append(letter)

if sorted(found) == alphabets:
    print('PANGRAM')
else:
    print('NOT PANGRAM')