# -*- coding: utf-8 -*-
"""
Created on Fri May 10 17:31:20 2019

@author: Administrator
"""

with open('code_files/romeo.txt') as fp:
    
    word_freq = {}
    
    data = fp.readlines()
    
    for line in data:
        
        line = line.split()
        
        for word in line:
            
            if word not in word_freq:
                
                word_freq[word] = 1
            else:
                
                word_freq[word] += 1
    
    for word, freq in word_freq.items():
        
        print(word, freq)