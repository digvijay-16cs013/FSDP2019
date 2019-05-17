# -*- coding: utf-8 -*-
"""
Created on Tue May  7 16:30:47 2019

@author: Administrator
"""

# distance travelled in a day
distance = float(input('Enter the distance travelled in a day : '))

# cost of deisel per litre in ruppees
cost_deisel_per_litre = float(input('Enter cost of deisel per litre in ruppees : '))

# fuel average of vehicle
fuel_avg_vehicle = float(input('Enter fuel average per litre : '))

# cost per day
cost_per_day = (distance / fuel_avg_vehicle) * cost_deisel_per_litre

# Printing cost
print('Cost per day :', round(cost_per_day))


