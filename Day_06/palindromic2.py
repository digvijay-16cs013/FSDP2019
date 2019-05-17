# -*- coding: utf-8 -*-
"""
Created on Mon May 13 15:55:49 2019

@author: Administrator
"""
# palindrome checker
#def palindromic(num):
#    
#    reverse = 0
#    
#    val = num
#     
#    while num > 0:
#        
#        rem = num % 10
#        
#        reverse = reverse * 10 + rem
#        
#        num /= 10
#        
#    if val == reverse:
#        return True
#    else:
#        return False

numbers = input('Enter space separated numbers : ').split()

positive_numbers = [int(value) >= 0 for value in numbers]

palindrome_numbers = [True if value == value[::-1] else False for value in numbers]

if any(palindrome_numbers) and all(positive_numbers):
    print(True)
else:
    print(True)
    