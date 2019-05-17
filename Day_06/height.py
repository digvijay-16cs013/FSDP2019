# -*- coding: utf-8 -*-
"""
Created on Mon May 13 17:43:59 2019

@author: Administrator
"""

from functools import reduce

people = [{'name': 'Mary', 'height': 160},
          {'name': 'Isla', 'height': 80},
          {'name': 'Sam'}]

name_with_height = list(filter(lambda dc : 'height' in dc.keys(), people))

total_height = reduce(lambda p1, p2 : p1['height'] + p2['height'], name_with_height)

average_height = total_height / len(name_with_height)

print(average_height)