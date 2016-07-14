import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

data = np.genfromtxt('sleepstudy.dat')

#Define x and y values of data as numpy arrays
x=data[:,2]
y=data[:,1]


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
	return sigma(y)*np.sqrt(1-r*r)

def plot_conf_intervals(x,y,conf=0.95):

	n = len(y)
	
	alpha = 1-conf

	df = n-2

	std_err = Syx(x,y)
	SSX = SSx(x)
	
	x_mean = np.mean(x)

	t = stats.t.isf(alpha/2,n-2)


	x_min,y_min,x_max,y_max=np.amin(x),np.amin(y),np.amax(x),np.amax(y)

	linx = np.linspace(x_min,x_max,50)
	
	m,b,r = fit_linear_reg(x,y)

	conf_int = t*std_err*np.sqrt(1/n+(linx-x_mean)**2/SSX)
	print conf_int
	

	plt.scatter(x,y)
	plt.plot(linx,m*linx+b,color ='r')	
	plt.plot(linx,m*linx+b+conf_int,color = 'g')
	plt.plot(linx,m*linx+b-conf_int,color = 'g')
	plt.xlabel('Days without sleep')
	plt.ylabel('Reaction time (ms)')

	plt.savefig('sleep_all.pdf')
	plt.close()
	
plot_conf_intervals(x,y)
		
	





