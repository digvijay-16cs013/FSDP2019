# -*- coding: utf-8 -*-
"""
Created on Thu May 16 16:23:17 2019

@author: Administrator
"""
# sqlit3

import sqlite3, pandas as pd

con = sqlite3.connect('db_University')

c = con.cursor()

c.execute("""CREATE TABLE Students(
            Roll_no INTEGER,
            Student_Name TEXT,
            Student_Age INTEGER,
            Student_Branch TEXT
            )""")

c.execute('INSERT INTO Students VALUES(1, "Sourabh Prajapati", 21, "CSE")')
c.execute('INSERT INTO Students VALUES(2, "Harshit Goswami", 21, "CSE")')
c.execute('INSERT INTO Students VALUES(3, "Anupam Sharma", 22, "CSE")')
c.execute('INSERT INTO Students VALUES(4, "Tapan Vijayvergiya", 22, "CSE")')
c.execute('INSERT INTO Students VALUES(5, "Digvijay Singh", 21, "CSE")')

c.execute('SELECT * FROM Students')
df = pd.DataFrame(c.fetchall())
df.columns = ['Roll_No', 'Student_Name', 'Student_Age', 'Student_Branch']
print(df)

con.commit()
con.close()

# mongo db
from pymongo import MongoClient

client = MongoClient('localhost', 27017)

my_db = client.db_University

def add_student(roll, name, age, branch):
    unique_val = my_db.students.find_one({"Roll_No" : roll})
    if unique_val:
        print('Entry already exists...')
    else:
        my_db.students.insert({
                "Roll_No" : roll,
                "Student_Name" : name,
                "Age" : age,
                "Branch" : branch
                })

def all_values():
    data = my_db.students.find()
    for d in data:
        print(d)
        
add_student(1, 'Sourabh', 21, 'CSE')
add_student(2, 'Harshit', 22, 'CSE')
add_student(1, 'Digvijay', 21, 'CSE')
add_student(1, 'Tapan', 21, 'CSE')
add_student(1, 'Anupam', 22, 'CSE')

all_values()


# mysql database 
import mysql.connector, pandas as pd

con = mysql.connector.connect(user = 'root', password = '', host = 'localhost')

c = con.cursor()

c.execute('CREATE DATABASE Student;')

c.execute('USE Student;')


c.execute("""CREATE TABLE Students(
        Roll_No INTEGER,
        Student_Name TEXT,
        Age INTEGER,
        Branch TEXT
        )""")

c.execute('INSERT INTO Students VALUES(1, "Sourabh Prajapati", 21, "CSE")')
c.execute('INSERT INTO Students VALUES(2, "Harshit Goswami", 21, "CSE")')
c.execute('INSERT INTO Students VALUES(3, "Anupam Sharma", 22, "CSE")')
c.execute('INSERT INTO Students VALUES(4, "Tapan Vijayvergiya", 22, "CSE")')
c.execute('INSERT INTO Students VALUES(5, "Digvijay Singh", 21, "CSE")')

c.execute('SELECT * FROM Students')
df = pd.DataFrame(c.fetchall())
df.columns = ['Roll_No', 'Student_Name', 'Student_Age', 'Student_Branch']
print(df)


