# -*- coding: utf-8 -*-
"""
Created on Sun May 19 22:14:25 2019

@author: Administrator
"""

# to import some modules for image manipulation
from PIL import Image, ImageDraw, ImageFont

# to get the background image
background = Image.open('background.png')

# to get the logo
logo = Image.open('logo.png')

# to get the seal
seal = Image.open('forsk_seal.png')

# to get the signature
sign = Image.open('signature.png')

# Certificate header
certificate_text = 'Certificate of training'

# color of certificate header 
certificate_color = 'rgb(34, 47, 62)'

# text after header
text_t = 'This is to certify that'

# name of candidate
name = input('Enter Candidate Name : ')

# completion text
text_b = 'has successfully completed the course on'

# course name
course_name = input('Enter Course Name : ')

# at text for place
at = 'at'

# from text for timing
from_text = 'from'

# to text for timing
to_text = 'to'

# start date of course
from_date = input('Enter starting date of course like (01 Jan 2000) : ')

# end date of course
to_date = input('Enter ending date of course like (01 Jan 2000) : ')

# company name
company_name = input('Enter Company Name : ')

# to paste the logo on certificate background
background.paste(logo, (700, 10))

# to paste the seal on certificate background
background.paste(seal, (282, 390))

# to paste the signature on certificate background
background.paste(sign, (25, 350))

# to set a draw object to draw text
draw = ImageDraw.Draw(background)

# font of text "Certificate"
font_c = ImageFont.truetype('Oswald-Regular.ttf', size = 50)

# to draw "Certificate" text on Certificate image
draw.text((270, 80), certificate_text, fill = certificate_color, font = font_c)

# font of text "This is to certify that"
font_t = ImageFont.truetype('Oswald-Regular.ttf', size = 20)

# to draw "This is to certify that"
draw.text((375, 155), text_t, fill = certificate_color, font = font_t)

# font of Name
font_n = ImageFont.truetype('Playball-Regular.ttf', size = 50)

# font of course name and company name
font_cn = ImageFont.truetype('Playball-Regular.ttf', size = 30)

# font of date
font_cn1 = ImageFont.truetype('Playball-Regular.ttf', size = 20)

# to draw Name
draw.text((330, 180), name, fill = certificate_color, font = font_n)

# to draw text "has successfully completed the course on"
draw.text((230, 250), text_b, fill = certificate_color, font = font_t)

# to draw Course Name
draw.text((535, 250), course_name, fill = certificate_color, font = font_cn)

# to draw text "at" for place
draw.text((358, 290), at, fill = certificate_color, font = font_t)

# to draw Company Name
draw.text((380, 290), company_name, fill = certificate_color, font = font_cn)

# to draw text "From" for date
draw.text((330, 330), from_text, fill = certificate_color, font = font_t)

# to draw text "to" for date
draw.text((492, 330), to_text, fill = certificate_color, font = font_t)

# to draw Start Date
draw.text((372, 335), from_date, fill = certificate_color, font = font_cn1)

# to draw End Date
draw.text((512, 335), to_date, fill = certificate_color, font = font_cn1)

# to show Image
background.show()

# to save Certificate
background.save('Certificate.png')