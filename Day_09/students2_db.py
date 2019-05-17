# -*- coding: utf-8 -*-
"""
Created on Thu May 16 17:34:01 2019

@author: Administrator
"""

from pymongo import MongoClient

client = MongoClient("mongodb://root:mongodb@cluster0-shard-00-00-im8um.mongodb.net:27017,cluster0-shard-00-01-im8um.mongodb.net:27017,cluster0-shard-00-02-im8um.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")

my_db = client.student

def add_student(roll, name, age, branch):
    unique_val = my_db.students.find_one({'Roll_No' : roll})
    if unique_val:
        return 'Roll number already exists.'
    else:
        my_db.students.insert_one({
                'Roll_No' : roll,
                'Student_Name' : name,
                'Age' : age,
                'Branch' : branch
                 })

def fetch_values():
    data = my_db.students.find()
    for d in data:
        print(d)
        
add_student(1, 'Sourabh', 21, 'CSE')
add_student(2, 'Harshit', 22, 'CSE')
add_student(3, 'Digvijay', 21, 'CSE')
add_student(4, 'Tapan', 21, 'CSE')
add_student(5, 'Anupam', 22, 'CSE')

fetch_values()