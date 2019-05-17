# -*- coding: utf-8 -*-
"""
Created on Thu May 16 08:24:38 2019

@author: Administrator
"""


from selenium import webdriver
import pandas as pd
from collections import OrderedDict
from time import sleep
url = 'https://bidplus.gem.gov.in/bidlists'
driver = webdriver.Chrome(r'C:\Users\Administrator\Desktop\chromedriver')
driver.get(url)
sleep(2)
bid_no = []
items = []
numbers = []
dept_and_add = []
start_date = []
end_date = []

data = {}

for i in range(1, 11):
    download_link = driver.find_element_by_xpath('//*[@id="pagi_content"]/div[{}]/div[1]/p[1]/a'.format(i))
    bid_no.append(download_link.text)
    items.append(driver.find_element_by_xpath('//*[@id="pagi_content"]/div[{}]/div[2]/p[1]/span'.format(i)).text)
    numbers.append(driver.find_element_by_xpath('//*[@id="pagi_content"]/div[{}]/div[2]/p[2]/span'.format(i)).text)
    dept_and_add.append(driver.find_element_by_xpath('//*[@id="pagi_content"]/div[{}]/div[3]/p[2]'.format(i)).text)
    start_date.append(driver.find_element_by_xpath('//*[@id="pagi_content"]/div[{}]/div[4]/p[1]/span'.format(i)).text)
    end_date.append(driver.find_element_by_xpath('//*[@id="pagi_content"]/div[{}]/div[4]/p[2]/span'.format(i)).text)
    download_link.click()

st_date = [date[:date.find(' ')] for date in start_date]
st_time = [time[time.find(' ') + 1:] for time in start_date]
en_date = [date[:date.find(' ')] for date in end_date]
en_time = [date[date.find(' ') + 1:] for date in end_date]

col_name = ['Bid_no.', 'Items', 'Numbers', 'Dept_and_Address', 'Start_date', 'Start_time', 'End_date', 'End_time']
df = pd.DataFrame(OrderedDict(zip(col_name, [bid_no, items, numbers, dept_and_add, st_date, st_time, en_date, en_time])))
df.to_csv('Bid_detals.csv', index = False)

    
#bid no                //*[@id="pagi_content"]/div[1]/div[1]/p[1]/a
#                      //*[@id="pagi_content"]/div[2]/div[1]/p[1]/a
#
#items                 //*[@id="pagi_content"]/div[1]/div[2]/p[1]/span
#                      //*[@id="pagi_content"]/div[2]/div[2]/p[1]/span
#
#numbers               //*[@id="pagi_content"]/div[1]/div[2]/p[2]/span
#                      //*[@id="pagi_content"]/div[2]/div[2]/p[2]/span
#
#DeptName and address  //*[@id="pagi_content"]/div[1]/div[3]/p[2]
#                      //*[@id="pagi_content"]/div[2]/div[3]/p[2]
#
#start date            //*[@id="pagi_content"]/div[1]/div[4]/p[1]/span
#                      //*[@id="pagi_content"]/div[2]/div[4]/p[1]/span
#
#end date              //*[@id="pagi_content"]/div[1]/div[4]/p[2]/span
#                      //*[@id="pagi_content"]/div[2]/div[4]/p[2]/span

