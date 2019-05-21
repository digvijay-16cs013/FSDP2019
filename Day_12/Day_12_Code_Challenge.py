"""
Code Challenge
  Name: 
    Titanic Analysis
  Filename: 
    titanic.py
  Dataset:
    training_titanic.csv
  Problem Statement:
      It’s a real-world data containing the details of titanic ships 
      passengers list.
      Import the training set "training_titanic.csv"
  Answer the Following:
      How many people in the given training set survived the disaster ?
      How many people in the given training set died ?
      Calculate and print the survival rates as proportions (percentage) 
      by setting the normalize argument to True.
      Males that survived vs males that passed away
      Females that survived vs Females that passed away
      
      Does age play a role?
      since it's probable that children were saved first.
      
      Another variable that could influence survival is age; 
      since it's probable that children were saved first.

      You can test this by creating a new column with a categorical variable Child. 
      Child will take the value 1 in cases where age is less than 18, 
      and a value of 0 in cases where age is greater than or equal to 18.
 
      Then assign the value 0 to observations where the passenger 
      is greater than or equal to 18 years in the new Child column.
      Compare the normalized survival rates for those who are <18 and 
      those who are older. 
    
      To add this new variable you need to do two things
        1.     create a new column, and
        2.     Provide the values for each observation (i.e., row) based on the age of the passenger.
    
  Hint: 
      To calculate this, you can use the value_counts() method in 
      combination with standard bracket notation to select a single column of
      a DataFrame
"""
import pandas as pd

titanic_data = pd.read_csv('training_titanic.csv')
s_and_d = titanic_data['Survived'].value_counts()
s_and_d_per = titanic_data['Survived'].value_counts(normalize = True)
survived = s_and_d[1]
died = s_and_d[0]
survived_per =  s_and_d_per[1]
died_per =  s_and_d_per[0]

male_survived = titanic_data['Survived'][titanic_data['Sex'] == 'male'].value_counts(normalize = True)[1]
male_died = titanic_data['Survived'][titanic_data['Sex'] == 'male'].value_counts(normalize = True)[0]

female_survived = titanic_data['Survived'][titanic_data['Sex'] == 'female'].value_counts(normalize = True)[1]
female_died = titanic_data['Survived'][titanic_data['Sex'] == 'female'].value_counts(normalize = True)[0]

titanic_data['Age'] = titanic_data['Age'].fillna(titanic_data['Age'].mean())
titanic_data['Child'] = titanic_data['Age'].map(lambda x : 1 if x < 18 else 0)


sur_rate = titanic_data['Child'][titanic_data['Survived'] == 1].value_counts(normalize = True)
child_sur = sur_rate[0]
older_sur = sur_rate[1]


"""
Code Challenge
  Name: 
      Exploratory Data Analysis - Automobile
  Filename: 
      automobile.py
  Dataset:
      Automobile.csv
  Problem Statement:
      Perform the following task :
      1. Handle the missing values for Price column
      2. Get the values from Price column into a numpy.ndarray
      3. Calculate the Minimum Price, Maximum Price, Average Price and Standard Deviation of Price
"""
import pandas as pd, numpy as np

auto_data = pd.read_csv('Automobile.csv')

# replacing NaN values
auto_data['price'] = auto_data['price'].fillna(auto_data['price'].median())

price = np.array(auto_data['price'])

minimum = price.min()
maximum = price.max()
average = price.mean()
std_deviation = price.std()

"""
Code Challenge
  Name: 
    Thanks giving Analysis
  Filename: 
    Thanksgiving.py
  Problem Statement:
    Read the thanksgiving-2015-poll-data.csv file and 
    perform the following task :

    Discover regional and income-based patterns in what Americans eat for 
    Thanksgiving dinner

    Convert the column name to single word names
    
    Using the apply method to Gender column to convert Male & Female
    Using the apply method to clean up income
    (Range to a average number, X and up to X, Prefer not to answer to NaN)
    
    compare income between people who tend to eat homemade cranberry sauce for
    Thanksgiving vs people who eat canned cranberry sauce?
    
    find the average income for people who served each type of cranberry sauce
    for Thanksgiving (Canned, Homemade, None, etc).
    
    Plotting the results of aggregation
    
    Do people in Suburban areas eat more Tofurkey than people in Rural areas?
    Where do people go to Black Friday sales most often?
    Is there a correlation between praying on Thanksgiving and income?
    What income groups are most likely to have homemade cranberry sauce?

    Verify a pattern:
        People who have Turducken and Homemade cranberry sauce seem to have 
        high household incomes.
        People who eat Canned cranberry sauce tend to have lower incomes, 
        but those who also have Roast Beef have the lowest incomes
        
    Find the number of people who live in each area type (Rural, Suburban, etc)
    who eat different kinds of main dishes for Thanksgiving:
        
  Hint:

"""
      

"""
Code Challenge
  Name: 
    Telecom Churn Analysis
  Dataset:
    Telecom_churn.csv
  Filename: 
    telecom_churn.py
  Problem Statement:
    Read the telecom_churn.csv file and perform the following task :
    
"""

import pandas as pd, matplotlib.pyplot as plt

telecom_data = pd.read_csv('Telecom_churn.csv')

churn_prediction = telecom_data['churn'][(telecom_data['voice mail plan'] == 'yes') & (telecom_data['international plan'] == 'yes')].value_counts(normalize = True)[True]

intl_call_charge_for_churn = telecom_data['total intl charge'][telecom_data['churn'] == True].sum()
intl_call_charge_for_not_churn = telecom_data['total intl charge'][telecom_data['churn'] == False].sum()
plt.bar(['Churn', 'Not Churn'], [intl_call_charge_for_churn, intl_call_charge_for_not_churn], width = 0.5, align = 'center')
plt.title('International Call Charge')


state = telecom_data['state'][(telecom_data['churn'] == True) & (telecom_data['total night minutes'] == telecom_data['total night minutes'].max())]


