# -*- coding: utf-8 -*-
"""
Created on Tue May 21 23:29:54 2019

@author: Administrator
"""


# importing Counter from collections module
from collections import Counter

# importing numerical python (numpy) abbreviated as np
import numpy as np

# some values
values = np.array([13, 18, 13, 14, 13, 16, 14, 21, 13])

# calculate mean or average of values
mean = np.mean(values)

# calculate median of values
median = np.median(values)

# create a range of values form 21 - 13 using numpy
range_of_values = np.arange(21, 13, -1)

# getting count of each values from the list of "values" and converting the result in the form of dictionary
count = dict(Counter(values))

# finding the maximum occrances of a value
maximum = max(count.values())

# to check printing the value of max ocurrances
#print(count)

# loop to find out the mode of "values"(Number which occurs most frequently)
for key, value in count.items():
    
    # to check if number has maximum ocurrances
    if maximum == value:
        
        # set mode = value(which is represented by key)
        mode = key
        
        # getting out of the loop once we get the most frequent value
        break

# print what we calculated so far
print('Mean =', mean)
print('Median =', median)
print('Mode =', mode)
print('Range =', range_of_values)