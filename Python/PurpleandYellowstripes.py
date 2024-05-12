#Rojas Shrestha
#rojas.shrestha85@myhunter.cuny.edu
#March 13, 2024
#This program prompts the user to input an image size and creates a picture of purple and yellow stripes.

import matplotlib.pyplot as plt
import numpy as np

size = int(input("Enter how large you want your picture to be: "))
name = str(input("What would you like to name your file? "))

img = np.ones((size,size,3))
img[0::2,:,2] = 2
img[0::2,:,1] = 2
img[1::2,:,] = 1

plt.imsave(name, img)