# -*- coding: utf-8 -*-
"""
Created on Thu May  9 17:13:08 2019

@author: Administrator
"""

teen_age = {}

def fix_teen(age):
    if age >= 13 and age <= 19:
        if age != 15 and age != 16:
            return 0
    return age

while True:
    key = input('Enter key : ')
    if not key:
        break
    value = int(input('Enter value : '))
    teen_age[key] = value
    
    
for name, age in teen_age.items():
    teen_age[name] = fix_teen(age)
    
print(sum(teen_age.values()))    