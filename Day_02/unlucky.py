# -*- coding: utf-8 -*-
"""
Created on Thu May  9 10:02:36 2019

@author: Administrator
"""

def unlucky_sum(values):
    add = 0
    prev_num = 0
    
    for item in values:
        if prev_num != 13 and item != 13:
            add = add + item
        prev_num = item
    
    return add

values = input('Enter commma separated integers => ').split(',')
int_values = []

for item in values:
    int_values.append(int(item.strip()))

print(unlucky_sum(int_values))