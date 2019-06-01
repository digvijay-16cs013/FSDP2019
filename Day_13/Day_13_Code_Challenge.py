
"""
Code Challenge

https://en.wikipedia.org/wiki/List_of_states_and_union_territories_of_India_by_area


Scrap the data from State/Territory and National Share (%) columns for top 6 
statews basis on National Share (%). 
Crswdeate a Pie Chart using MatPlotLib and explode the state with largest national share %.
dx
"""

"""
Code Challenge 

import Automobile.csv file.

Using MatPlotLib create a PIE Chart of top 10 car makers according to the number 
of their cars and explode the largest car maker
"""


"""
Code Challenge
  Name: 
    SSA Analysis
  Filename: 
    ssa.py
  Problem Statement:
    (Baby_Names.zip)
    The United States Social Security Administration (SSA) has made available 
    data on the frequency of baby names from 1880 through the 2010. 
    (Use Baby_Names.zip from Resources)  
    
    Read data from all the year files starting from 1880 to 2010, 
    add an extra column named as year that contains year of that particular data
    Concatinate all the data to form single dataframe using pandas concat method
    Display the top 5 male and female baby names of 2010
    Calculate sum of the births column by sex as the total number of births 
    in that year(use pandas pivot_table method)
    Plot the results of the above activity to show total births by sex and year  
     
"""
# to get pandas as pd 
import pandas as pd

# creating a main DataFrame with column names, which will be used to concat all the dataframes into one
main_df = pd.DataFrame(columns = ['Name', 'Sex', 'Number', 'Year'])

# iterating to read all the csv files from year 1880 to 2010
for i in range(1880, 2011):
    
    # since file name follows a specific pattern therefore creating file name using that pattern
    file_name = 'yob' + str(i) + '.txt'
    
    # read one csv file at a time 
    data = pd.read_csv(file_name, header = None)
    
    # setting columns for the individual dataframe
    data.columns = ['Name', 'Sex', 'Number']
    
    # adding a new columns year to each dataframe which has its year value
    data['Year'] = i 
    
    # sort the dataframe by 'Number' column in descending order for later use
    data = data.sort_values(by = 'Number', ascending = False)
    
    # concat each dataframe to the main dataframe
    main_df = pd.concat([data, main_df])
    
# getting top 5 male names from all the data
male_names_2010 = main_df['Name'][(main_df['Sex'] == 'M') & (main_df['Year'] == 2010)].head()

# getting top 5 female names from all the data
female_names_2010 = main_df['Name'][(main_df['Sex'] == 'F') & (main_df['Year'] == 2010)].head()
"""
Code Challenge
  Name: 
    URL shortening service Bitly
  Filename: 
    bitly.py
  Problem Statement:
    (usagov_bitly_data.json)
    In 2011, URL shortening service Bitly partnered with the US government website
    USA.gov to provide a feed of anonymous data gathered from users who shorten links
    ending with .gov or .mil. 
    In 2011, a live feed as well as hourly snapshots were available
    as downloadable text files. 
    This service is shut down at the time of this writing (2017),
    but we preserved one of the data files.
    In the case of the hourly snapshots, each line in each file contains a common form of
    web data known as JSON. (Use usagov_bitly_data.txt file from Resources)

    Replace the 'nan' values with 'Mising' and ' ' values with 'Unknown' keywords
    Print top 10 most frequent time-zones from the Dataset i.e. 'tz', with and without Pandas
    Count the number of occurrence for each time-zone
    Plot a bar Graph to show the frequency of top 10 time-zones (using Seaborn)
    From field 'a' which contains browser information and separate out browser capability(i.e. the first token in the string eg. Mozilla/5.0)
    Count the number of occurrence for separated browser capability field and plot bar graph for top 5 values (using Seaborn)
    Add a new Column as 'os' in the dataset, separate users by 'Windows' for the values in  browser information column i.e. 'a' that contains "Windows" and "Not Windows" for those who don't

Hint:
    http://1usagov.measuredvoice.com/2011/
    
"""
# getting Counter class from collections module
from collections import Counter

# getting some modules(pandas as pd, numpy as np, matplotlib.pyplot as plt)
import pandas as pd,numpy as np, matplotlib.pyplot as plt

# reading the json file using pandas method read_json, lines = True will avoid Value Error
bitly_data = pd.read_json('usagov_bitly_data.json', lines = True)

# replaces all the "NaN" to "Missing" values
bitly_data = bitly_data.replace(np.nan, 'Missing')

# replaces all the '' values "Unknown"
bitly_data = bitly_data.replace('', 'Unknown')

