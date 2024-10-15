#ForestStockDemo.py
# Forest stock calculations - example of Python as a simple calculator
#
# Usage: Set the tree type and age and run the script to 
#
# John.Fay@duke.edu (for ENV 859)

# User Input variables
treeType = "loblolly"   # Type of tree
treeAge = 8             # Age of tree

# Script variables
stockRateDict = {} # Stocking rate at 0,5,10,15,20 years in m tons C/acre
stockRateDict["loblolly"] = (14.4,20.9,27.2,32.1,37.1)
stockRateDict["oak"] = (13.4,18.7,24.1,28.6,33.2)
stockRateDict["cottonwood"] = (16.8,21.7,26.5,31.1,35.8)
stockRateDict["cypress"] = (16.7,20.0,26.2,31.8,37.2)

# Get the age class from the supplied treeAge
if treeAge <= 5:
    ageClass = 0
elif treeAge <= 10:
    ageClass = 1
elif treeAge <= 15:
    ageClass = 2
elif treeAge <= 20:
    ageClass = 3
else:
    print ("Your tree can't be older than 20 years!")

# extract the initial and end stock rates (current and future age classes)
initStock = stockRateDict[treeType][ageClass]
endStock = stockRateDict[treeType][ageClass + 1]

# calculate the flux rate as the different between and initial rates
rate = endStock - initStock

# tell the user about the tree
print(f"Your {treeAge} year old {treeType} tree is storing {rate:0.2f}m tons of carbon/year")
