#### the format of the original datafile columns are like so:  ###

#[,0] 	"alcgp" 	Alcohol consumption
#                       1 0--39 gm/day
#			2 40--79
#			3 80--119
#			4 120+
#[,1] 	"tobgp" 	Tobacco consumption
#                       1 0-- 9 gm/day
#			2 10--19
#			3 20--29
#			4 30+
#[,2] 	"ncases" 	Number of cases 	
###################################################

# import some libraries that we will need
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

## create some arrays with the ranges of data above.  Use the middle value.
age_range = [30, 40, 50, 60, 70, 80]
alc_range = [20, 60, 100, 140]
tob_range = [5, 15, 25, 35]

##  read in the data file  ##
##  columns separated by commas.  We want columns 1-5, and not the first row.
data = np.genfromtxt("noage_esoph.csv",delimiter=",",skip_header=1)

# the result "data" is a matrix of all of the information.  Now we need to organize it a little bit.

alc = data[:,0]
tob = data[:,1]
ncases = data[:,2]

# turn them into numpy arrays so we can do math with them
alc = np.array(alc)
tob = np.array(tob)
ncases = np.array(ncases)

### find unique values of the arrays
unique_alc = np.unique(alc)
unique_tob = np.unique(tob)


### OK we will find the trend for tobacco use and N cases
# fit a line to the data using polyfit
# the "1" at the end means Linear
answer = np.polyfit(tob,ncases,1)
# use the fit to create an array of Y values
# we'll use this to plot a line later
fit = answer[0]*np.array(unique_tob) + answer[1]

####  creating confidence intervals!!  #####
#  x value is tobacco use  (could change later!)
#  y value is number of cases
#  we are going to use some functions, so our code will be more flexible later

# SSx function
def SSx(x):
    n = len(x)
    return np.sum(x**2.) - (np.sum(x))**2./n

#  SSxy function
def SSxy(x,y):
    n = len(x)
    return np.sum(x*y) - np.sum(x)*np.sum(y)/n

def linear_regression(x,y):
    # fits linear regression and returns slope, incercept, and goodness of fit
    m = SSxy(x,y)/SSx(x)
    b = np.mean(y) - m*np.mean(x)
    r = SSxy(x,y)/np.sqrt(SSx(x)*SSx(y))
    return m,b,r

def sigma(x):
    n = len(x)
    return np.sqrt(SSx(x)/n)

def Syx(x,y):
    m,b,r = linear_regression(x,y)
    return sigma(y)*np.sqrt(1.-r*r)

#########################################################################
# OK, what do you want your variables to be?
# these are the things to change if you wnat a new plot/prediction!!
#########################################################################
x = tob
y = ncases
unique_x = unique_tob
#########################################################################

### now let's plot the confidence intervals  ##
ny = len(y)
conf = 0.95  # what conf. interval do we want? currently 95%
alpha = 1.-conf
df = ny-2            # degrees of freedom = N-2 
std_err = Syx(x,y)   #  standard error
SSX = SSx(x)         
x_mean = np.mean(x)  # the mean of x
t = stats.t.isf(alpha/2.,df)   # what is this?
conf_int = t*std_err*np.sqrt(1./ny + (unique_x-x_mean)**2./SSX)
print conf_int  # make sure it's not cray


##### PLOTTING  #####

# selects a color map which I want for plotting
cm = plt.get_cmap("nipy_spectral")
# creates a scatter plot with the chosen parameters
image=plt.scatter(tob,ncases,c=alc,vmin=00,vmax=130,cmap=cm)
plt.ylabel("N Cancer Cases")
plt.xlabel("Tobacco Use")
# makes the colorbar
bar = plt.colorbar(image)
bar.set_label("alcohol")
# use the result from our fit to
plt.plot(unique_tob,fit)
# plot the confidence intervals
plt.plot(unique_tob,fit+conf_int)
plt.plot(unique_tob,fit-conf_int)
plt.show()
# uncomment the line below to save the plot to a file
#plt.savefig("esoph.png")

