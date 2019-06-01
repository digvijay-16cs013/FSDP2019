# -*- coding: utf-8 -*-
"""
Created on Fri May 31 13:12:47 2019

@author: Administrator
"""

from PIL import Image

frames = []
for i in range(1, 21):
    img = Image.open('i{}.png'.format(i))
    frames.append(img)

frames[0].save('Cute_Dog.gif', format = 'GIF', append_images = frames[1:], save_all = True, duration = 160, loop = 0)
