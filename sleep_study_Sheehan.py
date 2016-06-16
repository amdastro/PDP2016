import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt('sleepstudy.dat')

#Define x and y values of data as numpy arrays
x=data[:,2]
y=data[:,1]



def fit_linear_reg(x,y):

	#fits linear regression and returns slope and intercept
	
	m,b = np.polyfit(x,y,1)
	
	
	return m,b




def y_err_calc(x,y):

	#works only for discrete x values with y scatter. Otherwise requires binning (not here yet)
	

	mean_list =[]
	std_list=[]
	std_err_list=[]
	
	xs=np.unique(x)					#finds unique x values
	for i in xs:					#loops through these x values
		
		args=np.where(x==i)[0]			#finds the arguments of these x values in full x data
		ys=y[args]				#finds all corresponding y vlaues
		mean=np.mean(ys)			#mean, standard deviation and std error of these y values
		std=np.std(ys)				
		std_err=std/np.sqrt(len(ys))
	
	
		mean_list=np.append(mean_list,mean)	#all values calculated above appended to an array
		std_list=np.append(std_list,std)
		std_err_list=np.append(std_err_list,std_err)
	
	
	print xs
	print mean_list
	print std_err_list

	#outputs unique x values, corresponding y means and y std errors
	return xs, mean_list, std_err_list


m,b=fit_linear_reg(x,y)

xs, mean_list, std_err_list = y_err_calc(x,y)

# simple scatter plot for data with linear regression fit
plt.scatter(x,y)
plt.plot(x,m*x+b,'-')
plt.xlim(0,10)
plt.ylim(200,400)
plt.xlabel('Days without sleep')
plt.ylabel('Reaction time (ms)')
plt.savefig('sleep.png')
plt.close()


#means of y vs x along with regression
plt.scatter(xs,mean_list)
plt.plot(xs,m*xs+b,'-')
plt.xlim(0,10)
plt.ylim(200,400)
plt.xlabel('Days without sleep')
plt.ylabel('Reaction time (ms)')
plt.savefig('sleep_mean.png')
plt.close()

#1xstandard error bar
plt.errorbar(xs,mean_list,yerr=std_err_list,fmt='o')
plt.plot(xs,m*xs+b,'-')
plt.xlim(0,10)
plt.ylim(200,400)
plt.xlabel('Days without sleep')
plt.ylabel('Reaction time (ms)')
plt.savefig('sleep_err.png')
plt.close()

#2xstandard error bar
plt.errorbar(xs,mean_list,yerr=2*std_err_list,fmt='o')
plt.plot(xs,m*xs+b,'-')
plt.xlim(0,10)
plt.ylim(200,400)
plt.xlabel('Days without sleep')
plt.ylabel('Reaction time (ms)')
plt.title('95% confidence limits')
plt.savefig('sleep_2err.png')
plt.close()
