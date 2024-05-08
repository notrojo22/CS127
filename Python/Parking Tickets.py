#Rojas Shrestha
#rojas.shrestha85@myhunter.cuny.edu
#April 5, 2024
#This program counts which cars got the most parking tickets 

import pandas as pd 

csvFile = input ("Enter csv file name: ")
tickets = pd.read_csv(csvFile)
attribute = input("Enter an attribute to search by: ")
 #tickets is the csv file, attribute is the column header and counts the first 10 values in the column from :10
attribute_count = tickets[attribute].value_counts()[:10]

print ("The 10 worst offenders are: ", attribute_count)


