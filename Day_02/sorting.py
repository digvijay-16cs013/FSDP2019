# -*- coding: utf-8 -*-
"""
Created on Thu May  9 09:21:05 2019

@author: Administrator
"""

print('Enter Name, Age and Height of students :-')
lines = []
new_list = []

# Taking multiple line input from user
while True:
    line = input()
    if line:
        lines.append(line)
    else:
        break

# Creating input in list of tuples
for line in lines:
    values = line.split(',')
    values[1] = int(values[1])
    values[2] = int(values[2])
    value_tuple = tuple(values)
    new_list.append(value_tuple)
    
# Sorting using bubble sort    
for i in range(len(new_list) - 1):
    for j in range(len(new_list) - i - 1):
        if new_list[j] > new_list[j+1]:
            new_list[j], new_list[j+1] = new_list[j+1], new_list[j]

# sorted list of tuples
print(new_list)