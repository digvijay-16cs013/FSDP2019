# -*- coding: utf-8 -*-
"""
Created on Sat May 11 10:54:47 2019

@author: Administrator
"""

# import Image Module from PIL Library
from PIL import Image
import os

image_files = os.listdir('.')
print(os.getcwd())
for image in image_files:
    if image.endswith('.jpg'):
        print(image.rstrip('.jpg'))

# getting image name from user
image_name = input('Enter Image Name : ') + '.jpg'

# to open image
img = Image.open(image_name)

while True:

    # getting choice from user
    choice = input('Press :-\nG : Greyscale\nR : Rotate 90 degree\nC : Crop\nT : Thumbnail\n\n')
    
    if not choice:
        break
    
    elif choice[0].lower() == 'g':
        
        img = img.convert(mode = 'L')
        # img_bw = Image.open('greyscale.jpg')
        # img_bw.show()
        # print('Image Saved\nImage Name : greyscale.jpg')
        
    elif choice[0].lower() == 'r':
        img = img.transpose(Image.ROTATE_90)
        # img_rotate.show()
        # img_rotate.save('rotated_image.jpg')
        # print('Image Saved\nImage Name : rotated_image.jpg')
        
    elif choice[0].lower() == 'c':
        
        # to get the image size
        print('You image size is', img.size)
        
        # to get coordinates fro user
        coordinates = input('Enter coordinates for cropping separated by space: ').split()
        
        int_coordinates = []
        
        # to convert coordinates into integer
        for c in coordinates:
            int_coordinates.append(int(c))
        
        # to crop the image    
        img = img.crop(box = tuple(int_coordinates))
        
        # to show the cropped image
        # cropped_image.show()
        
        # saving image...
        # cropped_image.save('cropped_image.jpg')
        
        # print('Image Name : cropped_image.jpg')
        
    elif choice[0].lower() == 't':
        
        # to get the thumbnail size
        width = int(input('Enter Width : '))
        height = int(input('Enter height : '))
        
        # size of thumbnail
        size = (width, height)
        
        # to convert image thumbnail
        img.thumbnail(size)
        
        # to save the image
        # img.save('thumbnail.jpg')
        
        # to open thumbnail image
        # img = Image.open('thumbnail.jpg')
        
        # to show image
        # img.show()
        
        # print('Image Saved\nImage Name : thumbnail.jpg')
        
    else:   
        
        print('Please enter right choice...')
    

img.save('new_image.jpg')
print('Image Saved\nImage Name : new_image.jpg')