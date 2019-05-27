# -*- coding: utf-8 -*-
"""
Created on Mon May 27 22:22:23 2019

@author: Administrator
"""

# importing pandas as pd, numpy as np
import pandas as pd, numpy as np

# importing LinearRegression class from scikit-learn's "linear_model" module
from sklearn.linear_model import LinearRegression

# importing LabelEncoder and OneHotEncoder class from scikit-learn's "preprocessing" module
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

# getting data from csv file in Pandas DataFrame
df = pd.read_csv('University_data.csv')

# creating an instance for label encoding
label_encoder = LabelEncoder()

# extracting features from the data in 2D format
features = df.iloc[:, :-1].values

# extracting lables from the data
labels = df.iloc[:, -1].values

# using label encoding for categorical data
features[:, 0] = label_encoder.fit_transform(features[:, 0])

# creaating an instance of OneHotEncoder class by specifying the column index which is to be encoded
one_hot_encoder = OneHotEncoder(categorical_features = [0])

# encoding the labelled data using OneHotEncoding
features = one_hot_encoder.fit_transform(features).toarray()

# discarding first column to remove redundancy
features = features[:, 1:]

# getting the last column as label for our model
labels = df.iloc[:, -1]

# creating an instance of LinearRegression class
regressor = LinearRegression()

# training our model
regressor.fit(features, labels)

# predicting result for some data
regressor.predict(np.array([0, 1, 0, 0, 340, 5, 5, 10, 1]).reshape(1, 9))
