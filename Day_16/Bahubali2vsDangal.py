# -*- coding: utf-8 -*-
"""
Created on Mon May 27 22:17:29 2019

@author: Administrator
"""

# importing pandas as pd, numpy as np
import pandas as pd, numpy as np

# importing LinearRegression class from scikit-learn.linear_model
from sklearn.linear_model import LinearRegression

# getting data from csv file
df = pd.read_csv('Bahubali2_vs_Dangal.csv')

# creating an instance of LinearRegression class
regressor = LinearRegression()

# extracting features from our dataframe in 2d format(which is mandatory)
features = df.iloc[:, :1].values

# extracting labels from our dataframe in 1d format
labels = df.iloc[:, 1:].values

# training our model using features and labels
regressor.fit(features, labels)

# making the data ready to predict something
day = np.array(10).reshape(1, 1)

# predicting the corresponding value for day 10
day_10_pred = regressor.predict(day)

# printing the data on console
print('Bahubali2 :', day_10_pred[0][0])
print('Dangal :', day_10_pred[0][1])


