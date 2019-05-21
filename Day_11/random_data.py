# -*- coding: utf-8 -*-
"""
Created on Tue May 21 23:38:16 2019

@author: Administrator
"""


# import Counter from collections module
from collections import Counter

# import numpy abbreviated as np
import numpy as np

# generates 40 random values from range 5 to 15 both inclusive
random_values = np.random.randint(5, 15, 40)

# Part 1 - with numpy :-
# calculates most frequent value
most_frequent = np.bincount(random_values).argmax()

# print most_frequent value
print(most_frequent)

# Part 2 - without numpy :-
# creating a dictionary which contains frequency of each value using Counter 
freq = dict(Counter(random_values))

# to get the maximum ocurrances of a value
maximum = max(freq.values())

# to get the most frequent value
for k, v in freq.items():
    
    # checks if frequency of number is maximum
    if v == maximum:
        
        # get value which occurs most frequently
        most_frequent = k
        
        # get out of the loop if value found
        break
    
# printing the value
print(most_frequent)
