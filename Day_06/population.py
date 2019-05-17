# -*- coding: utf-8 -*-
"""
Created on Tue May 14 14:09:15 2019

@author: Administrator
"""

import csv

# to open csv file in read mode
with open('population.csv') as csv_file:
    
    # to avoid first line
    next(csv_file)
    
    # setting csv reader on file
    csv_reader = csv.reader(csv_file, delimiter = ',')
    
    # converting all the rows in list
    data = list(csv_reader)

# to initialize all state's population to zero initially
population_of_states = {x : [] for x in set([state[-1] for state in data])}

# to get population of each state as list in dictionary where key is state name
list(map(lambda row: population_of_states[row[-1]].append(int(''.join(row[-2].split(',')))), data))


# print(population_of_states)

# convert the population data in the list of dictionary
population_by_states = [{'key' : state, 'value' : sum(population)} for state, population in population_of_states.items()]

# to get the data on console
print(population_by_states)