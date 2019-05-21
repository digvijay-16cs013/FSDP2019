# -*- coding: utf-8 -*-
"""
Created on Mon May 20 16:09:41 2019

@author: Administrator
"""


# to import numpy as np
import numpy as np

# to take input and convert it into numpy array
numbers = np.array(list(map(int, input('Enter nine space separated intgers : ').split()[:9])))

# to reshape the numpy array
numbers = numbers.reshape((3, 3))

# print the reshaped 2D array
print(numbers)