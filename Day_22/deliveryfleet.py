# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 08:07:08 2019

@author: Administrator
"""

""" Q1. (Create a program that fulfills the following specification.)
deliveryfleet.csv


Import deliveryfleet.csv file

Here we need Two driver features: mean distance driven per day (Distance_feature) and the mean percentage of time a driver was >5 mph over the speed limit (speeding_feature).

    Perform K-means clustering to distinguish urban drivers and rural drivers.
    Perform K-means clustering again to further distinguish speeding drivers from those who follow speed limits, in addition to the rural vs. urban division.
    Label accordingly for the 4 groups.
"""

# Importing KMeans from scikit-learn's cluster module
from sklearn.cluster import KMeans

# Importing matplotlib.pyplot  as plt for visualuzation
import matplotlib.pyplot as plt

# Importing pandas as pd
import pandas as pd

# Loading data from csv file 
data = pd.read_csv('deliveryfleet.csv')

# Extracting and visualizing features 
features = data.drop('Driver_ID', axis = 1).values
plt.scatter(features[:, 0], features[:, 1])
plt.show()

# Creating an empty list wcss(Within )
wcss = []

# getting wcss for each value of clusters to identify exactly how many clusters are required
for i in range(1, 11):
    
    # creating instancw of KMeans
    kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 0)
    
    # creating our cluster
    cluster = kmeans.fit(features)
    
    # apending inertia of cluster in wcss
    wcss.append(cluster.inertia_)

# plotting wcss
plt.plot(range(1, 11), wcss)

# by using elbow method in visualization we get that their are only 2 clusters
kmeans = KMeans(n_clusters = 2, init = 'k-means++', random_state = 0)

# getting cluster for features
clusters = kmeans.fit_predict(features)

# plotting clusters
plt.scatter(features[clusters == 0, 0], features[clusters == 0, 1], color = 'm', label = 'Rural')
plt.scatter(features[clusters == 1, 0], features[clusters == 1, 1], color = 'blue', label = 'Urban')
plt.title('Rural v/s Urban')
plt.xlabel('Distance-Feature')
plt.ylabel('Speeding-Feature')
plt.legend()
plt.show()

# using 4 clusters
kmeans = KMeans(n_clusters = 4, init = 'k-means++', random_state = 0)

# clustering features into 4 clusters
clusters_speed = kmeans.fit_predict(features)

# visualizing clusters
plt.scatter(features[clusters_speed == 0, 0], features[clusters_speed == 0, 1], c = 'magenta', label = 'Cluster 1')
plt.scatter(features[clusters_speed == 1, 0], features[clusters_speed == 1, 1], c = 'red', label = 'Cluster 2')
plt.scatter(features[clusters_speed == 2, 0], features[clusters_speed == 2, 1], c = 'blue', label = 'Cluster 3')
plt.scatter(features[clusters_speed == 3, 0], features[clusters_speed == 3, 1], c = 'violet', label = 'Cluster 4')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c = 'yellow', label = 'Centroid')
plt.title('Speeding drivers (Rural v/s Urban)')
plt.xlabel('Distance-Feature')
plt.ylabel('Speeding-Feature')
plt.legend()
plt.show()
