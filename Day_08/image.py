# -*- coding: utf-8 -*-
"""
Created on Thu May 16 09:55:49 2019

@author: Administrator
"""

import requests

# url of the image
url = 'http://forsk.in/images/Forsk_logo_bw.png'

# binary source of the image
source = requests.get(url).content

# to get the image name from url
file_name = url.split('/')[-1]

# to save the image with file_name
with open(file_name, 'wb') as fp:
    fp.write(source)