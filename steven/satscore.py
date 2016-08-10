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
import numpy.random as ran
import scipy.stats as stats

# Range of scores
scores = np.array([200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800])

###############################################################
# Groups arranged by percentile order according to above scores
# including total number, mean and the standard deviation
# One could arrange this data in a cleaner way but I was lazy
###############################################################
# Male
mnum = 794802
mreadmean = 497
mreadstd = 119
mmathmean = 527
mmathstd = 124
mwritmean = 478
mwritstd = 117

# Percentile scores
mreadper = np.array([0, 2, 4, 10, 20, 34, 50, 65, 79, 89, 95, 98, 99])
mmathper = np.array([0, 1, 3, 7, 14, 26, 41, 56, 70, 82, 91, 95, 99])
mwritper = np.array([0, 2, 5, 12, 25, 41, 58, 72, 83, 91, 96, 98, 99])

# Number of people at a particular percentile
mread = np.round(mnum * mreadper / 100.)
mmath = np.round(mnum * mmathper / 100.)
mwrit = np.round(mnum * mwritper / 100.)

# Scores for those people
mreaddat = ran.normal(mreadmean, mreadstd, size=mnum)
mreaddat = mreaddat[np.where((mreaddat > 200) & (mreaddat < 800))]
mmathdat = ran.normal(mmathmean, mmathstd, size=mnum)
mmathdat = mmathdat[np.where((mmathdat > 200) & (mmathdat < 800))]
mwritdat = ran.normal(mwritmean, mwritstd, size=mnum)
mwritdat = mwritdat[np.where((mwritdat > 200) & (mwritdat < 800))]

# Female
fnum = 903719
freadmean = 493
freadstd = 113
fmathmean = 496
fmathstd = 115
fwritmean = 490
fwritstd = 113

freadper = np.array([0, 1, 3, 9, 19, 35, 52, 68, 82, 91, 96, 98, 99])
fmathper = np.array([0, 1, 3, 9, 19, 35, 52, 67, 80, 89, 95, 98, 99])
fwritper = np.array([0, 1, 3, 9, 20, 37, 54, 70, 82, 90, 96, 98, 99])

fread = np.round(fnum*freadper/100.)
fmath = np.round(fnum*fmathper/100.)
fwrit = np.round(fnum*fwritper/100.)

freaddat = ran.normal(freadmean, freadstd, size=fnum)
freaddat = freaddat[np.where((freaddat > 200) & (freaddat < 800))]
fmathdat = ran.normal(fmathmean, fmathstd, size=fnum)
fmathdat = fmathdat[np.where((fmathdat > 200) & (fmathdat < 800))]
fwritdat = ran.normal(fwritmean, fwritstd, size=fnum)
fwritdat = fwritdat[np.where((fwritdat > 200) & (fwritdat < 800))]

# Black
blnum = 219018
blreadmean = 431
blreadstd = 101
blmathmean = 428
blmathstd = 100
blwritmean = 418
blwritstd = 96

blreadper = np.array([0, 3, 7, 18, 37, 59, 75, 87, 94, 98, 99, 99, 99])
blmathper = np.array([0, 3, 8, 20, 39, 59, 76, 88, 94, 98, 99, 99, 99])
blwritper = np.array([0, 3, 8, 22, 43, 65, 80, 90, 95, 98, 99, 99, 99])

blread = np.round(blnum*blreadper/100.)
blmath = np.round(blnum*blmathper/100.)
blwrit = np.round(blnum*blwritper/100.)

blreaddat = ran.normal(blreadmean, blreadstd, size=blnum)
blreaddat = mreaddat[np.where((blreaddat > 200) & (blreaddat < 800))]
blmathdat = ran.normal(blmathmean, blmathstd, size=blnum)
blmathdat = blmathdat[np.where((blmathdat > 200) & (blmathdat < 800))]
blwritdat = ran.normal(blwritmean, blwritstd, size=blnum)
blwritdat = blwritdat[np.where((blwritdat > 200) & (blwritdat < 800))]


