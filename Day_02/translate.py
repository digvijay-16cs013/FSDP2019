# -*- coding: utf-8 -*-
"""
Created on Thu May  9 08:17:02 2019

@author: Administrator
"""

def translate(string):
    vowels = 'aeiou'
    consonant = []
    swedish_string = ''
    
    # Consonant generator
    for asciii in range(97, 123):
        letter = chr(asciii)
        if letter not in vowels:
            consonant.append(letter)
            
    for letter in string:
        if letter.lower() in consonant:
            swedish_string = swedish_string + letter + 'o' + letter
        else:
            swedish_string = swedish_string + letter
    
    print(swedish_string)
    
string = input('Enter any string => ')
translate(string)