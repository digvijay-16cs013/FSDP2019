# -*- coding: utf-8 -*-
"""
Created on Wed May  8 15:46:33 2019

@author: Administrator
"""
# states name
state_name = ['Alabama', 'California', 'Oklahoma', 'Florida']

# list of vowels
vowels = ['a', 'e', 'i', 'o', 'u']

# new list will contain states name without vowels
new_list = []

# loop to get individual state
for state in state_name:
    
    # temp list wiil contain letter name of state without vowel
    temp = []
    
    # to get each letter of state
    for letter in state:
        
        # letter of state which is not vowel
        if letter.lower() not in vowels:
            
            # append consonant to list temp
            temp.append(letter)
     
    # combining state name without vowel
    state_without_vowel = ''.join(temp)
    
    # storing state name to new_list
    new_list.append(state_without_vowel)

# Printing list of state names with no vowel  
print(new_list)