# American Indian
ainnum = 10031
ainreadmean = 481
ainreadstd = 108
ainmathmean = 482
ainmathstd = 107
ainwritmean = 460
ainwritstd = 103

ainreadper = np.array([0, 2, 4, 10, 21, 38, 56, 72, 85, 94, 98, 99, 99])
ainmathper = np.array([0, 1, 3, 10, 21, 37, 56, 73, 85, 93, 97, 99, 99])
ainwritper = np.array([0, 1, 3, 12, 27, 47, 65, 80, 90, 95, 99, 99, 99])

fread = np.round(fnum*freadper/100.)
fmath = np.round(fnum*fmathper/100.)
fwrit = np.round(fnum*fwritper/100.)

ainreaddat = ran.normal(ainreadmean, ainreadstd, size=ainnum)
ainreaddat = ainreaddat[np.where((ainreaddat > 200) & (ainreaddat < 800))]
ainmathdat = ran.normal(ainmathmean, ainmathstd, size=ainnum)
ainmathdat = ainmathdat[np.where((ainmathdat > 200) & (ainmathdat < 800))]
ainwritdat = ran.normal(ainwritmean, ainwritstd, size=ainnum)
ainwritdat = ainwritdat[np.where((ainwritdat > 200) & (ainwritdat < 800))]


# Asian
asnum = 211238
asreadmean = 525
asreadstd = 126
asmathmean = 598
asmathstd = 127
aswritmean = 531
aswritstd = 129

asreadper = np.array([0, 2, 3, 8, 15, 27, 41, 56, 70, 82, 91, 96, 98])
asmathper = np.array([0, 1, 1, 3, 7, 13, 22, 34, 46, 60, 75, 86, 95])
aswritper = np.array([0, 1, 3, 7, 15, 27, 41, 54, 67, 79, 89, 95, 99])

asread = np.round(asnum*asreadper/100.)
asmath = np.round(asnum*asmathper/100.)
aswrit = np.round(asnum*aswritper/100.)

asreaddat = ran.normal(asreadmean, asreadstd, size=asnum)
asreaddat = asreaddat[np.where((asreaddat > 200) & (asreaddat < 800))]
asmathdat = ran.normal(asmathmean, asmathstd, size=asnum)
asmathdat = asmathdat[np.where((asmathdat > 200) & (asmathdat < 800))]
aswritdat = ran.normal(aswritmean, aswritstd, size=asnum)
aswritdat = aswritdat[np.where((aswritdat > 200) & (aswritdat < 800))]


# Mexican
mexnum = 130026
mexreadmean = 448
mexreadstd = 98
mexmathmean = 457
mexmathstd = 98
mexwritmean = 438
mexwritstd = 92

mexreadper = np.array([0, 2, 5, 14, 30, 51, 70, 84, 93, 97, 99, 99, 99])
mexmathper = np.array([0, 1, 4, 12, 26, 47, 66, 82, 91, 96, 99, 99, 99])
mexwritper = np.array([0, 1, 5, 14, 33, 56, 76, 87, 94, 98, 99, 99, 99])

mexread = np.round(mexnum*mexreadper/100.)
mexmath = np.round(mexnum*mexmathper/100.)
mexwrit = np.round(mexnum*mexwritper/100.)

mexreaddat = ran.normal(mexreadmean, mexreadstd, size=mexnum)
mexreaddat = mexreaddat[np.where((mexreaddat > 200) & (mexreaddat < 800))]
mexmathdat = ran.normal(mexmathmean, mexmathstd, size=mexnum)
mexmathdat = mexmathdat[np.where((mexmathdat > 200) & (mexmathdat < 800))]
mexwritdat = ran.normal(mexwritmean, mexwritstd, size=mexnum)
mexwritdat = mexwritdat[np.where((mexwritdat > 200) & (mexwritdat < 800))]

