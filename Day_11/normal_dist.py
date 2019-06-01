# -*- coding: utf-8 -*-
"""
Created on Tue May 21 23:50:48 2019

@author: Administrator
"""


# to get the numpy as np and matplotlib.pyplot as plt
import numpy as np, matplotlib.pyplot as plt

# generates 1000 random values where mean = 150, standard deviation = 20
data = np.random.normal(150, 20, 1000)

# plots the histogram of values with 100 bins
plt.hist(data, bins = 100)

# to show the histogram
plt.show()

# calculates standard deviation and variance of normally distributed data
print('Standard deviation :', np.std(data), '\nVariance :', np.var(data))