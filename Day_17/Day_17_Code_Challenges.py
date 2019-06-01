
"""
Q. (Create a program that fulfills the following specification.)
Female_Stats.Csv

Female Stat Students

 

Import The Female_Stats.Csv File

The Data Are From N = 214 Females In Statistics Classes At The University Of California At Davi.

Column1 = Student’s Self-Reported Height,

Column2 = Student’s Guess At Her Mother’s Height, And

Column 3 = Student’s Guess At Her Father’s Height. All Heights Are In Inches.

 

Build A Predictive Model And Conclude If Both Predictors (Independent Variables) Are Significant For A Students’ Height Or Not
When Father’s Height Is Held Constant, The Average Student Height Increases By How Many Inches For Each One-Inch Increase In Mother’s Height.
When Mother’s Height Is Held Constant, The Average Student Height Increases By How Many Inches For Each One-Inch Increase In Father’s Height.
"""
import statsmodels.api as sm
import pandas as pd
dataset = pd.read_csv('Female_Stats.csv')

features = dataset.iloc[:, 1:]
labels = dataset.iloc[:, 0]

features_opt = sm.add_constant(features)
model = sm.OLS(endog = labels, exog = features_opt).fit()
print(model.pvalues)

print('Mom\'s height effect :', model.params['momheight'])
print('Dad\'s height effect :', model.params['dadheight'])

"""
Q. (Create a program that fulfills the following specification.)
bluegills.csv

How is the length of a bluegill fish related to its age?

In 1981, n = 78 bluegills were randomly sampled from Lake Mary in Minnesota. The researchers (Cook and Weisberg, 1999) measured and recorded the following data (Import bluegills.csv File)

Response variable(Dependent): length (in mm) of the fish

Potential Predictor (Independent Variable): age (in years) of the fish

    How is the length of a bluegill fish best related to its age? (Linear/Quadratic nature?)
    What is the length of a randomly selected five-year-old bluegill fish? Perform polynomial regression on the dataset.

NOTE: Observe that 80.1% of the variation in the length of bluegill fish is reduced by taking into account a quadratic function of the age of the fish.
"""
from sklearn.linear_model import LinearRegression
import pandas as pd, numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures


data = pd.read_csv('bluegills.csv').sort_values(by = 'age')

features = data.iloc[:, 0:1].values 
labels = data.iloc[:, 1].values

regressor = LinearRegression()
regressor.fit(features, labels)
plt.scatter(features, labels)
plt.plot(features, regressor.predict(features))
poly_data = PolynomialFeatures(degree = 10)
features_poly = poly_data.fit_transform(features)
print(regressor.predict(data))
print(regressor.score(features, labels))
regressor_poly = LinearRegression()
regressor_poly.fit(features_poly, labels)

plt.scatter(features, labels)
plt.plot(features, regressor_poly.predict(poly_data.fit_transform(features)))
data = np.array(5).reshape(1, 1)
print(regressor_poly.predict(poly_data.transform(data)))
print(regressor_poly.score(features_poly, labels))

"""
Q. (Create a program that fulfills the following specification.)
iq_size.csv

Are a person's brain size and body size (Height and weight) predictive of his or her intelligence?

 

Import the iq_size.csv file

It Contains the details of 38 students, where

Column 1: The intelligence (PIQ) of students

Column 2:  The brain size (MRI) of students (given as count/10,000).

Column 3: The height (Height) of students (inches)

Column 4: The weight (Weight) of student (pounds)

    What is the IQ of an individual with a given brain size of 90, height of 70 inches, and weight 150 pounds ? 
    Build an optimal model and conclude which is more useful in predicting intelligence Height, Weight or brain size.
"""






