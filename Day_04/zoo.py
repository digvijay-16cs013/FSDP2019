# -*- coding: utf-8 -*-
"""
Created on Fri May 10 16:29:32 2019

@author: Administrator
"""

def zoo_data():
    with open('code_files/zoo.csv') as csv_file:
        data = csv_file.readlines()
        for line in data:
            print(line)
        


# group of animals
def list_of_animals():
    
    animals = {}
    
    with open('code_files/zoo.csv') as csv_file:
        
        next(csv_file)
        
        data = csv_file.readlines()
        
        for line in data:
            
            line = line.split(',')
            
            if line[0] not in animals:
                
                animals[line[0]] = [[int(line[1])], [int(line[2])]]
            
            else:
                
                animals[line[0]][0].append(int(line[1]))
                animals[line[0]][1].append(int(line[2].rstrip('\n')))
                
        print(animals)
            
                
    return animals





def individual_water_need():
    
    animals_water_need = {} 
    
    with open('code_files/zoo.csv') as csv_file:
        
        next(csv_file)
        
        data = csv_file.readlines()
        
        for line in data:
            
            line = line.split(',')
            
            if line[0] not in animals_water_need:
                
                animals_water_need[line[0]] = int(line[2])
                
            else:
                
                animals_water_need[line[0]] += int(line[2])
        
        for animal, water in animals_water_need.items():  
            
            print(animal, water)
            
  
def water_need():

    water = 0
    
    with open('code_files/zoo.csv') as csv_file:
        
        next(csv_file)
        
        data = csv_file.readlines()
        
        for line in data:
            
            line = line.split(',')
            
            water = water + int(line[2])
            
    return water
          
                
zoo_data()

group_animals = list_of_animals()

print(group_animals)

individual_water_need()  

total_water = water_need()

print('total water need :', total_water)