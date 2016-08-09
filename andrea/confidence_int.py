# What is the confidence interval of your fit to the data?



# If we have the residuals, we can get the residual standard deviation 'sd_res'
# This is a measure of the deviation of the data from the fitted line.
var_res = np.sum(residuals**2)/(n-2)
sd_res = np.sqrt(var_res)


# We can calculate the standard error of the slope of our fitted line:
se_b = sd_res/np.sqrt(Sxx)

# And here is the standard error of the y-intercept:
se_a = sd_res*np.sqrt(np.sum(x**2)/(n*Sxx))


# This defines a function (a fancy 'lambda function' again)
# that returns the standard error of the fitted line.
# It basically takes the sum of squares of the erorr of the slope
# and the error of the y-intercept. 
se_fit     = lambda x: sd_res * np.sqrt(  1./n + (x-np.mean(x))**2/Sxx)


# This imports a pacakge that gives us cool stats things
import scipy.stats as stats

# Here we define a few terms, like the degrees of freedom 'df'
df = n-2  
# For calculating confidence intervals, the alpha value 
# corresponds to the level of confidence you want to consider.
# For a 95% confidence interval, we set alpha = 0.05 
# so the limit is 95%
# This can be changed to whatever level you want. 
alpha=0.05
limit = (1-alpha)*100
# The t-value is something that goes into the confidence interval formula.
# It's just a number that we need to pull from a table, but 
# the python stats package can do that for us if we 
# give is alpha and the degrees of freedom. 
tval = stats.t.isf(alpha/2., df) 


# Now we have a confidence interval!
# If we want to plot it, we can call the function like this.
# First we can plot the a line that is fit to the data,
# where a is the y-intercept and b is the slope.
plt.plot(x, a+b*x, label='Fitted line')
# Then we can plot the line PLUS the confidence interval. 
# The confidence interval is given by <the line> + <t_value> * <standard error of the fit, which depends on x>
plt.plot(x, a+b*x + tval*se_fit(x), 'r', label=r'Confidence limit ({0:.1f}\%)'.format(limit))
# The label keyword just labels the confidence line. You can see the label by then adding
plt.legend()






