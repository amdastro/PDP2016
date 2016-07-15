###############################################################
###############################################################
# SAT scores by race/gender
###############################################################
###############################################################
# This code was taken from the College Board for college bound seniors in 2015
# We will use this to observe possible trends related to race/gender in the SAT


###############################################################
# Import useful packages that you import so you don't have to rewrite code
###############################################################
import numpy as np  # Has a ton of useful operations related to storing and accessing data
from matplotlib import pyplot as plt  # basic package used to plot data
import np.random.normal as norm 

# Range of scores
scores = np.array([200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800])

###############################################################
# Groups arranged by percentile order according to above scores
# including total number, mean and the standard deviation
# One could arrange this data in a cleaner way but I was lazy
###############################################################
# Male
mnum = 794802
mmean = 497
mstd = 119
mreadper = np.array([0, 2, 4, 10, 20, 34, 50, 65, 79, 89, 95, 98, 99])
mmathper = np.array([0, 1, 3, 7, 14, 26, 41, 56, 70, 82, 91, 95, 99])
mwritper = np.array([0, 2, 5, 12, 25, 41, 58, 72, 83, 91, 96, 98, 99])
mread = np.round(mnum*mreadper/100.)
mmath = np.round(mnum*mmathper/100.)
mwrit = np.round(mnum*mwritper/100.)
mreaddat = norm(mmean, mstd, size=mnum)
mreaddat = mreaddat[np.where((mreaddat > 200) & (mreaddat < 800))]


# Female
fnum = 903719
fmean = 493
fstd = 113
freadper = np.array([0, 1, 3, 9, 19, 35, 52, 68, 82, 91, 96, 98, 99])
fmathper = np.array([0, 1, 3, 9, 19, 35, 52, 67, 80, 89, 95, 98, 99])
fwritper = np.array([0, 1, 3, 9, 20, 37, 54, 70, 82, 90, 96, 98, 99])
fread = np.round(fnum*freadper/100.)
fmath = np.round(fnum*fmathper/100.)
fwrit = np.round(fnum*fwritper/100.)

# Black
blnum = 219018
blmean = 431
blstd = 101
blreadper = np.array([0, 3, 7, 18, 37, 59, 75, 87, 94, 98, 99, 99, 99])
blmathper = np.array([0, 3, 8, 20, 39, 59, 76, 88, 94, 98, 99, 99, 99])
blwritper = np.array([0, 3, 8, 22, 43, 65, 80, 90, 95, 98, 99, 99, 99])
blread = np.round(blnum*blreadper/100.)
blmath = np.round(blnum*blmathper/100.)
blwrit = np.round(blnum*blwritper/100.)

# American Indian
ainnum = 10031
ainmean = 481
ainstd = 108
ainreadper = np.array([0, 2, 4, 10, 21, 38, 56, 72, 85, 94, 98, 99, 99])
ainmathper = np.array([0, 1, 3, 10, 21, 37, 56, 73, 85, 93, 97, 99, 99])
ainwritper = np.array([0, 1, 3, 12, 27, 47, 65, 80, 90, 95, 99, 99, 99])
fread = np.round(fnum*freadper/100.)
fmath = np.round(fnum*fmathper/100.)
fwrit = np.round(fnum*fwritper/100.)


# Asian
asnum = 211238
asmean = 525
asstd = 126
asreadper = np.array([0, 2, 3, 8, 15, 27, 41, 56, 70, 82, 91, 96, 98])
asmathper = np.array([0, 1, 1, 3, 7, 13, 22, 34, 46, 60, 75, 86, 95])
aswritper = np.array([0, 1, 3, 7, 15, 27, 41, 54, 67, 79, 89, 95, 99])
asread = np.round(asnum*asreadper/100.)
asmath = np.round(asnum*asmathper/100.)
aswrit = np.round(asnum*aswritper/100.)

# Mexican
mexnum = 130026
mexmean = 448
mexstd = 98
mexreadper = np.array([0, 2, 5, 14, 30, 51, 70, 84, 93, 97, 99, 99, 99])
mexmathper = np.array([0, 1, 4, 12, 26, 47, 66, 82, 91, 96, 99, 99, 99])
mexwritper = np.array([0, 1, 5, 14, 33, 56, 76, 87, 94, 98, 99, 99, 99])
mexread = np.round(mexnum*mexreadper/100.)
mexmath = np.round(mexnum*mexmathper/100.)
mexwrit = np.round(mexnum*mexwritper/100.)

