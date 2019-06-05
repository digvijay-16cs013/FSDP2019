# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 14:43:20 2019

@author: Administrator
"""

"""Q1. (Create a program that fulfills the following specification.)

Program Specification:

Import breast_cancer.csv file.

This breast cancer database was obtained from the University of Wisconsin

Hospitals, Madison from Dr. William H. Wolberg.

Attribute Information: (class attribute has been moved to last column)

Sample Code Number(id number)                     ----> represented by column A.

Clump Thickness (1 – 10)                                     ----> represented by column B.
Uniformity of Cell Size(1 - 10)                             ----> represented by column C.
Uniformity of Cell Shape (1 - 10)                        ----> represented by column D.
Marginal Adhesion (1 - 10)                                  ----> represented by column E.
Single Epithelial Cell Size (1 - 10)                        ----> represented by column F.
Bare Nuclei (1 - 10)                                               ----> represented by column G.
Bland Chromatin (1 - 10)                                     ----> represented by column H.
Normal Nucleoli (1 - 10)                                      ----> represented by column I.
Mitoses (1 - 10)                                                     ----> represented by column J.
Class: (2 for Benign and 4 for Malignant)         ----> represented by column K. 
A Benign tumor is not a cancerous tumor and Malignant tumor is a cancerous tumor.

                    Impute the missing values with the most frequent values.
                    Perform Classification on the given data-set to predict if the tumor is cancerous or not.
                    Check the accuracy of the model.
                    Predict whether a women has Benign tumor or Malignant tumor, if her Clump thickness is around 6, uniformity of cell size is 2, Uniformity of Cell Shape is 5, Marginal Adhesion is 3, Bland Chromatin is 9, Mitoses is 4, Bare Nuclei is 7, Normal Nuclei is 2 and Single Epithelial Cell Size is 2
                                                                                                                                                                                                                                                                                                            
(you can neglect the id number column as it doesn't seem  a predictor column)
"""


# Importing Support Vector Classifier from Support Vector Machines
from sklearn.svm import SVC

# Importing Train_test_split from scikit-learn's model selection module
from sklearn.model_selection import train_test_split

# Imporing pandas and numpy
import pandas as pd, numpy as np

# Reading the data
data = pd.read_csv('breast_cancer.csv')

# checking null values 
print(data.isnull().any(axis = 0))

# Replacing null values with most frequent value 
data['G'] = data['G'].fillna(data['G'].mode()[0])

# Extracting features from datasets
features = data.drop(['A', 'K'], axis = 1).values

# Extracting labels from datasets
labels = data['K'].values

# spliting training and testing data
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.20, random_state =0)

# creating instance of Support Vector Classifier
rbf = SVC(kernel = 'rbf', random_state = 0)

# Training the model
rbf.fit(features_train, labels_train)

# getting predictions for test data
labels_pred = rbf.predict(features_test)

# Score or accuracy of model for training and testing data
print(rbf.score(features_train, labels_train))
print(rbf.score(features_test, labels_test))

# data of one random woman 
woman_data = np.array([6, 2, 5, 3, 9, 4, 7, 2, 2]).reshape(1, -1)

# Checking woman's condition
if rbf.predict(woman_data) == 4:
    print('Malignant Tumor')
else:
    print('Benign Tumor')
