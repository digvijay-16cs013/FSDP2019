# -*- coding: utf-8 -*-
"""
Created on Tue May  7 18:13:56 2019

@author: Administrator
"""

i = 1

# While loop to iterate
while i <= 100:
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)
    i += 1