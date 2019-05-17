# -*- coding: utf-8 -*-
"""
Created on Mon May 13 17:18:35 2019

@author: Administrator
"""

names = ['Mary', 'Isla', 'Sam']
hash_values = list(map(lambda name : hash(name), names))
print(hash_values)
