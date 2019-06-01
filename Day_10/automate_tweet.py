# -*- coding: utf-8 -*-
"""
Created on Tue May 21 23:08:22 2019

@author: Administrator
"""


# import selenium to perform some web automation
from selenium import webdriver

# url of twitter
url = 'https://twitter.com/login'

# url of horoscope site
horoscope_url = 'https://www.astrology.com/horoscopes.html'

# loading web driver for Chrome browser which is default in my case
driver_h = webdriver.Chrome(r'C:\Users\Administrator\Desktop\chromedriver')

# loading the horoscope site
driver_h.get(horoscope_url)

# finding the Zodiac name, for me it is Pisces
zodiac = driver_h.find_element_by_xpath('/html/body/section[1]/div[3]/a[12]')

# click the link on Pisces
zodiac.click()

# finding horoscope content using xpath
horoscope = 'Horoscope Today \n' + driver_h.find_element_by_xpath('/html/body/section/section[1]/div[2]/main/p[1]').text

# posting horoscope only till we encounters first period('.') because single tweet cannot have more than 213 characters
horoscope = horoscope[:horoscope.index('.')]

# to close the browser
driver_h.close()

# load the web driver again
driver = webdriver.Chrome(r'C:\Users\Administrator\Desktop\chromedriver')

# load the twitter site in browser
driver.get(url)

# finding username input box on twitter site using xpath
username = driver.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/fieldset/div[1]/input')

# to type username into input box
username.send_keys('Your Username of twitter')

# finding password input box on twitter site using xpath
password = driver.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/fieldset/div[2]/input')

# to type password into password box
password.send_keys('Your Password of twitter')

# to uncheck the remember checkbox to avoid saving username and password in browser's cache
remember = driver.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/div[2]/div/label/input')

# click to uncheck
remember.click()

# find login button by its xpath on twitter page
login = driver.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/div[2]/button')

# click login button to login into twitter account
login.click()

# finding text box for tweet 
text_box = driver.find_element_by_xpath('//*[@id="tweet-box-home-timeline"]')

# to type the horoscope on text box on page
text_box.send_keys(horoscope)

# find tweet button on twiiter page
tweet = driver.find_element_by_xpath('//*[@id="timeline"]/div[2]/div/form/div[3]/div[2]/button/span[1]')

# click tweet button to tweet the horoscope
tweet.click()

# to close the browser after tweet uncomment the following line
# driver.close()