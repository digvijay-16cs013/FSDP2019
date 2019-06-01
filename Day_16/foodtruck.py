# -*- coding: utf-8 -*-
"""
Created on Mon May 27 22:12:54 2019

@author: Administrator
"""
# getting pandas as pd, numpy as np
import pandas as pd, numpy as np

# getting LinearRegression class from scikit-learn.linear_model
from sklearn.linear_model import LinearRegression

# getting data from csv file
df = pd.read_csv('Foodtruck.csv')

# getting features in 2d format since only 2d data is allowed to train the model
features = df.iloc[:, :-1].values

# getting labels (it may either be in 2d foramt or 1d format)
labels = df['Profit'].values

# creating an instance of LinearRegression class
regressor = LinearRegression()

# training our model
regressor.fit(features, labels)

# converting the data in 2d format
Jaipur = np.array(3.073).reshape(1, 1)

# predicting the result using our model
print(regressor.predict(Jaipur)[0])
