# -*- coding: utf-8 -*-
"""
Created on Wed May  8 17:08:04 2019

@author: Administrator
"""

# numbers from user
num = input('enter space separated integers').split() 

reverse = False
positive = True
new_list = []

for n in num:
    if n == n[::-1] :
        reverse = True
        break

for n in num:
    new_list.append(int(n))
    
for n in new_list:
    if n < 0:
        positive = False
        break

if positive and reverse:
    print(True)
else:
    print(False)

            