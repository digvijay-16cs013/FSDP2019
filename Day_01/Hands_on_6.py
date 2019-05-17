# -*- coding: utf-8 -*-
"""
Created on Wed May  8 09:41:51 2019

@author: Administrator
"""

num = 1

# loop to iterate 
while True:
    
    # condition to check odd number
    if num % 2 != 0:
        print(num)
    
    # number is incremented by 1    
    num += 1
    
    # condition to get out of the loop using break
    if num == 11:
        break