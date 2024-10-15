#ArcPy_Intro.py - An introduction to using the ArcPy module

#%% Import the module
import arcpy

#%% List the functions
funcList = dir(arcpy)
print(len(funcList))

#%% Print the help
help(arcpy)

#%% Print help on the spatial analyst "buffer" tool
help(arcpy.Buffer_analysis)

#%% Add parentheses after the command to display contextual help
arcpy.Buffer_analysis

