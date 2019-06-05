# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 17:25:17 2019

@author: Administrator
"""

"""
Code Challenge:
Datset: Market_Basket_Optimization.csv
Q2. In today's demo sesssion, we did not handle the null values before fitting the data to model, remove the null values from each row and perform the associations once again.
Also draw the bar chart of top 10 edibles.
"""

# Importing some libraries and apriori algorithm(which is downloaded from Google)
import pandas as pd, numpy as np
from apyori import apriori
import matplotlib.pyplot as plt

# laoding the data into dataframe
data = pd.read_csv('Market_Basket_Optimisation.csv', header = None).values

# to get the transactions form data in list of lists format
def get_transactions(data):
    transactions = []
    for i in range(data.shape[0]):
        transactions.append([data[i, j] for j in range(data.shape[1]) if str(data[i, j]) != str(np.nan)])
    return transactions

# storing the transactions
transactions = get_transactions(data)

# using apriori algorithm
assoc_gen = apriori(transactions, min_support = 0.003, min_confidence = 0.25, min_lift = 4)

# creating list of assoc_gen generator
association = list(assoc_gen)

# to show data(associated items, support, confidence, lift) from association
def show_assoc(association):
    for item in (association):
        item_data = item[0]
        items = [i for i in item_data]
        print('Items Associated :', items[0], '->', items[1])
        print('Support :', item[1])
        print('Confidence :', item[2][0][2])
        print('Lift :', item[2][0][3])
        print('========================================')

# calling show_assoc to show data        
show_assoc(association)

# to show top 10 edibles
def show_bar(data):
    top_10_edibles = pd.Series(data.flatten()).value_counts().head(10)
    plt.bar(top_10_edibles.index, top_10_edibles.values, width = 0.50, color = 'green')
    plt.title('Top 10 Edibles')
    plt.xlabel('Edibles')
    plt.xticks(rotation = 'vertical')
    plt.ylabel('Popularity')
    plt.show()

# to plot bar chart of top 10 edibles
show_bar(data)
    
    