# First you need to import the numpy package
# which contains a bunch of useful functions.
# We will nickname it "np"
import numpy as np

# Read in the data by each column.
# Make sure the text in quotes gives the path of the file. 
year,jan,feb,mar,apr,may,jun,jul,aug,sep,oco,nov,dec,JmD,DmN,DJF,MAM,JJA,SON,yr\
=np.genfromtxt('GIST.txt',unpack=True,skip_footer=1)
# The first column is the year, followed by the temperature anomalies for each month,
# and the temperature anomalies measure over the year.
# The units are in milli-degrees Celsius.
# The temperature anomalies indicate how much warmer or colder it is than normal.
# They are calculated by comparing an average of the global temperature to an average of
# the temperature over a base period from 1951-1980. This shows us the long-term temperature changes. 
# For more information, see http://data.giss.nasa.gov/gistemp/FAQ.html#q101
# The annual means are labeled as 'JmD' and 'DmN'
# These refer to the annual means measured over periods from January to December or December to November. 
# The rest are seasonal and meteorological annual means, 
# which you can read about here: http://data.giss.nasa.gov/gistemp/station_data/seas_ann_means.html
# For example, 'DJF' corresponds to the Northern hemisphere winter mean.



