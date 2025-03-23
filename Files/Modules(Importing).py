import os       #Module provides functions for interacting with the operating system
import sys      #Module allows interaction with Python interpreter and command lind arguments
import datetime #Module provides functions for working with dates and times

#OS some functions
print("Current Directory",os.getcwd())
print("Files and Directories",os.listdir())
#Create new Directory
os.mkdir("Awad")

#Remove Directory
os.rmdir("Awad")

#Sys some functions

print("Command-line arguments: ",sys.argv)

print("Python Version: ",sys.version)



#Date time

now = datetime.datetime.now()
print("Current datatime",now)

today = datetime.date.today()
print("Today is :",today)

custom_data = datetime.date(2025,8,31)
print("Custom Date: ",custom_data)

#Difference between dates
diff = custom_data - today
print("Difference: ",diff.days)






#Exit the Program (Sys)
sys.exit("Exiting the program")