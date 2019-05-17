# -*- coding: utf-8 -*-
"""
Created on Wed May 15 09:27:41 2019

@author: Administrator
"""
import requests
api_key = '?key=trnsl.1.1.20190515T035656Z.8ca9bef32afdad91.4a3f414a7c5ecc4ce349544adade1950053b8ae8'
base_url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
text = '&text=' + input('Enter text to translate :')
translation_direction = '&lang=' + input('Enter language code of entered text : ') + '-' + input('Enter language code for translated text : ')
url = base_url + api_key + text + translation_direction
response = requests.get(url)
data = response.json()
print(data["text"][0])

# & text=<text to translate>
# & lang=<translation direction>