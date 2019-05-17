# -*- coding: utf-8 -*-
"""
Created on Fri May 17 13:46:02 2019

@author: Administrator
"""

# mysql to perform database operations
import mysql.connector

# bs4 for web scraping
from bs4 import BeautifulSoup

# requests to interact with browser
import requests

# to get page source code
source = requests.get('https://www.icc-cricket.com/rankings/mens/team-rankings/odi').text

# parsing the source using lxml parser
html_page = BeautifulSoup(source, 'lxml')

# some lists to store the data
Pos = []
Team_name = []
Weighted_matches = []
Points = []
Rating = []

# finding specific data table
table = html_page.find('table', class_ = 'table')

# finding all the tr(s)
for row in table.find_all('tr'):
    
    # finding al the td(s) in tr
    data = row.find_all('td')
    
    # getting specified tr which has 5 columns
    if len(data) == 5:
        
        # appending data to the list
        Pos.append(data[0].text.strip())
        Team_name.append(data[1].text.strip())
        Weighted_matches.append(data[2].text.strip())
        Points.append(data[3].text.strip())
        Rating.append(data[4].text.strip())

#  to connect to database
con = mysql.connector.connect(user = 'phpmyadmin', password = 'phpmyadmin', host = 'db4free.net', database = 'db4free_db')

# setting cursor to database
c = con.cursor()

# removing ',' from Points data and converting into integer
Points = [int(''.join(p.split(','))) if ',' in p else int(p) for p in Points]

# to create a table
c.execute("""CREATE TABLE Icc_data(
            Position INTEGER,
            Team_Name TEXT,
            Weighted_Matches INTEGER,
            Points INTEGER,
            Rating INTEGER
        )""") 

# length of Pos table to iterate 
length = len(Pos)

# inserting all data using for
for i in range(length):
    c.execute("INSERT INTO Icc_data VALUES ('{}', '{}', '{}', '{}', '{}')".format(int(Pos[i]), Team_name[i], int(Weighted_matches[i]), int(Points[i]), int(Rating[i])))

# commiting changes
con.commit()

# closing the connection from database
con.close()