# Puerto Rican
prnum = 30192
prmean = 456
prstd = 105
prreadper = np.array([0, 2, 6, 14, 28, 48, 66, 80, 90, 96, 99, 99, 99])
prmathper = np.array([0, 2, 6, 16, 31, 50, 68, 81, 91, 96, 99, 99, 99])
prwritper = np.array([0, 2, 6, 16, 33, 53, 71, 84, 92, 97, 99, 99, 99])
prread = np.round(prnum*prreadper/100.)
prmath = np.round(prnum*prmathper/100.)
prwrit = np.round(prnum*prwritper/100.)

# Latin American
lanum = 162655
lamean = 449
lastd = 107
lareadper = np.array([0, 3, 6, 16, 32, 51, 68, 81, 91, 96, 99, 99, 99])
lamathper = np.array([0, 2, 5, 14, 29, 48, 66, 80, 89, 95, 98, 99, 99])
lawritper = np.array([0, 2, 6, 17, 35, 56, 73, 85, 92, 97, 99, 99, 99])
laread = np.round(lanum*lareadper/100.)
lamath = np.round(lanum*lamathper/100.)
lawrit = np.round(lanum*lawritper/100.)

# White
whnum = 800236
whmean = 529
whstd = 103
whreadper = np.array([0, 1, 1, 3, 9, 21, 38, 57, 74, 87, 94, 98, 99])
whmathper = np.array([0, 1, 1, 3, 9, 20, 36, 55, 72, 85, 94, 98, 99])
whwritper = np.array([0, 1, 1, 4, 12, 27, 45, 63, 78, 89, 95, 98, 99])
whread = np.round(whnum*whreadper/100.)
whmath = np.round(whnum*whmathper/100.)
whwrit = np.round(whnum*whwritper/100.)

# Other
otnum = 65063
otmean = 490
otstd = 124
otreadper = np.array([0, 3, 6, 12, 22, 37, 53, 67, 79, 89, 95, 98, 99])
otmathper = np.array([0, 1, 3, 8, 16, 29, 44, 59, 72, 83, 92, 96, 99])
otwritper = np.array([0, 3, 5, 11, 22, 38, 55, 69, 81, 89, 95, 98, 99])
otread = np.round(otnum*otreadper/100.)
otmath = np.round(otnum*otmathper/100.)
otwrit = np.round(otnum*otwritper/100.)

###############################################################
# Confidence intervals
###############################################################
# We can calculate confidence intervals for each dataset according to the size, #, and std

# For 95% confidence, we get z = 1.96 from a z-table
z = 1.96

# Here we just calculate the CI for three groups, asian, mexican and white
whconf = z * whstd/ np.sqrt(whnum)
mexconf = z * mexstd/ np.sqrt(mexnum)
asconf = z * asstd/ np.sqrt(asnum)


###############################################################
# Now that the data is loaded, we can make plots
###############################################################
# Format is plt.plot(x, y, *insert keywords*)
# The keywords include things that can change the color, shape, etc. of the ploted data
# Here we use a simple label to label the data and at the end use plt.legend() to make a
# Legend and show the labels

'''
nope
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
'''

# Another plotting tool uses scatterpoints, whereas plot makes lines. The format is the same
# We first plot the actual data
plt.scatter(scores, whread, c='red',  label='white')
plt.scatter(scores, mexread, c='blue', label='mexican')
plt.scatter(scores, asread, c='green', label='asian')

# Then we create the upper and lower confidence intervals for the data
plt.plot(scores, whread+whconf, c='red')
plt.plot(scores, whread-whconf, c='red')
plt.plot(scores, mexread+mexconf, c='blue')
plt.plot(scores, mexread-mexconf, c='blue')
plt.plot(scores, asread+asconf, c='green')
plt.plot(scores, asread-asconf, c='green')

# We create a legend
plt.legend(loc=4, scatterpoints=1)

# Now we use this command to plot the data
plt.show()