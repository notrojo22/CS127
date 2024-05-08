#Rojas Shrestha
#rojas.shrestha85@myhunter.cuny
#March 25, 2024
#This program prints out the average and the maximum population for a borough in NYC

import pandas as pd

pop = pd.read_csv ("nycHistPop.csv", skiprows = 5)
borough = input("Enter a borough: ")

print ("The average population of" , borough, "is:", pop[borough].mean())
print ("The maximum population of" , borough, "is:", pop[borough].max())
