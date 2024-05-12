#Rojas Shrestha
#rojas.shrestha85@myhunter.cuny.edu
#March 25, 2024
#This program asks the user for the name of a borough in NYC and outputs a graph of the population throughout a petiod of time

import matplotlib.pyplot as plt
import pandas as pd

borough = input("Enter a name of a borough: ")
filename = input("Enter a name for your file: ")

pop = pd.read_csv("nycHistPop.csv", skiprows = 5)


pop["Fraction"] = pop[borough]/pop["Total"]
pop.plot (x = "Year", y = "Fraction")


fig = plt.gcf()
fig.savefig(filename)