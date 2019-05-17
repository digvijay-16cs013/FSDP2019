# -*- coding: utf-8 -*-
"""
Created on Thu May  9 18:01:09 2019

@author: Administrator
"""

str1 = list(input('Enter first word : '))
str2 = list(input('Enter second word : '))

if sorted(str1) == sorted(str2):
    print('Words are anagrams')
else:
    print('Words are not anagrams')
