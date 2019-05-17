# -*- coding: utf-8 -*-
"""
Created on Tue May 14 17:10:29 2019

@author: Administrator
"""

import requests, json
#base_url = "https://free.currconv.com/api/v7/convert"
#currency = "?q=" + 
#api_key = "&compact=ultra&apiKey=9d27f514cd892f5eb80d"
#url = base_url + currency + api_key
url = 'https://free.currconv.com/api/v7/convert?q=USD_INR&compact=ultra&apiKey=9d27f514cd892f5eb80d'
response = requests.get(url)
data = json.loads(response.text)
value = int(input('Enter how many dollars you want to convert into ruppess : '))
print(value, '$ =', data['USD_INR'] * value)
