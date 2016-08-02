import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt("noage_esoph.csv",delimiter=",",skip_header=1,dtype='str')

alc=[]     #  grams per day
tob=[]     #  grams per day
ncases=[]

for row in data:
    alc.append(float(row[0]))
    tob.append(float(row[1]))
    ncases.append(float(row[2]))


alc = np.array(alc)
tob = np.array(tob)
ncases = np.array(ncases)

### find unique values of the arrays
unique_alc = np.unique(alc)
unique_tob = np.unique(tob)

### fit the line using polyfit  ###
fit = np.polyfit(tob,ncases,1)
#  answer is in the form y = mx + b  where fit[1] is b and fit[0] is m
answer = fit[0]*tob+fit[1]

### plot the things.
plt.scatter(tob,ncases)
plt.plot(tob,answer)
plt.xlabel("tobacco use (grams/day)")
plt.ylabel("# of cases")
plt.show()
