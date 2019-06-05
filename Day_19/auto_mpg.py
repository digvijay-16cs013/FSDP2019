"""
Q1. (Create a program that fulfills the following specification.)
Auto_mpg.txt

Here is the dataset about cars. The data concerns city-cycle fuel consumption in miles per gallon (MPG).

    Import the dataset Auto_mpg.txt
    Give the column names as "mpg", "cylinders", "displacement","horsepower","weight","acceleration", "model year", "origin", "car name" respectively
    Display the Car Name with highest miles per gallon value
    Build the Decision Tree and Random Forest models and find out which of the two is more accurate in predicting the MPG value
    Find out the MPG value of a 80's model car of origin 3, weighing 2630 kgs with 6 cylinders, having acceleration around 22.2 m/s due to it's 100 horsepower engine giving it a displacement of about 215. (Give the prediction from both the models)




"""



from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
import pandas as pd, numpy as np

dataset = pd.read_csv('Auto_mpg.txt', delimiter = '\s+', header = None, names = ["mpg", "cylinders", "displacement","horsepower","weight","acceleration", "model year", "origin", "car name"])
car_high_mpg = dataset.loc[dataset['mpg'].argmax(), ['car name']].values
print('Highest Milaege Car :', car_high_mpg[0])

# to check if null values present
# print(dataset.isnull().any(axis = 0))

features = dataset.drop(['mpg', 'car name'], axis = 1)
features["horsepower"] = features["horsepower"].replace("?",np.nan).astype(np.float64)
features["horsepower"] = features["horsepower"].fillna(features["horsepower"].mean())


labels = dataset['mpg'].values

sc = StandardScaler()
features = sc.fit_transform(features)

features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.20, random_state = 0)

dtr = DecisionTreeRegressor()
dtr.fit(features_train, labels_train)

lab_dtr_pred = dtr.predict(features_test)
print(pd.DataFrame(labels_test, lab_dtr_pred))
dtr.score(features_train, labels_train)
dtr.score(features_test, labels_test)

rfr = RandomForestRegressor(n_estimators = 20, random_state = 0)
rfr.fit(features_train, labels_train)

lab_rfr_pred = rfr.predict(features_test)
print(pd.DataFrame(labels_test, lab_rfr_pred))
print(rfr.score(features_train, labels_train))
print(rfr.score(features_test, labels_test))

# Car Name does not play any important role
values = sc.transform(np.array([ 6, 215, 100, 2630, 22.2, 80, 3]).reshape(1, -1))
dtr.predict(values)
rfr.predict(values)