# -*- coding: utf-8 -*-
"""
Created on Thu May  9 15:56:28 2019

@author: Administrator
"""

days_of_week = input('Enter days of week => ') .split(', ')

weeks = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

for index, day in enumerate(weeks):
    if day not in days_of_week:
        days_of_week.insert(index, day)

days_of_week = tuple(days_of_week)
print(days_of_week)
        
        
    
