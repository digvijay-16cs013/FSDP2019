# -*- coding: utf-8 -*-
"""
Created on Sat May 11 17:50:40 2019

@author: Administrator
"""

# to import specific methods from regular expression module
from re import search, match

# get card number from user
card_number = input('Enter your credit card number : ')

# to match pattern
pattern = match(r'^[456]{1}[0-9]{3}-?[0-9]{4}-?[0-9]{4}-?[0-9]{4}$', card_number)

# to search if 4 repetitive digits occur
rep_digits = search(r'(\d)\1{3,}', card_number.replace('-', ''))

# to check if pattern is correct and does not cantain four repetitive digits
if pattern and not rep_digits:
    print('Valid')
    
#if pattern is incorrect
else:
    print('Invalid')