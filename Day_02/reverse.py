# -*- coding: utf-8 -*-
"""
Created on Thu May  9 07:58:58 2019

@author: Administrator
"""

def reverse_string(string):
    reverse = ''
    
    length = 0
    
    for letter in string:
        length += 1
    
    for index in range(length - 1, -1, -1):
        reverse = reverse + string[index]
    
    print(reverse)

string = input('Enter any string : ')
reverse_string(string)
