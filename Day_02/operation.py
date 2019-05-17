# -*- coding: utf-8 -*-
"""
Created on Thu May  9 08:40:17 2019

@author: Administrator
"""

def Add(list1):
    add = 0
    for item in list1:
        add = add + item
    print('Sum =', add)
    

def Multiply(list1):
    mul = 1
    for item in list1:
        mul = mul * item
    print('Multiply =', mul)
    

def Largest(list1):
    maximum = list1[0]
    for item in list1:
        if item > maximum:
            maximum = item
    print('Maximum =', maximum)
    

def Smallest(list1):
    minimum = list1[0]
    for item in list1:
        if item < minimum:
            minimum = item
    print('Minimum =', minimum)
    
    
def Sorting(list1):
    length = len(list1)
    for i in range(length - 1):
        for j in range(length - i - 1):
            if list1[j] > list1[j+1]:
                list1[j], list1[j+1] = list1[j+1], list1[j]
    print('Sorted =', list1)
    
    
def Remove_Duplicates(list1):
    found = []
    for item in list1:
        if item not in found:
            found.append(item)
    print('Without Duplicates =', found)
    

        
def Print(list1):
    Add(list1.copy())
    Multiply(list1.copy())
    Largest(list1.copy())
    Smallest(list1.copy())
    Sorting(list1.copy())
    Remove_Duplicates(list1.copy())

list_of_values = input('Enter comma separated list of values => ').split(',')
int_values = []

for value in list_of_values:
    int_values.append(int(value))

Print(int_values.copy())
    