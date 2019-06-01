# -*- coding: utf-8 -*-
"""
Created on Mon May 20 17:45:49 2019

@author: Administrator
"""

from selenium import webdriver
import numpy as np, matplotlib.pyplot as plt

url = 'https://en.wikipedia.org/wiki/List_of_states_and_union_territories_of_India_by_area'

driver = webdriver.Chrome(r'C:\Users\Administrator\Desktop\chromedriver')
driver.get(url)


state = []
national_share = []

for i in range(1, 7):
    state.append(driver.find_element_by_xpath('//*[@id="mw-content-text"]/div/table[2]/tbody/tr[{}]/td[2]/a'.format(i)).text)
    national_share.append(driver.find_element_by_xpath('//*[@id="mw-content-text"]/div/table[2]/tbody/tr[{}]/td[5]'.format(i)).text)

national_share = list(map(float, national_share))
colors = ['blue', 'magenta', 'green', 'skyblue', 'indigo', 'gold']
exp_index = national_share.index(max(national_share))
explode = np.zeros(6)
explode[exp_index] = 0.2
#print(national_share)
plt.pie(national_share, explode = explode, labels = state, colors = colors, shadow = True, autopct='%1.1f%%')
plt.savefig('Pie_chart.png')
plt.show()
