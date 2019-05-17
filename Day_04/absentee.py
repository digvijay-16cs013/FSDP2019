# -*- coding: utf-8 -*-
"""
Created on Fri May 10 16:02:28 2019

@author: Administrator
"""

names = []
counter = 1

print('Enter maximum of 25 names :-')

while True:
    
    name = input('> ')
    
    if not name or counter == 25:
        break
    
    names.append(name)
    
    counter += 1
    
with open('absentee.txt', 'w') as fp:
    for name in  names:
        fp.write(name + '\n')
        print(name)
        