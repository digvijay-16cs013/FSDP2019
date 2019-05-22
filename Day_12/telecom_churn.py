# -*- coding: utf-8 -*-
"""
Created on Wed May 22 22:44:51 2019

@author: Administrator
"""

# -*- coding: utf-8 -*-
"""
Created on Wed May 22 22:31:47 2019

@author: Administrator
"""


# gettting pandas as pd and matplotlib.pyplot as plt 
import pandas as pd, matplotlib.pyplot as plt

# readding the whole data from csv file
telecom_data = pd.read_csv('Telecom_churn.csv')

# counting the number of churn customers who have taken both voice mail and international plan  
churn_prediction = telecom_data['churn'][(telecom_data['voice mail plan'] == 'yes') & (telecom_data['international plan'] == 'yes')].value_counts(normalize = True)[True]

# total international call charges for Churn customers
intl_call_charge_for_churn = telecom_data['total intl charge'][telecom_data['churn'] == True].sum()

# total international call charges for Normal customers
intl_call_charge_for_not_churn = telecom_data['total intl charge'][telecom_data['churn'] == False].sum()

# plotting the bar chart of international call charges for Churn and not Churn customers
plt.bar(['Churn', 'Not Churn'], [intl_call_charge_for_churn, intl_call_charge_for_not_churn], width = 0.5, align = 'center')

# giving the bar chart a good title
plt.title('International Call Charge')

# finding the maximum "total night minutes" for churn customers
night_calls_churn_cus = telecom_data['total night minutes'][telecom_data['churn'] == True].max()

# finding the state for which churn customers have max "total night minutes"
state = telecom_data['state'][telecom_data['total night minutes'] == night_calls_churn_cus].item()

# gives a title to our bar chart
plt.title('Popularity of different call types among Churn Users')

# gives the max value for each call type for churn customers
most_popular_call_type = telecom_data[['total day calls', 'total eve calls', 'total night calls', 'total intl calls']][telecom_data['churn'] == True].max()

# plots the nice bar chart
plt.bar(most_popular_call_type.index.tolist(), most_popular_call_type.values)

# to show the bar chart
plt.show()


# gives the minimum charge for all call type
min_ch_all_call_type = telecom_data[['total day charge', 'total eve charge', 'total night charge', 'total intl charge']][telecom_data['churn'] == True].min()

# gives a nice title to our bar chart
plt.title('Minimum call charges of all call types for Churn users')

# plots a nice bar chart
plt.bar(min_ch_all_call_type.index, min_ch_all_call_type.values)

# to avoid overlapping of ticks on x-axis changing their rotation to vertical
plt.xticks(rotation = 'vertical')

# to show the bar chart
plt.show()

# gives the maximum account length for churn customers
max_acc_length_churn = telecom_data['account length'][telecom_data['churn'] == True].max() 

# gives the maximum account length for normal customers
max_acc_length_not_churn = telecom_data['account length'][telecom_data['churn'] == False].max()

# gives a title to bar chart
plt.title('Account length')

# plots a nice bar chart of data
plt.bar(['Churn', 'Not Churn'], [max_acc_length_churn, max_acc_length_not_churn], color = 'violet', width = 0.5)

# to show the bar chart
plt.show()

# gives the customer service calls for churn customers
cus_care_service = telecom_data['customer service calls'][telecom_data['churn'] == True]

# to know how many churn customers actually use customer care service for complaints(assigning 1 if they use the serivce, otherwise 0)
churn_called = cus_care_service.map(lambda x : 1 if x != 0 else 0)

# gives the percentage of churn customers who actually use customers service for complaints
churn_called_per = (churn_called.sum() / churn_called.count()) * 100