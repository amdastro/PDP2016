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

### plot the things.
plt.scatter(tob,ncases)
plt.xlabel("tobacco use (grams/day)")
plt.ylabel("# of cases")
plt.show()
