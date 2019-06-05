# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 08:07:58 2019

@author: Administrator
"""

"""
Q1. (Create a program that fulfills the following specification.)
tshirts.csv


T-Shirt Factory:

You own a clothing factory. You know how to make a T-shirt given the height and weight of a customer.

You want to standardize the production on three sizes: small, medium, and large. How would you figure out the actual size of these 3 types of shirt to better fit your customers?

Import the tshirts.csv file and perform Clustering on it to make sense out of the data as stated above.
"""


# Importing KMeans from scikit-learn's cluster module
from sklearn.cluster import KMeans

# Importing some important libraries
import pandas as pd
import matplotlib.pyplot as plt

# Getting the data into a dataframe using csv file
data = pd.read_csv('tshirts.csv')

# Extracting features
features = data.drop('name', axis = 1).values

# visualizing features
plt.scatter(features[:, 0], features[:, 1])

# creating an instance of KMeans
kmeans = KMeans(n_clusters = 3, init = 'k-means++', random_state = 0)

# clustering our features into clusters
clusters = kmeans.fit_predict(features)

# visualizing clusters
plt.scatter(features[clusters == 0, 0], features[clusters == 0, 1], color = 'green', label = 'Cluster 1')

plt.scatter(features[clusters == 1, 0], features[clusters == 1, 1], color = 'blue', label = 'Cluster 2')

plt.scatter(features[clusters == 2, 0], features[clusters == 2, 1], color = 'magenta', label = 'Cluster 3')

plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], color = 'yellow', label = 'Centroid')

plt.title('Size of t-shirts')

plt.xlabel('Height (inches)')

plt.ylabel('Weight (pounds)')

plt.legend()

plt.show()

