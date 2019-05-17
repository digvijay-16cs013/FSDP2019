# -*- coding: utf-8 -*-
"""
Created on Thu May  9 09:51:56 2019

@author: Administrator
"""

def centered_average(values):
    nume = sum(values) - (max(values) + min(values))
    deno = len(values) - 2
    cen_avg = nume // deno
    return cen_avg

values = input('Enter comma separated values => ').split(',')
new_list = []

for item in values:
    new_list.append(int(item.strip()))
    
cen_avg = centered_average(new_list)
print(cen_avg)