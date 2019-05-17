# -*- coding: utf-8 -*-
"""
Created on Thu May  9 16:20:49 2019

@author: Administrator
"""

items = {}
i = ''
print('Enter items and price :-\n')
while True:
    item = input().split()    
    
    if item:
        if len(item) >= 3:
            i = ' '.join(item[:-1])
        else:
            i = item[0]
        
        if i not in items:
            items[i] = int(item[-1])
        else:
            items[i] += int(item[-1])
    else:
        break

print(items)
     