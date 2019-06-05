"""
Code Challenge 01: (Prostate Dataset)
Load the dataset from given link: 
pd.read_csv("http://www.stat.cmu.edu/~ryantibs/statcomp/data/pros.dat")

This is the Prostate Cancer dataset. Perform the train test split before you apply the model.

(a) Can we predict lpsa from the other variables?
(1) Train the unregularized model (linear regressor) and calculate the mean squared error.
(2) Apply a regularized model now - Ridge regression and lasso as well and check the mean squared error.

(b) Can we predict whether lpsa is high or low, from other variables?
"""



import pandas as pd
from sklearn.linear_model import LinearRegression, Lasso, Ridge, ElasticNet, LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, confusion_matrix
from sklearn.metrics import accuracy_score, precision_score, recall_score, classification_report

data = pd.read_csv('http://www.stat.cmu.edu/~ryantibs/statcomp/data/pros.dat', delimiter = ' ')
# checking null values -> data.isnull().any(axis = 0)

features = data.drop('lpsa', axis = 1)
labels = data['lpsa']

sc = StandardScaler()
features = sc.fit_transform(features)

features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.20, random_state = 0)
lr = LinearRegression()
lr.fit(features_train, labels_train)

labels_pred = lr.predict(features_test)

print(mean_squared_error(labels_test, labels_pred))
print('10 % of Mean of labels :', labels.mean() / 10)

lr_lasso = Lasso()
lr_ridge = Ridge()
lr_en = ElasticNet()

lr_lasso.fit(features_train, labels_train)
lr_ridge.fit(features_train, labels_train)
lr_en.fit(features_train, labels_train)

labels_pred_lasso = lr_lasso.predict(features_test)
labels_pred_ridge = lr_ridge.predict(features_test)
labels_pred_en = lr_en.predict(features_test)

print('Mean Squared Error(Lasso) :', mean_squared_error(labels_test, labels_pred_lasso))

print('Mean Squared Error(Ridge) :', mean_squared_error(labels_test, labels_pred_ridge))

print('Mean Squared Error(Elastic Net) :', mean_squared_error(labels_test, labels_pred_en))

labels = data['lpsa'].apply(lambda x : 1 if data['lpsa'].mean() <= x else 0)

features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.20, random_state = 0)
classifier = LogisticRegression()
classifier.fit(features_train, labels_train)

clr_predict = classifier.predict(features_test)

cm = confusion_matrix(labels_test, clr_predict)
classifier.score(features_train, labels_train)

print(classification_report(labels_test, clr_predict))

