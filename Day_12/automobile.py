# -*- coding: utf-8 -*-
"""
Created on Wed May 22 22:19:57 2019

@author: Administrator
"""


# getting pandas as pd and numpy as np
import pandas as pd, numpy as np

# reads the Automobile data from csv file
auto_data = pd.read_csv('Automobile.csv')

# replaces "NaN" values in price column with median
auto_data['price'] = auto_data['price'].fillna(auto_data['price'].median())

# converts the data of price columns into a numpy array
price = np.array(auto_data['price'])

# finds max, min, mean and std deviation using numpy's buitl in methods
minimum = price.min()
maximum = price.max()
average = price.mean()
std_deviation = price.std()
print('Price :-\nMinimum : {}\nMaximum : {}\nAverage : {}\nStandard Deviation : {}'.format(minimum, maximum, average, std_deviation))
