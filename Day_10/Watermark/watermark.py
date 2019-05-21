# -*- coding: utf-8 -*-
"""
Created on Tue May 21 08:54:31 2019

@author: Administrator
"""

from PIL import Image

img = Image.open('Certificate.png')
logo = Image.open('logo.png')
mask = Image.new('L', logo.size, color = 50)
img.paste(logo, (349, 190), mask)
img.show()
img.save('Certificate_with_watermark.png')