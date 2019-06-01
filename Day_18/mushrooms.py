# -*- coding: utf-8 -*-
"""
Created on Thu May 30 13:58:18 2019

@author: Administrator
"""

"""
Q2. (Create a program that fulfills the following specification.)
mushrooms.csv

Import mushrooms.csv file

This dataset includes descriptions of hypothetical samples corresponding to 23 species of gilled mushrooms in the Agaricus and Lepiota Family Mushroom drawn from The Audubon Society Field Guide to North American Mushrooms (1981). Each species is identified as definitely edible, definitely poisonous, or of unknown edibility and not recommended. This latter class was combined with the poisonous one.

 

Attribute Information:

classes: edible=e, poisonous=p (outcome)

cap-shape: bell=b,conical=c,convex=x,flat=f, knobbed=k,sunken=s

cap-surface: fibrous=f,grooves=g,scaly=y,smooth=s

cap-color: brown=n, buff=b,cinnamon=c,gray=g,green=r,pink=p,purple=u,red=e,white=w,yellow=y

 

bruises: bruises=t, no=f

 

odor: almond=a,anise=l,creosote=c,fishy=y,foul=f,musty=m,none=n,pungent=p,spicy=s

 

gill-attachment: attached=a,descending=d,free=f,notched=n

 

gill-spacing: close=c,crowded=w,distant=d

 

gill-size: broad=b,narrow=n\

 

gill-color: black=k,brown=n,buff=b,chocolate=h,gray=g,

green=r,orange=o,pink=p,purple=u,red=e,white=w,yellow=y

 

stalk-shape: enlarging=e,tapering=t

 

stalk-root: bulbous=b,club=c,cup=u,equal=e,rhizomorphs=z,rooted=r,missing=?

 

stalk-surface-above-ring: fibrous=f,scaly=y,silky=k,smooth=s

 

stalk-surface-below-ring: fibrous=f,scaly=y,silky=k,smooth=s

 

stalk-color-above-ring: brown=n,buff=b,cinnamon=c,gray=g,orange=o,pink=p,red=e,white=w,yellow=y

 

stalk-color-below-ring: brown=n,buff=b,cinnamon=c,gray=g,orange=o,pink=p,red=e,white=w,yellow=y

 

veil-type: partial=p,universal=u

 

veil-color: brown=n,orange=o,white=w,yellow=y

ring-number: none=n,one=o,two=t

 

ring-type: cobwebby=c,evanescent=e,flaring=f,large=l,none=n,pendant=p,sheathing=s,zone=z

 

spore-print-color: black=k,brown=n,buff=b,chocolate=h,green=r,orange=o,purple=u,white=w,yellow=y

 

population: abundant=a,clustered=c,numerous=n,scattered=s,several=v,solitary=y

 

habitat: grasses=g,leaves=l,meadows=m,paths=p,urban=u,waste=w,woods=d

    Perform Classification on the given dataset to predict if the mushroom is edible or poisonous w.r.t. it’s different attributes.

(you can perform on habitat, population and odor as the predictors)

    Check accuracy of the model.


"""
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
import pandas as pd, numpy as np
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

data = pd.read_csv('mushrooms.csv')
features = data.iloc[:, [5, 21, 22]].values
labels = data.iloc[:, 0].values

le1 = LabelEncoder()
features[:, 0] = le1.fit_transform(features[:, 0])
features[:, 1] = le1.fit_transform(features[:, 1])
features[:, 2] = le1.fit_transform(features[:, 2])
labels = le1.fit_transform(labels)


ohe = OneHotEncoder(categorical_features = [0, 1, 2])
features = ohe.fit_transform(features).toarray()


features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.20, random_state = 0)

classifier = LogisticRegression()
classifier.fit(features_train, labels_train)
classifier.score(features_train, labels_train)
classifier.score(features_test, labels_test)
labels_pred = classifier.predict(features_test)


cm = confusion_matrix(labels_test, labels_pred)

KNN_Classifier = KNeighborsClassifier(n_neighbors = 5, p = 2)
KNN_Classifier.fit(features_train, labels_train)

KNN_pred = KNN_Classifier.predict(features_test)

KNN_Classifier.score(features_train, labels_train)
KNN_Classifier.score(features_test, labels_test)
