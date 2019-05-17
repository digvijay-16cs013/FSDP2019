# -*- coding: utf-8 -*-
"""
Created on Tue May 14 16:26:16 2019

@author: Administrator
"""
from datetime import datetime as dt
import requests, json
api_key = "&appid=ebedc94f4bc8cb9a052821159937018c"
base_url = "http://api.openweathermap.org/data/2.5/weather"
city_name = input('Enter City Name : ')
url = base_url + '?q=' + city_name + api_key
response = requests.get(url)
weather_data = json.loads(response.text)
print('Lattitude :', weather_data['coord']['lat'])
print('Longitude :', weather_data['coord']['lon'])
print('Temprature :', round(weather_data['main']['temp'] - 273, 2), 'Celsius.')
print('Pressure :', weather_data['main']['pressure'])
print('Humidity :', weather_data['main']['humidity'])
print('Max. Temprature :', weather_data['main']['temp_max'])
print('Min. Temprature :', weather_data['main']['temp_min'])
print('Wind Speed :', weather_data['wind']['speed'])
print('Sunrise Time :', dt.fromtimestamp(weather_data['sys']['sunrise']))
print('Sunrise Time :', dt.fromtimestamp(weather_data['sys']['sunset']))