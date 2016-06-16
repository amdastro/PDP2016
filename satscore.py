import numpy as np
from matplotlib import pyplot as plt
import matplotlib
matplotlib.rcParams['figure.figsize'] = 16, 8
matplotlib.rcParams['font.size'] = 20


#Scores
scores = [200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800]

# Males
mnum = 794802
mmean = 497
mstd = 119
mread = [0, 2, 4, 10, 20, 34, 50, 65, 79, 89, 95, 98, 99]
mmath = [0, 1, 3, 7, 14, 26, 41, 56, 70, 82, 91, 95, 99]
mwrit = [0, 2, 5, 12, 25, 41, 58, 72, 83, 91, 96, 98, 99]

# females
fnum = 903719
fmean = 493
fstd = 113
fread = [0, 1, 3, 9, 19, 35, 52, 68, 82, 91, 96, 98, 99]
fmath = [0, 1, 3, 9, 19, 35, 52, 67, 80, 89, 95, 98, 99]
fwrit = [0, 1, 3, 9, 20, 37, 54, 70, 82, 90, 96, 98, 99]

# Black
blnum = 219018
blmean = 431
blstd = 101
blread = [0, 3, 7, 18, 37, 59, 75, 87, 94, 98, 99, 99, 99]
blmath = [0, 3, 8, 20, 39, 59, 76, 88, 94, 98, 99, 99, 99]
blwrit = [0, 3, 8, 22, 43, 65, 80, 90, 95, 98, 99, 99, 99]

# amind
ainnum = 10031
ainmean = 481
ainstd = 108
ainread = [0, 2, 4, 10, 21, 38, 56, 72, 85, 94, 98, 99, 99]
ainmath = [0, 1, 3, 10, 21, 37, 56, 73, 85, 93, 97, 99, 99]
ainwrit = [0, 1, 3, 12, 27, 47, 65, 80, 90, 95, 99, 99, 99]

# asian
asnum = 211238
asmean = 525
asstd = 126
asread = [0, 2, 3, 8, 15, 27, 41, 56, 70, 82, 91, 96, 98]
asmath = [0, 1, 1, 3, 7, 13, 22, 34, 46, 60, 75, 86, 95]
aswrit = [0, 1, 3, 7, 15, 27, 41, 54, 67, 79, 89, 95, 99]

# mexican
mexnum = 130026
mexmean = 448
mexstd = 98
mexread = [0, 2, 5, 14, 30, 51, 70, 84, 93, 97, 99, 99, 99]
mexmath = [0, 1, 4, 12, 26, 47, 66, 82, 91, 96, 99, 99, 99]
mexwrit = [0, 1, 5, 14, 33, 56, 76, 87, 94, 98, 99, 99, 99]

# puerto rican
prnum = 30192
prmean = 456
prstd = 105
prread = [0, 2, 6, 14, 28, 48, 66, 80, 90, 96, 99, 99, 99]
prmath = [0, 2, 6, 16, 31, 50, 68, 81, 91, 96, 99, 99, 99]
prwrit = [0, 2, 6, 16, 33, 53, 71, 84, 92, 97, 99, 99, 99]

# latin american
lanum = 162655
lamean = 449
lastd = 107
laread = [0, 3, 6, 16, 32, 51, 68, 81, 91, 96, 99, 99, 99]
lamath = [0, 2, 5, 14, 29, 48, 66, 80, 89, 95, 98, 99, 99]
lawrit = [0, 2, 6, 17, 35, 56, 73, 85, 92, 97, 99, 99, 99]

# white
whnum = 800236
whmean = 529
whstd = 103
whread = [0, 1, 1, 3, 9, 21, 38, 57, 74, 87, 94, 98, 99]
whmath = [0, 1, 1, 3, 9, 20, 36, 55, 72, 85, 94, 98, 99]
whwrit = [0, 1, 1, 4, 12, 27, 45, 63, 78, 89, 95, 98, 99]

# other
otnum = 65063
otmean = 490
otstd = 124
otread = [0, 3, 6, 12, 22, 37, 53, 67, 79, 89, 95, 98, 99]
otmath = [0, 1, 3, 8, 16, 29, 44, 59, 72, 83, 92, 96, 99]
otwrit = [0, 3, 5, 11, 22, 38, 55, 69, 81, 89, 95, 98, 99]

plt.plot(scores, mread, label='male')
plt.plot(scores, fread, label='female')
plt.plot(scores, blread, label='black')
plt.plot(scores, ainread, label='NatAm')
plt.plot(scores, asread, label='asian')
plt.plot(scores, mexread, label='mexican')
plt.plot(scores, prread, label='PR')
plt.plot(scores, laread, label='LatAm')
plt.plot(scores, whread, label='white')
plt.plot(scores, otread, label='other')


# For 95% confidence

z = 1.96
whconf = z * whstd/ np.sqrt(whnum)
mexconf = z * mexstd/ np.sqrt(mexnum)
asconf = z * asstd/ np.sqrt(asnum)

plt.scatter(scores, whread, c='red',  label='white')
plt.scatter(scores, mexread, c='blue', label='mexican')
plt.scatter(scores, asread, c='green', label='asian')

plt.legend(loc=4, scatterpoints=1)
plt.plot(scores, whread+whconf, c='red')
plt.plot(scores, whread-whconf, c='red')
plt.plot(scores, mexread+mexconf, c='blue')
plt.plot(scores, mexread-mexconf, c='blue')

plt.plot(scores, asread+asconf, c='green')
plt.plot(scores, asread-asconf, c='green')
