#osModuleDemo.py
#
# Description: Demonstrates some uses of the os module and the os.path submodule
#
# John.Fay@duke.edu (for ENV859)

#%% import the os module
import os   

#%% list the contents of your V: drive
print (os.listdir("V:\\"))

#%% print the current working directory (place from where PythonWin was started)
print (os.getcwd())

#%% create a new folder in your V: drive
os.mkdir("V:\\osplayground")

#%% ensure that the folder was created (check for its existence)
print (os.path.exists("V:\\osplayground"))

#%% change the working directory to your newly created folder
os.chdir("V:\\osplayground")

#%% Create a new file in the current working directory, write some text, and close it
fileObj = open("myFile.txt",'w')
fileObj.write("Hello there!")
fileObj.close()

#%% Open the file (Close notepad manually when done!)
os.system("notepad myFile.txt")

#%% Rename the file
os.rename("myFile.txt", "theFile.txt")

#%% Use the os.path sub-module to parse the file's path into components
pathString = "V:\\osplayground\\theFile.txt"    #Make a variable of the path to avoid retyping it
print (os.path.basename(pathString))            #Gets the file name (without the path)
print (os.path.dirname(pathString))             #Gets the path in which the file exists

theDirname,theFilename = os.path.split(pathString)       # Creates a tuple of the path and file name
print (theDirname)     # The path
print (theFilename)    # The file name

#%% Use the os.path.join function to join a file with its path
pathString2 = os.path.join(theDirname,"MyOtherFile.txt")
print(pathString2)

#%% Remove the [renamed] file you created
os.remove("V:\\osplayground\\theFile.txt")

#%% Navigate back to the V: drive
os.chdir("V:\\")

#%% Remove the folder you created (if not in use)
os.rmdir("V:\\osplayground\\")

