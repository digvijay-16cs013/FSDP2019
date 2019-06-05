# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 15:40:06 2019

@author: Administrator
"""

"""Code Challenge:
dataset: BreadBasket_DMS.csv

Q1. In this code challenge, you are given a dataset which has data and time wise transaction on a bakery retail store.
1. Draw the pie chart of top 15 selling items.
2. Find the associations of items where min support should be 0.0025, min_confidence=0.2, min_lift=3.
3. Out of given results sets, show only names of the associated item from given result row wise.
"""

# Importing apriori algorithm from downloaded file
from apyori import apriori

# Importing pandas and matplotlib
import pandas as pd, numpy as np
import matplotlib.pyplot as plt

# getting data from csv into a dataframe
data = pd.read_csv('BreadBasket_DMS.csv')

# Replacing 'NONE' value with 'nan' in the 'Item' column
data['Item'] = data['Item'].replace('NONE', np.nan)

# droping all the 'nan' contained rows from the dataframe
data = data.dropna()

# getting top 15 items
top_15_items = data['Item'].value_counts()[:15]

# setting explode for each of the 15 items
explode = np.zeros(15)

# updating explode to show most popular item apart in the pie chart
explode[0] = 0.2

# plotting the pie chart
plt.pie(top_15_items.values, explode = explode, labels = top_15_items.index, autopct = '%1.2f%%', radius= 1.8)
plt.show()

# getting the grouped data 
def cart(Items):
    return list(set(Items))

# getting transactions
transactions = data.groupby('Transaction')['Item'].apply(cart)

# using apriori algorithm
result = apriori(transactions, min_support = 0.0025, min_confidence = 0.2, min_lift = 3)

# getting data in the list
res = list(result)

# to get the associated data from apriori object
items_assoc = [list(res[i][0]) for i in range(len(res))]

# to show the associated data
print(items_assoc)