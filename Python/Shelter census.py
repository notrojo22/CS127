#Rojas Shrestha
#rojas.shrestha85@myhunter.cuny.edu
#March 27, 2024 
#This program plots a graph where it displays the amount of homeless children over time

import pandas as pd
import matplotlib.pyplot as plt 


inputfile = input('Enter the name of a file: ')
outputfile = input('Enter the name of your output file: ')

pop = pd.read_csv(inputfile)

pop['Fraction Children'] = pop['Total Children In Shelter'] / pop['Total Individuals In Shelter']
pop.plot(x = 'Date Of Census', y = 'Fraction Children')
 
fig = plt.gcf()
fig.savefig(outputfile)
