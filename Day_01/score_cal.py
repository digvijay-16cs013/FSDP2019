# -*- coding: utf-8 -*-
"""
Created on Tue May  7 16:45:34 2019

@author: Administrator
"""

# Scores of three assignments

assignment_1 = int(input('Enter marks assignment number 1 : '))
assignment_2 = int(input('Enter marks of assignment number 2 : '))
assignment_3 = int(input('Enter marks of assignment number 3 : '))

# Scores of two exams 

exam_1 = int(input('Enter marks of exam 1 : '))
exam_2 = int(input('Enter marks of exam 2 : '))

# Weighted score

weighted_score = (assignment_1 + assignment_2 + assignment_3) * .1 + (exam_1 + exam_2) * .35

# Printing results

print('Your weighted score is :', weighted_score)