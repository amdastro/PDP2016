#### the format of the datafile columns are like so:  ###

#[,1] 	"agegp" 	Age group
#                       1 25--34 years
#			2 35--44
#			3 45--54
#			4 55--64
#			5 65--74
#			6 75+
#[,2] 	"alcgp" 	Alcohol consumption
#                       1 0--39 gm/day
#			2 40--79
#			3 80--119
#			4 120+
#[,3] 	"tobgp" 	Tobacco consumption
#                       1 0-- 9 gm/day
#			2 10--19
#			3 20--29
#			4 30+
#[,4] 	"ncases" 	Number of cases 	
#[,5] 	"ncontrols" 	Number of controls

###################################################

# import some libraries that we will need
import numpy as np
import matplotlib.pyplot as plt

## create some arrays with the ranges of data above.  Use the middle value.
age_range = [30, 40, 50, 60, 70, 80]
alc_range = [20, 60, 100, 140]
tob_range = [5, 15, 25, 35]

##  read in the data file  ##
##  columns separated by commas.  We want columns 1-5, and not the first row.
data = np.genfromtxt("noage_esoph.csv",delimiter=",",skip_header=1,dtype='str')

# the result "data" is a matrix of all of the information.  Now we need to organize it a little bit.

# these are some empty placeholder lists
# we will fill them with data
alc = []
tob = []
ncases=[]

## this "for loop" iterates through every row in the "data" matrix
## it fills our lists with the correct data

for row in data:
    alc.append(float(row[0]))
    tob.append(float(row[1]))
    ncases.append(float(row[2]))

# count the number of entries in the arrays
n = len(alc)

### find unique values of the arrays
unique_alc = np.unique(alc)
#unique_alc = [float(x) for x in unique_alc]
unique_tob = np.unique(tob)
print unique_tob
print type(unique_tob)

### OK we will find the trend for tobacco use and N cases
##### calculate a confidence interval?  #####
# fit a line to the data using polyfit
# the "1" at the end means Linear
answer = np.polyfit(tob,ncases,1)
# use the fit to create an array of Y values
# we'll use this to plot a line later
fit = answer[0]*np.array(unique_tob) + answer[1]




"""

#### for each alcohol content, find the number of cases ###
sigmas = []
for entry in unique_alc:  # loop through each unique alcohol value
    tally=[]
    for i in range(len(alc)):
        if alc[i] == entry:
            #  keep a tally of how many of each entry there are
            tally.append(ncases[i])
        # once we have tally, do statistics.    
        average = np.mean(tally)
        stddev = np.std(tally)
        median = np.median(tally)
    print "for alc ",str(entry)
    print average,stddev,median
    sigmas.append(float(stddev))  # list of standard deviations

sigmas = np.array(sigmas)  # convert to numpy array so we can do math
"""
"""
TERRIBLENESS IGNORE THIS

s_yx = np.sqrt((1./(n-2.0))* ( np.sum((np.array(fraction)-np.mean(fraction))**2.0) - ( (np.sum(np.array(alc)-np.mean(alc))*(np.array(fraction)-np.mean(fraction)))**2. / (np.sum((np.array(alc)-np.mean(alc))**2.) ))))
#print s_yx
SSx = np.sum((np.array(fraction) - np.mean(fraction))**2.0)
#print fraction
#print np.mean(fraction)
#print SSx
se =  s_yx * np.sqrt(1./np.array(n) + ((np.array(fraction) - np.mean(fraction))**2.0/SSx))
#print "****"
#print se
"""


"""
######  PLOTTING COMMANDS  #########

# now let's plot some error lines
#plt.plot(unique_alc,unique_answer+sigmas/2.0)
#plt.plot(unique_alc,unique_answer-sigmas/2.0)
# displays the plot
plt.show()


"""
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
plt.show()
# uncomment the line below to save the plot to a file
#plt.savefig("esoph.png")




"""
cm = plt.get_cmap("nipy_spectral")
image=plt.scatter(alc,ncases,c=tob,vmin=0,vmax=40,cmap=cm)
plt.ylabel("N Cancer Cases")
plt.xlabel("Alcohol Use")
bar = plt.colorbar(image)
bar.set_label("tobacco")
plt.show()
"""
