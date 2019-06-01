# -*- coding: utf-8 -*-
"""
Created on Wed May 22 22:15:02 2019

@author: Administrator
"""


# to get pandas abbreviated as pd
import pandas as pd

# loads titanic data from csv file
titanic_data = pd.read_csv('training_titanic.csv')

# calculates the number of people who survived and died
s_and_d = titanic_data['Survived'].value_counts()

# calculates the percentage of people who survived and died, here normalize is used to calculate the data in percentage
s_and_d_per = titanic_data['Survived'].value_counts(normalize = True)

# calculates the number of people who survived
print('Passengers survived :', s_and_d[1])

# calculates the number of people who died
print('Passengers died :', s_and_d[0])

# calculates the percentage of people who survived
print('Passengers survived :', s_and_d_per[1] * 1, ' %')

# calculates the percentage of people who died
print('Passengers died :', s_and_d_per[0], ' %')

# calculates the number of Male who survived
male_survived = titanic_data['Survived'][titanic_data['Sex'] == 'male'].value_counts(normalize = True)[1]
print('Male survived :', male_survived, ' %')

# calculates the number of Male who died
male_died = titanic_data['Survived'][titanic_data['Sex'] == 'male'].value_counts(normalize = True)[0]
print('Male died :',male_died , ' %')

# calculates the number of female who survived
female_survived = titanic_data['Survived'][titanic_data['Sex'] == 'female'].value_counts(normalize = True)[1]
print('Female survived :', female_survived, ' %')

# calculates the number of female who died
female_died = titanic_data['Survived'][titanic_data['Sex'] == 'female'].value_counts(normalize = True)[0]
print('Female died :', female_died,' %')

# Replaces the "NaN" values in "Age" column with Mean of values in "Age" column
titanic_data['Age'] = titanic_data['Age'].fillna(titanic_data['Age'].mean())

# creates a new "Child" column and setting it's values(for age >= 18 value will be 0, otherwise 1)
titanic_data['Child'] = titanic_data['Age'].map(lambda x : 1 if x < 18 else 0)

#  calculates the survival rate of adult and child
sur_rate = titanic_data['Child'][titanic_data['Survived'] == 1].value_counts(normalize = True)

# survival rate of Child
child_sur = sur_rate[1]
print('Child survived :', child_sur, ' %')

# survival rate of older persons
older_sur = sur_rate[0]
print('Older survived :', older_sur, ' %')
