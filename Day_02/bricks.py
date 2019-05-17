# -*- coding: utf-8 -*-
"""
Created on Wed May  8 18:14:54 2019

@author: Administrator
"""


def make_target(list1):
    
    small_bricks = list1[0]
    
    big_bricks = list1[1]
    
    target = list1[2]
    
    for small_brick in range(small_bricks + 1):
        for big_brick in range(big_bricks + 1):
            
            make_target = small_brick * 1 + big_brick * 5
            
            if make_target == target:
                return True
            elif make_target > target:
                return False
    
    if make_target < target:
         return False
     
        
list_of_input = input('Enter comma separated no of small bricks, no of big bricks and target value : ').split(', ')

int_values = []

for value in list_of_input:
    int_values.append(int(value))

target_build = make_target(int_values.copy())

if target_build:
    print('Target built')
else:
    print('Target couldn\'t build')
         


