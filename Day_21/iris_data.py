# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 17:58:45 2019

@author: Administrator
"""


"""
Q2. This famous classification dataset first time used in Fisher’s classic 1936 paper, The Use of Multiple Measurements in Taxonomic Problems. Iris dataset is having 4 features of iris flower and one target class.

The 4 features are

SepalLengthCm
SepalWidthCm
PetalLengthCm
PetalWidthCm
The target class

The flower species type is the target class and it having 3 types

Setosa
Versicolor
Virginica
The idea of implementing svm classifier in Python is to use the iris features to train an svm classifier and use the trained svm model to predict the Iris species type. To begin with let’s try to load the Iris dataset.
"""


# importing datasets from scikit learn library
from sklearn import datasets

# importing Support Vector Classifier from scikit-learn's Support Vector Machines
from sklearn.svm import SVC

# getting train test split method 
from sklearn.model_selection import train_test_split

# getting pandas as pd 
import pandas as pd

# getting the iris dataset
data = datasets.load_iris()

# Extracting features from dataset
features = pd.DataFrame(data['data'], columns = data['feature_names']).values

# Extracting labels from dataset
labels = pd.DataFrame(data['target']).values

# splitting the features and labels
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.20, random_state = 0)

# Creating an instance of Support Vector Classifier with kernel function -> 'Gaussian RBF'
rbf = SVC(kernel = 'rbf', random_state = 0)

# Training the model
rbf.fit(features_train, labels_train)

# getting predictions for test data
labels_pred = rbf.predict(features_test)

# checking the score for training and testing data
print(rbf.score(features_train, labels_train))
print(rbf.score(features_test, labels_test))