# getting all the time zones which are known
time_zone = bitly_data['tz'][bitly_data['tz'] != 'Unknown']

# getting top ten time zones from all the time zones
top_ten_tz = time_zone.value_counts().head(10)
print(top_ten_tz)

# ploting a bar chart time zones
plt.bar(top_ten_tz.index, top_ten_tz.values, color = 'skyblue')

# avoiding overlapping of time zone names on x axis by setting rotaion to vertical
plt.xticks(rotation = 'vertical')

# shows the bar chart
plt.show()

# without pandas top 10 most common time zones
time_zones = Counter(bitly_data['tz'])

# most_common method returns key-value pairs as list of tuples 
# then that tuple converted into dictionay
# then finally we get name of time zones by calling the keys method on dictionary
top_10_tz = dict(time_zones.most_common(10)).keys()
print(top_10_tz)



"""
Code Challenge
  Name: 
    Baltimore City Analysis
  Filename: 
    baltimore.py
  Problem Statement:
    Read the Baltimore_City_Employee_Salaries_FY2014.csv file 
    and perform the following task :

    0. remove the dollar signs in the AnnualSalary field and assign it as a float
    0. Group the data on JobTitle and AnnualSalary, and aggregate with sum, mean, etc.
       Sort the data and display to show who get the highest salary
    0. Try to group on JobTitle only and sort the data and display
    0. How many employess are there for each JobRoles and Graph it
    0. Graph and show which Job Title spends the most
    0. List All the Agency ID and Agency Name 
    0. Find all the missing Gross data in the dataset 
    
  Hint:

import pandas as pd
import requests
import StringIO as StringIO
import numpy as np
        
url = "https://data.baltimorecity.gov/api/views/2j28-xzd7/rows.csv?accessType=DOWNLOAD"
r = requests.get(url)
data = StringIO.StringIO(r.content)

dataframe = pd.read_csv(data,header=0)

dataframe['AnnualSalary'] = dataframe['AnnualSalary'].str.lstrip('$')
dataframe['AnnualSalary'] = dataframe['AnnualSalary'].astype(float)

# group the data
grouped = dataframe.groupby(['JobTitle'])['AnnualSalary']
aggregated = grouped.agg([np.sum, np.mean, np.std, np.size, np.min, np.max])

# sort the data
pd.set_option('display.max_rows', 10000000)
output = aggregated.sort(['amax'],ascending=0)
output.head(15)


aggregated = grouped.agg([np.sum])
output = aggregated.sort(['sum'],ascending=0)
output = output.head(15)
output.rename(columns={'sum': 'Salary'}, inplace=True)


from matplotlib.ticker import FormatStrFormatter

myplot = output.plot(kind='bar',title='Baltimore Total Annual Salary by Job Title - 2014')
myplot.set_ylabel('$')
myplot.yaxis.set_major_formatter(FormatStrFormatter('%d'))



"""
import pandas as pd

baltimore = pd.read_csv('Baltimore_City_Employee_Salaries_FY2014.csv')

baltimore['AnnualSalary'] = baltimore['AnnualSalary'].replace('$', baltimore['AnnualSalary'].median())



"""
Code Challenge
  Name: 
    IGN Analysis
  Filename: 
    ign.py
  Problem Statement:
    Read the ign.csv file and perform the following task :
   
   Let's say we want to find games released for the Xbox One 
   that have a score of more than 7.
   
   review distribution for the Xbox One vs the review distribution 
   for the PlayStation 4.We can do this via a histogram, which will plot the 
   frequencies for different score ranges.
   
   
   
  Hint:

    The columns contain information about that game:

    score_phrase — how IGN described the game in one word. 
                   This is linked to the score it received.
    title — the name of the game.
    url — the URL where you can see the full review.
    platform — the platform the game was reviewed on (PC, PS4, etc).
    score — the score for the game, from 1.0 to 10.0.
    genre — the genre of the game.
    editors_choice — N if the game wasn't an editor's choice, Y if it was. This is tied to score.
    release_year — the year the game was released.
    release_month — the month the game was released.
    release_day — the day the game was released.



xbox_one_filter = (reviews["score"] > 7) & (reviews["platform"] == "Xbox One")
filtered_reviews = reviews[xbox_one_filter]
filtered_reviews.head()
      
%matplotlib inline
reviews[reviews["platform"] == "Xbox One"]["score"].plot(kind="hist")

reviews[reviews["platform"] == "PlayStation 4"]["score"].plot(kind="hist")

filtered_reviews["score"].hist()
        
"""

