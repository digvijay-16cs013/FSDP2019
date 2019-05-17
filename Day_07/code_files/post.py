# -*- coding: utf-8 -*-
"""
Created on Tue May 14 17:40:00 2019

@author: Administrator
"""

import requests
data = {"name" : "Tapan", "value" : 0}
header = {"Content-Type" : "Application"}
url = "https://enyllzg3bgi0g.x.pipedream.net"
requests.post(url, data, header)
response = requests.get(url)

print(response.text)