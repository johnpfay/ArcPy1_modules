#PMOTW_examples.py
#
# These examples relate to Doug Hellman's Python Module of the Week
# website: https://pymotw.com/3/index.html

############ Math module: https://pymotw.com/3/math ############
#%% import the module
import math

#%% print the value of pi
print(math.pi)

#%% Use the "format" function to print math to exactly 10 decimal places
print(f"{math.pi:0.10f}")

########## Statistics module: https://pymotw.com/3/statistics ##########
#%% import the module
import statistics

#%% print the mean of the following list: [10,12,14,21,29,8,11,1,30]
print(statistics.median([10,12,14,21,29,8,11,1,30]))

############ Datetime module: https://pymotw.com/3/datetime ############

#%% import the module
import datetime

#%% set theTime as today
theTime = datetime.date.today()

#%% show the time
print(theTime)

#%% show the type of the theTime variable
print(type(theTime))

#%% show what functions come with this object
print(dir(theTime))

#%% print the current year
print(theTime.year)

