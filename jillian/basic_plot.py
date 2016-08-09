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

##  read in the data file  ##
##  columns separated by commas.  We don't want the first row.
data = np.genfromtxt("noage_esoph.csv",delimiter=",",skip_header=1,dtype='str')

# the result "data" is a matrix of all of the information.
# Now we need to organize it a little bit.
alc = data[:,0]
tob = data[:,1]
ncases = data[:,2]


# turn them into numpy arrays so we can do math with them
alc = np.array(alc)
tob = np.array(tob)
ncases = np.array(ncases)

### plot the things.
plt.scatter(tob,ncases)
plt.xlabel("tobacco use (grams/day)")
plt.ylabel("# of cases")
plt.show()
