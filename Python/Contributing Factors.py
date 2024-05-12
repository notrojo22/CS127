#Rojas Shrestha
#rojas.shrestha85@myhunter.cuny.edu
#April 8, 2024
#This program prints out the top 3 contributing factors of vehicle collisions

import pandas as pd

file = input("Enter the name of a CSV file: ")
input_file = pd.read_csv(file)


contributing_factor = input_file["CONTRIBUTING FACTOR VEHICLE 1"].value_counts()[:3]
    

print ("Top three contributing factors for collisions: " , contributing_factor)