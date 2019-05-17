# -*- coding: utf-8 -*-
"""
Created on Mon May 13 18:43:03 2019

@author: Administrator
"""

product_details = [[34587, 'Learning Python', 'Mark Lutz', 4, 40.95], [98762, 'Programming Python', 'Mark Lutz', 5, 56.80], [77226, 'Head First Python', 'Paul Barry', 3, 32.95], [88112, 'Einführung in Python3', 'Bernd Klein', 3, 24.99]]

price_item = list(map(lambda value : [value[0], value[-2] * value[-1]], product_details))

print(price_item)

product_details = list(map(lambda value : (value[0], value[1] + 10) if value[1] < 100 else tuple(value), price_item))

print(product_details)