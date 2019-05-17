# -*- coding: utf-8 -*-
"""
Created on Fri May 10 17:46:27 2019

@author: Administrator
"""

file_name = input('Enter file name : ') + '.txt'

with open('code_files/' + file_name) as fp:

    data = fp.readlines()
    
    print(data[-1])