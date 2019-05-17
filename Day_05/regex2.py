# -*- coding: utf-8 -*-
"""
Created on Sat May 11 16:02:49 2019

@author: Administrator
"""

# to import regular expression module
import re

# it will contain all the valid emails
emails = []

# create pattern to search
pattern = re.compile(r'^[\w_-]+@\w+\.[a-zA-Z]{2,4}$')
# this can also be used
# pattern = re.compile(r'^[0-9A-Za-z_-]+@[a-zA-Z0-9]+\.[a-z]{2,4}$')


# loop to get email one by one
while True:
    
    # get email from user
    email = input('Enter email address : ')
    
    # if email is not provided then get out of the loop
    if not email:
        break
    
    # if email provided then check if it is valid
    elif re.match(pattern, email):
        # if valid then add it to emails list
        emails.append(email)
        
        
# finally print list of emails in sorted order
print(sorted(emails))