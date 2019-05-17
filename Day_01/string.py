# -*- coding: utf-8 -*-
"""
Created on Tue May  7 17:44:40 2019

@author: Administrator
"""

# name from user
name = input('Enter first and last name with a space between them : ')

# finding index of space using find method
index = name.find(' ')

# taking first Name and last name separately
first_name = name[:index]
last_name = name[index+1:]

# Printing names
print(last_name + ' ' + first_name)
