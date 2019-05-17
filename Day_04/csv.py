# -*- coding: utf-8 -*-
"""
Created on Sat May 11 08:56:48 2019

@author: Administrator
"""

import csv

# open passwd file
with open('code_files/passwd') as csv_file:
    
    # to read csv file content
    csv_reader = csv.reader(csv_file, delimiter = ':')
    
    # open new file to write data
    with open('user_data.txt', 'w') as fp:
        
        # to read individual line
        for line in csv_reader:
            
            # to check if not commented line
            if line[2]:
                    
                # to write data to another file
                fp.write(line[0] + '\t' + line[2] + '\n')