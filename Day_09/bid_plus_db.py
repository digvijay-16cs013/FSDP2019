# -*- coding: utf-8 -*-
"""
Created on Thu May 16 17:58:54 2019

@author: Administrator
"""

from selenium import webdriver
import mysql.connector
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

for i in range(1, 11):
    download_link = driver.find_element_by_xpath('//*[@id="pagi_content"]/div[{}]/div[1]/p[1]/a'.format(i))
    bid_no.append(download_link.text)
    items.append(driver.find_element_by_xpath('//*[@id="pagi_content"]/div[{}]/div[2]/p[1]/span'.format(i)).text)
    numbers.append(driver.find_element_by_xpath('//*[@id="pagi_content"]/div[{}]/div[2]/p[2]/span'.format(i)).text)
    dept_and_add.append(driver.find_element_by_xpath('//*[@id="pagi_content"]/div[{}]/div[3]/p[2]'.format(i)).text)
    start_date.append(driver.find_element_by_xpath('//*[@id="pagi_content"]/div[{}]/div[4]/p[1]/span'.format(i)).text)
    end_date.append(driver.find_element_by_xpath('//*[@id="pagi_content"]/div[{}]/div[4]/p[2]/span'.format(i)).text)
    # download_link.click()

driver.close()

st_date = [date[:date.find(' ')] for date in start_date]
st_time = [time[time.find(' ') + 1:] for time in start_date]
en_date = [date[:date.find(' ')] for date in end_date]
en_time = [date[date.find(' ') + 1:] for date in end_date]

con = mysql.connector.connect(user = 'phpmyadmin', password = 'phpmyadmin', host = 'db4free.net', database = 'db4free_db')

c = con.cursor()
c.execute('DROP TABLE Bid1_details')
c.execute("""CREATE TABLE Bid1_details(
        Bid_id TEXT,
        Items TEXT,
        NUMBERS INTEGER,
        DEPT_AND_ADDRESS TEXT,
        START_DATE TEXT,
        START_TIME TEXT,
        END_DATE TEXT,
        END_TIME TEXT
        )""")
for i in range(10):
    c.execute('INSERT INTO Bid1_details VALUES("{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}")'.format(bid_no[i], items[i], int(numbers[i]), dept_and_add[i], st_date[i], st_time[i], en_date[i], en_time[i]))
    
c.execute("SELECT * FROM Bid1_details")

print(c.fetchall())

con.commit()
con.close()
