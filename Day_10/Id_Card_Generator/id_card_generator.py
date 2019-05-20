# -*- coding: utf-8 -*-
"""
Created on Mon May 20 23:21:11 2019

@author: Administrator
"""


# to import some important modules from PIL library
from PIL import Image, ImageDraw, ImageFont

# importing os for path validation
import os

# to get the number of students
num_of_students = int(input('Enter number of students : '))

# loop to create each student card 
for stu in range(num_of_students):
    
    # loads the background template of card (downloaded from freepik.com)
    background = Image.open('id_card.png')
    
    # sets draw object to draw text
    draw = ImageDraw.Draw(background)
    
    # Company Name
    company_name = 'Forsk Technologies'
    
    # font for Company Name
    font_c = ImageFont.truetype('Lobster-Regular.ttf', size = 21)
    
    # Color for Company Name
    color_c = 'rgb(223, 230, 233)'
    
    # draw Company Name on id_card template
    draw.text((85, 143), company_name, fill = color_c, font = font_c)
    
    # to get the Name of student
    name = input('Enter Student {} Name : '.format(stu + 1)).upper()
    
    # font for Student name 
    font_n = ImageFont.truetype('Roboto-Regular.ttf', size = 21)
    
    # color for Student Name
    color_c = 'rgb(1, 2, 3)'
    
    # draw Student Name on id_card template
    draw.text((90, 320), name, fill = color_c, font = font_n)
    
    # unique ids for students
    Id = 'ID : FSDP2019-0{}'.format(stu + 1)
    
    # font for student id
    font_id = ImageFont.truetype('Roboto-Regular.ttf', size = 16)  
    
    # draw student id on id_card template
    draw.text((112, 360), Id, fill = color_c, font = font_id)
    
    # to get the seal of company
    seal = Image.open('forsk_seal.png')
    
    # paste seal on id_card
    background.paste(seal, (66, 407))
    
    # to get the sign of autority
    sign = Image.open('signature.png')
    
    # paste sign on id_card
    background.paste(sign, (185, 411))
    
    # validity of id_card
    validity = '07 Jul 2019'
    
    # font for validity date
    font_v = ImageFont.truetype('Roboto-Bold.ttf', size = 11)
    
    # draw validity date on id_card
    draw.text((493, 343), validity, fill = color_c, font = font_v)
    
    # Email ID of student
    email = input('Enter Email Id : ')
    
    # font for Email_ID
    font_m = ImageFont.truetype('Roboto-Regular.ttf', size = 8)
    
    # draw Email ID on id_card
    draw.text((392, 426), email, fill = color_c, font = font_m)
    
    # address of Student
    address = input('Enter address : ')
    
    # draw address of Student
    draw.text((503, 426), address, fill = color_c, font = font_m)
    
    # site of Student if any
    site = input('Enter Site Name or Enter N/A if not available: ')
    
    # draw site name on id_card
    draw.text((392, 444), site, fill = color_c, font = font_m)
    
    # contact number of Student
    contact_number = input('Enter Contact Number : ')
    
    # draw contact number on id_card
    draw.text((503, 444), contact_number, fill = color_c, font = font_m)
    
    # to get the path for image file of signature of Student
    stu_sign_path = input('Enter Image path for signature : ')
    
    # loop until path is not correct
    while not os.path.exists(stu_sign_path):
        
        # letting user know
        print('\nPath provided is wrong\nPlease provide correct path\n')
        stu_sign_path = input('\nTo know your current working directory Enter pwd or Enter correct path to continue: ')
        
        # to check if user wants to know the current working directory
        if stu_sign_path.lower() == 'pwd':
            
            # to show the current working directory
            print('Your current working directory :', os.getcwd())
            
    # getting signture image data
    stu_sign = Image.open(stu_sign_path)
    
    # changing shape of image
    stu_sign.thumbnail((80, 28), Image.ANTIALIAS)
    
    # paste the signature of Student on id_card
    background.paste(stu_sign, (436, 363))
    
    # to get the path of Student's photo
    stu_photo_path = input('Enter Image path for photo : ')
    
    # loop until path is not correct
    while not os.path.exists(stu_photo_path):
        
        # letting user know
        print('\nPath provided is wrong\nPlease provide correct path\n')
        stu_photo_path = input('\nTo know your current working directory Enter pwd or Enter correct path to continue: ')
        
        # to check if user wants to know the current working directory
        if stu_photo_path.lower() == 'pwd':
            
            # to show the current working directory
            print('Your current working directory :', os.getcwd())
    
    # to get the Student's photo data
    photo = Image.open(stu_photo_path)
    
    # resizing the image
    photo.thumbnail((128, 128), Image.ANTIALIAS)
    
    # pasting Student's Photogrpah on id_card
    background.paste(photo, (110, 190))
    
    # to show the id_card
    background.show()
    
    # saving id_card
    background.save('{}\'s_id_card.png'.format(name))