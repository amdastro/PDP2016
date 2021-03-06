# Want to look at the residuals of your fit?

# Here is a function 
# defines a straight line.
# a is the y-intercept, and b is the slope.
def fit(xx):
    fit = a + b*xx
    return fit

# The residuals are just your data's y-values minus the fit.
# This is the same as taking the difference between
# your data (the real value) and the fit (the expected value).
residuals = y - fit(x)