# Puerto Rican
prnum = 30192
prreadmean = 456
prreadstd = 105
prmathmean = 449
prmathstd = 106
prwritmean = 442
prwritstd = 102

prreadper = np.array([0, 2, 6, 14, 28, 48, 66, 80, 90, 96, 99, 99, 99])
prmathper = np.array([0, 2, 6, 16, 31, 50, 68, 81, 91, 96, 99, 99, 99])
prwritper = np.array([0, 2, 6, 16, 33, 53, 71, 84, 92, 97, 99, 99, 99])

prread = np.round(prnum*prreadper/100.)
prmath = np.round(prnum*prmathper/100.)
prwrit = np.round(prnum*prwritper/100.)

prreaddat = ran.normal(prreadmean, prreadstd, size=prnum)
prreaddat = prreaddat[np.where((prreaddat > 200) & (prreaddat < 800))]
prmathdat = ran.normal(prmathmean, prmathstd, size=prnum)
prmathdat = prmathdat[np.where((prmathdat > 200) & (prmathdat < 800))]
prwritdat = ran.normal(prwritmean, prwritstd, size=prnum)
prwritdat = prwritdat[np.where((prwritdat > 200) & (prwritdat < 800))]


# Latin American
lanum = 162655
lareadmean = 449
lareadstd = 107
lamathmean = 457
lamathstd = 107
lawritmean = 439
lawritstd = 102

lareadper = np.array([0, 3, 6, 16, 32, 51, 68, 81, 91, 96, 99, 99, 99])
lamathper = np.array([0, 2, 5, 14, 29, 48, 66, 80, 89, 95, 98, 99, 99])
lawritper = np.array([0, 2, 6, 17, 35, 56, 73, 85, 92, 97, 99, 99, 99])

laread = np.round(lanum*lareadper/100.)
lamath = np.round(lanum*lamathper/100.)
lawrit = np.round(lanum*lawritper/100.)

lareaddat = ran.normal(lareadmean, lareadstd, size=lanum)
lareaddat = lareaddat[np.where((lareaddat > 200) & (lareaddat < 800))]
lamathdat = ran.normal(lamathmean, lamathstd, size=lanum)
lamathdat = lamathdat[np.where((lamathdat > 200) & (lamathdat < 800))]
lawritdat = ran.normal(lawritmean, lawritstd, size=lanum)
lawritdat = lawritdat[np.where((lawritdat > 200) & (lawritdat < 800))]

# White
whnum = 800236
whreadmean = 529
whreadstd = 103
whmathmean = 534
whmathstd = 104
whwritmean = 513
whwritstd = 104

whreadper = np.array([0, 1, 1, 3, 9, 21, 38, 57, 74, 87, 94, 98, 99])
whmathper = np.array([0, 1, 1, 3, 9, 20, 36, 55, 72, 85, 94, 98, 99])
whwritper = np.array([0, 1, 1, 4, 12, 27, 45, 63, 78, 89, 95, 98, 99])

whread = np.round(whnum*whreadper/100.)
whmath = np.round(whnum*whmathper/100.)
whwrit = np.round(whnum*whwritper/100.)

whreaddat = ran.normal(whreadmean, whreadstd, size=whnum)
whreaddat = whreaddat[np.where((whreaddat > 200) & (whreaddat < 800))]
whmathdat = ran.normal(whmathmean, whmathstd, size=whnum)
whmathdat = whmathdat[np.where((whmathdat > 200) & (whmathdat < 800))]
whwritdat = ran.normal(whwritmean, whwritstd, size=whnum)
whwritdat = whwritdat[np.where((whwritdat > 200) & (whwritdat < 800))]

# Other
otnum = 65063
otreadmean = 490
otreadstd = 124
otmathmean = 519
otmathstd = 123
otwritmean = 487
otwritstd = 122 

