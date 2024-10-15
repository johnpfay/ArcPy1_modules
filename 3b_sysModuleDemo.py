# Note: This script demonstrates how to use the sys module to 
# get user input from the command line. It should not be run
# from the interactive window, but rather from the command line 
# or in debug mode.

# Import the sys module
import sys

# Import the date time "submodule" of the date time module
from datetime import datetime 

# Point "name" to the first input the user gives
name = sys.argv[1]

# Point "startDate" to the second input the user gives
startDate = int(sys.argv[2])

# Point "currentYear" to today's year
currentYear = datetime.now().year

# Compute the difference between the current year and the start year 
employmentYears = currentYear - startDate

# Check that the user provided a year in the past
if startDate > currentYear:
	print ("Need to enter a year before {}. Exiting".format(currentYear))
    #Exit the program
	sys.exit(1)

# Print the output message
print ("Hello {}".format(name))
print (f"Seems you've been working for {employmentYears} years")