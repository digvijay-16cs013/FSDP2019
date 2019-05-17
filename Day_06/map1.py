# -*- coding: utf-8 -*-
"""
Created on Mon May 13 17:04:37 2019

@author: Administrator
"""

import random

names = ['Mary', 'Isla', 'Sam']
code_names = ['Mr. Pink', 'Mr. Orange', 'Mr.  Blonde']

assigned_names = []

names = list(map(lambda n : code_names.pop(random.randint(0, n)), [2, 1, 0]))

print(names)