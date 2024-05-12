#Davlatbek Toshpulatov

import matplotlib.pyplot as plt
import numpy as np

picture = input("Enter an image for pixel analysis: ")

ca = plt.imread(picture) 
CountSnow = 0
t = 0.75

for i in range (ca.shape[0]):
    for j in range (ca.shape[1]):
        if (ca[i,j,0]> t) and (ca[i,j,1]> t) and (ca[i,j,2]> t):
            CountSnow = CountSnow + 1


print ("Snow count is : ", CountSnow)
