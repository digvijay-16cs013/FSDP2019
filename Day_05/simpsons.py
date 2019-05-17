# -*- coding: utf-8 -*-
"""
Created on Sat May 11 18:21:16 2019

@author: Administrator
"""

# import regular expression library
import re

# it will contain contact details
phone_book = []

# open file in read mode
with open('code_files/simpsons_phone_book.txt', 'r') as fp:
    
    # read all the lines and create a list
    data = fp.readlines()
    
    # create pattern
    pattern = re.compile(r'^J[^0-9]*Neu')
    
    # to get each row from list
    for contact in data:
        
        # check if patter matches
        if re.match(pattern, contact):
            
            # add contact to phone_book
            phone_book.append(contact.rstrip('\n'))
    
# to get each contact printed on screen        
for contact in phone_book:
    print(contact)