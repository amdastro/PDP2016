# Import the numpy package
import numpy as np

# --------------------------------- #
# Here is ONE way to fit a line to a set of data points.

# Define a function that gives a 'straight line' y=f(x)
def f(x, A, B): 
   return A*x + B

# Fit your data to a line
# This returns the slope and y-intercept of the fit
# B = slope
# A = y=intercept
from scipy.optimize import curve_fit
B,A = curve_fit(f, year, JmD)[0]



# --------------------------------- #
# You can also get a line fit by using statistics. 

# First you need to define the sample size of the data (the number of points).
# Change x to whatever your x-axis is
n = len(x)

# Calculate the sum of the squares of the x and y values.
# This is basically a measure of the deviation from the mean. 
Sxx = np.sum(x**2) - np.sum(x)**2/n
Sxy = np.sum(x*y) - np.sum(x)*np.sum(y)/n

# We can then get the slope (b) and the y-intercept (a)
b = Sxy/Sxx
a = np.mean(y) - b*np.mean(x)


