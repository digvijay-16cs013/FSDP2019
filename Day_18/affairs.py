# -*- coding: utf-8 -*-
"""
Created on Thu May 30 13:56:34 2019

@author: Administrator
"""

"""


Q1. (Create a program that fulfills the following specification.)
affairs.csv


Import the affairs.csv file.

It was derived from a survey of women in 1974 by Redbook magazine, in which married women were asked about their participation in extramarital affairs.

Description of Variables

The dataset contains 6366 observations of 10 variables:(modified and cleaned)

rate_marriage: woman's rating of her marriage (1 = very poor, 5 = very good)

age: women's age

yrs_married: number of years married

children: number of children

religious: women's rating of how religious she is (1 = not religious, 4 = strongly religious)

educ: level of education (9 = grade school, 12 = high school, 14 = some college, 16 = college graduate, 17 = some graduate school, 20 = advanced degree)

occupation: women's occupation (1 = student, 2 = farming/semi-skilled/unskilled, 3 = "white collar", 4 = teacher/nurse/writer/technician/skilled, 5 = managerial/business, 6 = professional with advanced degree)

occupation_husb: husband's occupation (same coding as above)

affair: outcome 0/1, where 1 means a woman had at least 1 affair.

    Now, perform Classification using logistic regression and check your model accuracy using confusion matrix and also through .score() function.

NOTE: Perform OneHotEncoding for occupation and occupation_husb, since they should be treated as categorical variables. Careful from dummy variable trap for both!!

    What percentage of total women actually had an affair?

(note that Increases in marriage rating and religiousness correspond to a decrease in the likelihood of having an affair.)

    Predict the probability of an affair for a random woman not present in the dataset. She's a 25-year-old teacher who graduated college, has been married for 3 years, has 1 child, rates herself as strongly religious, rates her marriage as fair, and her husband is a farmer.

Optional

    Build an optimum model, observe all the coefficients.

"""
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LogisticRegression
import pandas as pd, numpy as np
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier 

data = pd.read_csv('affairs.csv')

features = data.iloc[:, :-1].values
labels = data.iloc[:, -1].values

ohencoder = OneHotEncoder(categorical_features = [6, 7])
features = ohencoder.fit_transform(features).toarray()

features = features[:, 1:]
features = np.delete(features, 5, axis = 1)

features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.20, random_state = 0)


classifier = LogisticRegression()
classifier.fit(features_train, labels_train)

classifier.score(features_train, labels_train)
classifier.score(features_test, labels_test)

labels_pred = classifier.predict(features_test)

df = pd.DataFrame(labels_test, labels_pred)

cm = confusion_matrix(labels_test, labels_pred)


per_woman = data['affair'].value_counts()[1] / data['affair'].size * 100

random_woman = ohencoder.transform(np.array([3, 25, 3, 1, 4, 16, 4, 2]).reshape(1, -1)).toarray()
random_woman = np.delete(random_woman, [0, 5], axis = 1)

classifier.predict(random_woman) 

KNN_Classifier = KNeighborsClassifier(n_neighbors = 5, p = 2)
KNN_Classifier.fit(features_train, labels_train)
KNN_pred = KNN_Classifier.predict(features_test)

KNN_Classifier.score(features_train, labels_train)
KNN_Classifier.score(features_test, labels_test)
