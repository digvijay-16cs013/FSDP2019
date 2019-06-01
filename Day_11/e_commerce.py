# -*- coding: utf-8 -*-
"""
Created on Tue May 21 23:47:05 2019

@author: Administrator
"""


# import numpy as np for calculation and matplotlib.pyplot for visualization of data
import numpy as np, matplotlib.pyplot as plt

# getting normally distributed 10000 ranodm values where mean = 100.0 and standard deviation = 20.0
e_commerce = np.random.normal(100.0, 20.0, 10000)

# plotting a histogram  of e_commerce data with 50 bins or buckets
plt.hist(e_commerce, bins = 50)

# to show the histogram
plt.show()

# to calculate mean and median of e_commerce data
print(np.mean(e_commerce), np.median(e_commerce))

# adding an outlier to e_commerce data
val = np.append(e_commerce, 100000000000)

# plotting histogram of updated e_commerce data with 50 bins
plt.hist(val, bins = 50)

# to show the histogram
plt.show()

# to calculate mean and median of updated e_commerce data
print(np.mean(val), np.median(val))
