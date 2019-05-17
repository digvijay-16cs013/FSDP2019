# -*- coding: utf-8 -*-
"""
Created on Sat May 11 09:45:16 2019

@author: Administrator
"""

import hashlib

h = hashlib.sha1()

with open('code_files/new.txt', 'rb') as file:
    
    chunk = 0
    
    while chunk != b'':
        
        chunk = file.read(1024)
        
        h.update(chunk)
        
        
print(h.hexdigest())
