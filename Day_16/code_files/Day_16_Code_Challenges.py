

"""
Code Challenge: Simple Linear Regression
  Name: 
    Food Truck Profit Prediction Tool
  Filename: 
    Foodtruck.py
  Dataset:
    Foodtruck.csv
  Problem Statement:
    Suppose you are the CEO of a restaurant franchise and are considering 
    different cities for opening a new outlet. 
    
    The chain already has food-trucks in various cities and you have data for profits 
    and populations from the cities. 
    
    You would like to use this data to help you select which city to expand to next.
    
    Perform Simple Linear regression to predict the profit based on the 
    population observed and visualize the result.
    
    Based on the above trained results, what will be your estimated profit, 
    
    If you set up your outlet in Jaipur? 
    (Current population in Jaipur is 3.073 million)
        
  Hint: 
    You will implement linear regression to predict the profits for a 
    food chain company.
    Foodtruck.csv contains the dataset for our linear regression problem. 
    The first column is the population of a city and the second column is the 
    profit of a food truck in that city. 
    A negative value for profit indicates a loss.
"""
import pandas as pd, numpy as np
from sklearn.linear_model import LinearRegression

df = pd.read_csv('Foodtruck.csv')

features = df.iloc[:, :-1].values
labels = df['Profit'].values

regressor = LinearRegression()
regressor.fit(features, labels)

Jaipur = np.array(3.073).reshape(1, 1)
print(regressor.predict(Jaipur)[0])

"""
Code Challenge: Simple Linear Regression

  Name: 
    Box Office Collection Prediction Tool
  Filename: 
    Bahubali2vsDangal.py
  Dataset:
    Bahubali2vsDangal.csv
  Problem Statement:
    It contains Data of Day wise collections of the movies Bahubali 2 and Dangal 
    (in crores) for the first 9 days.
    
    Now, you have to write a python code to predict which movie would collect 
    more on the 10th day.
  Hint:
    First Approach - Create two models, one for Bahubali and another for Dangal
    Second Approach - Create one model with two labels
"""

import pandas as pd, numpy as np
from sklearn.linear_model import LinearRegression

df = pd.read_csv('Bahubali2_vs_Dangal.csv')

regressor = LinearRegression()
features = df.iloc[:, :1].values
labels = df.iloc[:, 1:].values

regressor.fit(features, labels)

day = np.array(10).reshape(1, 1)
day_10_pred = regressor.predict(day)
print('Bahubali2 :', day_10_pred[0][0])
print('Dangal :', day_10_pred[0][1])





