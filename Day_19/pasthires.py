
"""
Q1. (Create a program that fulfills the following specification.)
PastHires.csv


Here, we are building a decision tree to check if a person is hired or not based on certain predictors.

Import PastHires.csv File.

scikit-learn needs everything to be numerical for decision trees to work.

So, use any technique to map Y,N to 1,0 and levels of education to some scale of 0-2.

    Build and perform Decision tree based on the predictors and see how accurate your prediction is for a being hired.

Now use a random forest of 10 decision trees to predict employment of specific candidate profiles:

    Predict employment of a currently employed 10-year veteran, previous employers 4, went to top-tire school, having Bachelor's Degree without Internship.
    Predict employment of an unemployed 10-year veteran, ,previous employers 4, didn't went to any top-tire school, having Master's Degree with Internship.

"""



from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder 
import pandas as pd, numpy as np

dataset = pd.read_csv('PastHires.csv')

features = dataset.drop('Hired', axis = 1)
labels = dataset['Hired']

le = LabelEncoder()
features.iloc[:, 1] = le.fit_transform(features.iloc[:, 1])
features.iloc[:, 4] = le.transform(features.iloc[:, 4])
features.iloc[:, 5] = le.transform(features.iloc[:, 5])



labels = le.transform(labels)

features.iloc[:, 3] = le.fit_transform(features.iloc[:, 3])

dtc = DecisionTreeClassifier()
dtc.fit(features, labels)

print(dtc.score(features, labels))

rfc = RandomForestClassifier(n_estimators = 10, random_state = 0)
rfc.fit(features, labels)
print(rfc.score(features, labels))

emp1 = np.array([10, 1, 4, 0, 1, 0]).reshape(1, -1)
print(dtc.predict(emp1))

emp2 = np.array([10, 0, 4, 1, 0, 1]).reshape(1, -1)
print(rfc.predict(emp2))
