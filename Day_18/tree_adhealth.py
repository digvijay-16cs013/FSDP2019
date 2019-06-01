# -*- coding: utf-8 -*-
"""
Created on Thu May 30 13:59:41 2019

@author: Administrator
"""

"""
*****
Classification Code Challenge
*****

tree_addhealth.csv

Q1. (Create a program that fulfills the following specification.)

For this Code Challenge, The National Longitudinal Study of Adolescent to Adult Health (Add Health) data set, an ongoing (longitudinal) survey study that began in the mid-1990s is used. The project website URL is:

http://www.cpc.unc.edu/projects/addhealth/.

This large data set is available online from the University of North Carolina’s Carolina Population Center, http://www.cpc.unc.edu/projects/addhealth/data.

 

Import tree_addhealth.csv

 

The attributes are:

 

#BIO_SEX: 1 = male 0 = female    

#HISPANIC: 1=Yes,0=No    

#WHITE : 1=Yes,0=No

#BLACK : 1=Yes,0=No          

#NAMERICAN: 1=Yes,0=No                      

#ASIAN: 1=Yes,0=No                      

#ALCEVR1: ever drank alcohol(1=Yes,0=No)   

#marever1: ever smoked marijuana(1=Yes,0=No)    

#cocever1: ever used cocaine(1=Yes,0=No)                

#inhever1: ever used inhalants(1=Yes,0=No)             

#cigavail: cigarettes available in home(1=Yes,0=No)

PASSIST: parents or public assistance(1=Yes,0=No)

EXPEL1: ever expelled from school(1=Yes,0=No)

-> TREG1: Ever smoked regularly(1=Yes,0=No)

Explanatory Variables:

#Age

#ALCPROBS1:alcohol problems 0-6

#DEP1: depression scale

#ESTEEM1: self esteem scale       

VIOL1:violent behaviour scale

DEVIANT1: deviant behaviour scale     

SCHCONN1: school connectedness scale       

GPA1: gpa scale  4 points)

FAMCONCT: family connectedness scale       

PARACTV:parent activities scale

PARPRES:parental presence scale

 

    Build a classification tree model evaluating if an adolescent would smoke regularly or not based on: gender, age, (race/ethnicity) Hispanic, White, Black, Native American and Asian, alcohol use, alcohol problems, marijuana use, cocaine use, inhalant use, availability of cigarettes in the home, depression, and self-esteem.

    Build a classification tree model evaluation if an adolescent gets expelled or not from school based on their Gender and violent behavior.
    Use random forest in relation to regular smokers as a target and explanatory variable specifically with Hispanic, White, Black, Native American and Asian.

(Please make confusion matrix and also check accuracy score for each and every section)

"""


import pandas as pd, numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.neighbors import KNeighborsClassifier

data = pd.read_csv('tree_addhealth.csv')
print(data.isnull().any(axis = 0))
# null_values_data = data[data['age'].isnull() | data['ESTEEM1'].isnull() | data['VIOL1'].isnull()]
data = data.fillna(data.mean())

# Part 1:-
features = data.loc[:, ['BIO_SEX', 'HISPANIC', 'WHITE', 'BLACK', 'NAMERICAN', 'ASIAN', 'age', 'ALCEVR1', 'marever1', 'cocever1', 'inhever1', 'cigavail', 'ALCPROBS1', 'DEP1', 'ESTEEM1']].values
labels = data.loc[:, ['TREG1']].values

features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.20, random_state = 0)

sc = StandardScaler()
features_train = sc.fit_transform(features_train)
features_test = sc.transform(features_test)

classifier = LogisticRegression()
classifier.fit(features_train, labels_train)

labels_pred = classifier.predict(features_test)
cm = confusion_matrix(labels_test, labels_pred)

classifier.score(features_train, labels_train)
classifier.score(features_test, labels_test)

# Part 2:-
feat = data.loc[:, ['BIO_SEX', 'VIOL1']].values
lab = np.array(list(map(lambda x : round(x[0]), data.loc[:, ['EXPEL1']].values)))


feat_train, feat_test, lab_train, lab_test = train_test_split(feat, lab, test_size = 0.20, random_state = 0)

classifier_2 = LogisticRegression()
classifier_2.fit(feat_train, lab_train)

lab_pred = classifier_2.predict(feat_test)
cm_2 = confusion_matrix(lab_test, lab_pred)
print(classifier_2.score(feat_train, lab_train))
print(classifier_2.score(feat_test, lab_test))


# Using KNN (K Nearest Neighbors)
KNN_cl = KNeighborsClassifier(n_neighbors = 5, p = 2)
KNN_cl.fit(features_train, labels_train)

KNN_pred = KNN_cl.predict(features_test)

KNN_cl.score(features_train, labels_train)
KNN_cl.score(features_test, labels_test)
