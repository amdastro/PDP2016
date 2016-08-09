# import the package that lets you plot things.
import pylab as plt
# If you are using an ipython notebook, 
# put this line in there so the plots show in the notebook
%matplotlib inline


# Initialize the figure
plt.figure()
# Replace x and y with the variables you want to plot
plt.plot(x, y)


# Here's an example using some optional keywords, 
# where we set the linestyle to dotted, added markers for the points, 
# changed the color, and increased the linewidth. 
plt.plot(x, y, linestyle='--', marker='o', color='orchid', linewidth=2)
# We can add additional features to the axes like this:
# this sets your x-axis from 0 to 10
plt.xlim([0,10])
plt.ylim([-20,20])
# Label your axes like this
plt.xlabel('whatever x is')
plt.ylabel('y axis')
# Here's one of the many tutorials that shows several plotting options
# http://matplotlib.org/1.4.2/users/pyplot_tutorial.html