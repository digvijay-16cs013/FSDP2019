# -*- coding: utf-8 -*-
"""
Created on Fri May 10 15:48:37 2019

@author: Administrator
"""
#
#with open('code_files/romeo.txt', 'r') as fp1:
#    data = fp1.read()
#    with open('romeo3.txt', 'w') as fp2:
#        fp2.write(data)
#        fp2.flush()


with open('code_files/romeo.txt', 'r') as fp1:
    with open('romeo3.txt', 'w') as fp2:
        for line in fp1:
            fp2.write(line)
        