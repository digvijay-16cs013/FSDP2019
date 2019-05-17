# -*- coding: utf-8 -*-
"""
Created on Tue May 14 08:55:41 2019

@author: Administrator
"""
#Without lambda map and reduce
#data =   [ [1, ("5464", 4, 9.99), ("8274",18,12.99), ("9744", 9, 44.95)], \
#           [2, ("5464", 9, 9.99), ("9744", 9, 44.95)], \
#           [3, ("5464", 9, 9.99), ("88112", 11, 24.99)], \
#           [4, ("8732", 7, 11.99), ("7733",11,18.99), ("88112", 5, 39.95)] ]
#print(data)
#
#product_data = []
#
#def add(order, i):
#    return order[i][1] * order[i][2]
#
#for row in data:
#    total_amount_order = 0
#    i = 1    
#    while i != len(row):
#        total_amount_order = total_amount_order + add(row, i)
#        i += 1
#    
#    product_data.append([row[0], total_amount_order])


# lambda expression
a = lambda x :[x[0], sum([x[i][1] * x[i][2] for i in range(1, len(x))])]

# data of shop
data =   [ [1, ("5464", 4, 9.99), ("8274",18,12.99), ("9744", 9, 44.95)], \
           [2, ("5464", 9, 9.99), ("9744", 9, 44.95)], \
           [3, ("5464", 9, 9.99), ("88112", 11, 24.99)], \
           [4, ("8732", 7, 11.99), ("7733",11,18.99), ("88112", 5, 39.95)] ]

# applying map to get the result
result = list(map(a, data))

# final result
print(result)