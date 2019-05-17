# -*- coding: utf-8 -*-
"""
Created on Wed May 15 16:59:09 2019

@author: Administrator
"""

from bs4 import BeautifulSoup
import requests, pandas as pd
from collections import OrderedDict
source = requests.get('https://www.icc-cricket.com/rankings/mens/team-rankings/odi').text

html_page = BeautifulSoup(source, 'lxml')

col_1 = []
col_2 = []
col_3 = []
col_4 = []
col_5 = []

table = html_page.find('table', class_ = 'table')
for row in table.find_all('tr'):
    data = row.find_all('td')
    if len(data) == 5:
        col_1.append(data[0].text.strip())
        col_2.append(data[1].text.strip())
        col_3.append(data[2].text.strip())
        col_4.append(data[3].text.strip())
        col_5.append(data[4].text.strip())

column_names = ['Pos', 'Team', 'Weighted Matches', 'Points', 'Rating']
df = pd.DataFrame(OrderedDict(zip(column_names, [col_1, col_2, col_3, col_4, col_5])))
print(df)

df.to_csv('Ranking_of_ODI_Men_team.csv', index = False)
