#Rojas Shrestha
#rojas.shrestha85@myhunter.cuny.edu 
#April 1, 2024
#This program takes in an image and outputs only the bottom left corner of the image

import matplotlib.pyplot as plt
import numpy as np  

image_file = input("Enter a file: ")
output_file = input("Enter a name for your file: ")

image = plt.imread(image_file)
height_image = image.shape[0]
width_image = image.shape[1]

cropped_picture = image[height_image//2:, :width_image//2]

plt.imsave(output_file, cropped_picture)