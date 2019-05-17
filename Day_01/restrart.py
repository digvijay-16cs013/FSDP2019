# -*- coding: utf-8 -*-
"""
Created on Tue May  7 17:29:34 2019

@author: Administrator
"""

r = 'RESTART'

# Reverse of 'RESTART'
r = r[::-1]

# Now the string is 'TRATSER'
# Replacing Initial 'R'
r = r.replace('R', '$', 1)

# Now the string is T$ARSER
# Printing reverse of it i.e. 'RESTA$T'
print(r[::-1])