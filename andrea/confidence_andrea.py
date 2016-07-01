# Import the necessary packages
import pylab as plt
import numpy as np
from matplotlib import rc
from scipy.optimize import curve_fit
# Some plotting preferences
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
rc('text', usetex=True)
plt.rcParams['font.size'] = 18
plt.rcParams['legend.fontsize'] = 18
plt.rcParams['lines.linewidth'] = 2

# Read in the data by each column
year,jan,feb,mar,apr,may,jun,jul,aug,sep,oco,nov,dec,JmD,DmN,DJF,MAM,JJA,SON,yr\
=np.genfromtxt('GIS_plots/GIST.txt',unpack=True,skip_footer=1)
a = np.where(MAM < 900)


# Define a 'straight line' y=f(x)
def f(x, A, B): 
    return A*x + B

# Fit your data to a line
# This returns the slope and y-intercept of the fit
A,B = curve_fit(f, year[a], JmD[a])[0] 


# ---------------------------------
# Everything below is taken 
# from http://www.sjsu.edu/faculty/gerstman/StatPrimer/regression.pdf
# Calculate the standard error of the regression
# First the sum of squares of X and Y values:
SSyy = np.sum((JmD - np.mean(JmD))**2)
SSxx = np.sum((year - np.mean(year))**2)
SSxy = np.sum((year - np.mean(year))*(JmD - np.mean(JmD)))
# Sample size
n = len(year[a])
# Standard error of the regression:
se_reg = (SSyy - B*SSxy/(n-2))**0.5
# Standard error of the slope:
#se = se_reg / SSxx**0.5
# 95% confidence interval
# CI = Z * sigma/sqrt(n)
# Look up Z from a table for 95% 
#CI = 1.96*se/n**0.5
# Something wrong with this, cause CI is way too small
# ----------------------------

# Not sure about above, let's try something simpler
# Compute the standard deviation of the residuals
se = (np.sum((JmD - np.mean(JmD))**2)/n)**0.5
CI = 1.96*se/n**0.5
t_value = 2. # Look this up
# This gives a stupidly small CI too?
#CI = t_value*se*np.sqrt(1/n + (year -np.mean(year))**2/(n-1)/SSxx**2)


#------------------------------
# Ok, let's try these equations again
# A confidence interval is given by the 
# sum of the squares of the standard error of the mean
# and the standard error of the slope

# First I should shift my data so that 
# it is centered about the mean: 

# Then I can compute the standard deviation:

# and get the standard error of the mean 
# by dividing by the sqrt of the sample size:

# Then I can get the standard error of the 
# slope of the shifted line at the mean:

# Now the error on the slope at some *other* value of x
# Is the error on the slope times some distance from the mean:

# Now we can get the standard error of 
# an estimate of the mean at some other value of x:

# If you plot this as a function of x, 
# It should look like a curve:







# Plot it
plt.fill_between(year,f(year,A,B)+CI,f(year,A,B)-CI,color='#8258FA',alpha=0.5)
plt.plot(year,f(year,A,B)+CI,color='#8258FA',linewidth=2,label=r'$\rm CI$')
plt.plot(year,f(year,A,B)-CI,color='#8258FA',linewidth=2)
plt.plot(year[a],JmD[a],color='#0431B4',linewidth=2,label=r'$\rm annual \, mean$')
plt.plot(year,f(year,A,B),color='black',linewidth=2,label=r'$\rm fit$')
plt.plot(year,f(year,A,B)+se,color='grey',linestyle='--',linewidth=2,label=r'$\sigma$')
plt.plot(year,f(year,A,B)-se,color='grey',linewidth=2,linestyle='--')
plt.legend(loc=2)
plt.xlabel(r'$\rm year$')
plt.ylabel(r'$\rm 0.01 C/decade$')
plt.show()