otreadper = np.array([0, 3, 6, 12, 22, 37, 53, 67, 79, 89, 95, 98, 99])
otmathper = np.array([0, 1, 3, 8, 16, 29, 44, 59, 72, 83, 92, 96, 99])
otwritper = np.array([0, 3, 5, 11, 22, 38, 55, 69, 81, 89, 95, 98, 99])

otread = np.round(otnum*otreadper/100.)
otmath = np.round(otnum*otmathper/100.)
otwrit = np.round(otnum*otwritper/100.)

otreaddat = ran.normal(otreadmean, otreadstd, size=otnum)
otreaddat = otreaddat[np.where((otreaddat > 200) & (otreaddat < 800))]
otmathdat = ran.normal(otmathmean, otmathstd, size=otnum)
otmathdat = otmathdat[np.where((otmathdat > 200) & (otmathdat < 800))]
otwritdat = ran.normal(otwritmean, otwritstd, size=otnum)
otwritdat = otwritdat[np.where((otwritdat > 200) & (otwritdat < 800))]

###############################################################
# Now that the data is loaded, we can make plots
###############################################################

x = np.array(scores.tolist()*20)
y = np.array((mexread/mexnum).tolist()*20)

xx = np.array(scores.tolist()*20)
yy = np.array((whread/whnum).tolist()*20)

def SSx(x):
	#sum of (x-xbar)^2
	n = len(x)
	return np.sum(x**2)-(np.sum(x))**2/n

def SSxy(x,y):
	#sum of (x-xbar)(y-ybar)
	n = len(x)
	return np.sum(x*y) - np.sum(x)*np.sum(y)/n

def fit_linear_reg(x,y):
	#fits linear regression and returns slope and intercept
	#m,b = np.polyfit(x,y,1)
	
	m = SSxy(x,y)/SSx(x)
	b = np.mean(y) - m*np.mean(x)
	r = SSxy(x,y)/np.sqrt(SSx(x)*SSx(y))

	# returns slope and intercept and r
	return m,b,r

def sigma(x):
	#standard deviation x
	n = len(x)
	return np.sqrt(SSx(x)/n)

def Syx(x,y):
	#standard error of estimate = sigma(y)*sqrt(1-r^2)
	m,b,r=fit_linear_reg(x,y)
	return sigma(y)*np.sqrt(1.-r*r)

def plot_conf_intervals(x,y,color,conf=0.95):
	#plots scatter data and confidence intervals

	n = len(y)	#total number of points
	alpha = 1-conf	#alpha = 1-conf
	df = n-2	#degrees of freedom

	std_err = Syx(x,y)
	SSX = SSx(x)
	x_mean = np.mean(x)
	t = stats.t.isf(alpha/2.,n-2)	#students t value for a two tailed test

	x_min,y_min,x_max,y_max=np.amin(x),np.amin(y),np.amax(x),np.amax(y)	#for graphing boundaries maybe
	linx = np.linspace(x_min,x_max,50)					#array of x values for the confidence values
	m,b,r = fit_linear_reg(x,y)						#generates regression line values

	conf_int = t*std_err*np.sqrt(1./n+(linx-x_mean)**2./SSX)		#formula for confidence interval
	pred_int = t*std_err*np.sqrt(1.+1./n+(linx-x_mean)**2./SSX)		#formula for prediction interval
	
	plt.scatter(x,y,c=color, edgecolor='none')			#plot plot plot
	plt.plot(linx,m*linx+b,color ='r')	
	plt.plot(linx,m*linx+b+conf_int,color = 'g')
	plt.plot(linx,m*linx+b-conf_int,color = 'g')
	plt.plot(linx,m*linx+b+pred_int,color = 'y')
	plt.plot(linx,m*linx+b-pred_int,color = 'y')
	plt.xlabel('Scores')
	plt.ylabel('')
	#plt.show()
	#plt.savefig('sleepstudy.pdf')
	#plt.close()
	
plot_conf_intervals(x,y,'blue')	#call plot function
plot_conf_intervals(xx,yy,'purple')	#call plot function
plt.show()
