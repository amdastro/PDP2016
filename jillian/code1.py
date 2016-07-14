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
data = np.genfromtxt("averages_esoph.csv",delimiter=",",usecols=(1,2,3,4,5),skip_header=1,dtype='str')

# the result "data" is a matrix of all of the information.  Now we need to organize it a little bit.

# separate the data by e.g. smoking
ncases=[]
ncontrol = []
count = 0
for count in range(len(tob_range)):
    n=0
    n2=0
    for row in data:
        if int(row[2]) == tob_range[count]:
            n += float(row[3])
            n2 += float(row[4])
    ncases.append(n)
    ncontrol.append(n2)

plt.plot(tob_range,ncases,label='have cancer')
#plt.plot(tob_range,ncontrol,label='no cancer')
plt.xlabel("tobacco use")
plt.xlim=[0,40]
plt.ylabel("number of cancer cases")
#plt.legend()
plt.show()

# separate the data by e.g. alcohol
ncases=[]
ncontrol = []
count = 0
for count in range(len(alc_range)):
    n=0
    n2=0
    for row in data:
        if int(row[1]) == alc_range[count]:
            n += float(row[3])
            n2 += float(row[4])
    ncases.append(n)
    ncontrol.append(n2)


plt.plot(alc_range,ncases,label='have cancer')
#plt.plot(alc_range,ncontrol,label='no cancer')
plt.xlabel("alcohol use")
#plt.xlim=[0,40]
plt.ylabel("number of cancer cases")
#plt.legend()
plt.show()


# separate the data by e.g. age
ncases=[]
ncontrol = []
count = 0
for count in range(len(age_range)):
    n=0
    n2=0
    for row in data:
        if int(row[0]) == age_range[count]:
            n += float(row[3])
            n2 += float(row[4])
    ncases.append(n)
    ncontrol.append(n2)


plt.plot(age_range,ncases,label='have cancer')
#plt.plot(age_range,ncontrol,label='no cancer')
plt.xlabel(" age ")
#plt.xlim=[0,40]
plt.ylabel("number of cancer cases")
#plt.legend()
plt.show()




"""

##### calculate a confidence interval?  #####
# fit a line to the data using polyfit
# the "1" at the end means Linear
answer = np.polyfit(alc,fraction,1)
# use the fit to create an array of Y values
# we'll use this to plot a line later
unique_answer = answer[0]*np.array(unique_alc) + answer[1]


#### for each alcohol content, find the fraction data statistics ###
sigmas = []
for entry in unique_alc:  # loop through each unique alcohol value
    tally=[]
    for i in range(len(alc)):
        if alc[i] == entry:
            #  keep a tally of how many of each entry there are
            tally.append(fraction[i])
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

