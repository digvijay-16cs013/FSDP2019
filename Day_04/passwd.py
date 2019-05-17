# -*- coding: utf-8 -*-
"""
Created on Fri May 10 22:13:04 2019

@author: Administrator
"""

user = {}

# open passwd file in read mode
with open('code_files/passwd') as fp:
    
    # to read all the line from file one by one
    for row in fp:
        
        # to ignore data which starts with an "_"
        if row[0] != '#':
            
            # to get individual data by splitting each line by ":"
            sep_data = row.split(':')
            
            # add User Name and ID to dictionary
            user[sep_data[0]] = sep_data[2]
        
# to print User Name and ID in alphabetical order        
for k in sorted(user.keys()):
    
    print(k, user[k])
        
        
        
        