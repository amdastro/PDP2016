# Import the necessary packages
import pylab as plt
import numpy as np
from matplotlib import rc
from scipy.optimize import curve_fit
import scipy.stats as stats
# Some plotting preferences
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
rc('text', usetex=True)
plt.rcParams['font.size'] = 18
plt.rcParams['legend.fontsize'] = 18
plt.rcParams['lines.linewidth'] = 2

# Read in the data by each column
year,jan,feb,mar,apr,may,jun,jul,aug,sep,oco,nov,dec,JmD,DmN,DJF,MAM,JJA,SON,yr\
=np.genfromtxt('../GIS_plots/GIST.txt',unpack=True,skip_footer=1)
#a = np.where(MAM < 900)


# Define a 'straight line' y=f(x)
#def f(x, A, B): 
#    return A*x + B

# Fit your data to a line
# This returns the slope and y-intercept of the fit
#A,B = curve_fit(f, year, JmD)[0] 


# Sample size
n = len(year)


# COMMENT ALL THIS

x = year
y = JmD

Sxx = np.sum(x**2) - np.sum(x)**2/n
Sxy = np.sum(x*y) - np.sum(x)*np.sum(y)/n

# Linefit
b = Sxy/Sxx
a = np.mean(y) - b*np.mean(x)

# Residuals
fit = lambda xx: a + b*xx    
residuals = y - fit(x)

var_res = np.sum(residuals**2)/(n-2)
sd_res = np.sqrt(var_res)

# Confidence intervals
se_b = sd_res/np.sqrt(Sxx)
se_a = sd_res*np.sqrt(np.sum(x**2)/(n*Sxx))


df = n-2                            # degrees of freedom
alpha=0.05
tval = stats.t.isf(alpha/2., df) 	# appropriate t value

ci_a = a + tval*se_a*np.array([-1,1])
ci_b = b + tval*se_b*np.array([-1,1])




# create series of new test x-values to predict for
npts = 100
px = np.linspace(np.min(x),np.max(x),num=npts)
    
se_fit     = lambda x: sd_res * np.sqrt(  1./n + (x-np.mean(x))**2/Sxx)
se_predict = lambda x: sd_res * np.sqrt(1+1./n + (x-np.mean(x))**2/Sxx)


# Return info
ri = {'residuals': residuals, 
    'var_res': var_res,
    'sd_res': sd_res,
    'alpha': alpha,
    'tval': tval,
    'df': df}

# Plot the data
plt.figure()
x.sort()
limit = (1-alpha)*100
plt.plot(x, fit(x)+tval*se_fit(x), 'r', label=r'Confidence limit ({0:.1f}\%)'.format(limit))
plt.plot(x, fit(x)-tval*se_fit(x), 'r')
plt.fill_between(x,fit(x)+tval*se_fit(x),fit(x)-tval*se_fit(x),color='red',alpha=0.2)


plt.plot(px, fit(px),'black', label='Regression line')
plt.plot(x,y, label='Sample observations',linestyle='none',marker='o',color='black',markersize=3)


        
plt.plot(x, fit(x)+tval*se_predict(x), 'c--', label=r'Prediction limit ({0:.1f}\%)'.format(limit))
plt.plot(x, fit(x)-tval*se_predict(x), 'c--')

plt.ylabel('(milli?) degrees')
plt.xlabel('year')
plt.title('Linear regression and confidence limits')
        
# configure legend
plt.legend(loc=0)
leg = plt.gca().get_legend()
ltext = leg.get_texts()
plt.setp(ltext, fontsize=10)

plt.show()


'''
# Plot it
plt.fill_between(year,f(year,A,B)+CI,f(year,A,B)-CI,color='#8258FA',alpha=0.5)
plt.plot(year,f(year,A,B)+CI,color='#8258FA',linewidth=2,label=r'$\rm CI$')
plt.plot(year,f(year,A,B)-CI,color='#8258FA',linewidth=2)
plt.plot(year,JmD,color='#0431B4',linewidth=2,label=r'$\rm annual \, mean$')
plt.plot(year,f(year,A,B),color='black',linewidth=2,label=r'$\rm fit$')
plt.plot(year,f(year,A,B)+se,color='grey',linestyle='--',linewidth=2,label=r'$\sigma$')
plt.plot(year,f(year,A,B)-se,color='grey',linewidth=2,linestyle='--')
plt.legend(loc=2)
plt.xlabel(r'$\rm year$')
plt.ylabel(r'$\rm 0.01 C/decade$')
plt.show()
'''