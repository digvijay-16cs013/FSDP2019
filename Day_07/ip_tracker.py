# -*- coding: utf-8 -*-
"""
Created on Wed May 15 08:46:15 2019

@author: Administrator
"""

import requests
base_url = 'http://api.ipstack.com/'
ip_address = input('Enter ip adddress : ')
access_key = '?access_key=4aa482cc17809d40cf4aa39f4f044fe0'
url = base_url + ip_address + access_key
response = requests.get(url)
print(response.text)
json_format = response.json()
print(json_format)
print('IP address :', json_format['ip'])
print('Country Name :', json_format['country_name'])
print('Reginon Name :', json_format['region_name'])
print('City :', json_format['city'])
print('Latitude :', json_format['latitude'])
print('Longitude :', json_format['longitude'])