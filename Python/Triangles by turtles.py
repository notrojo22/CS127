#Rojas Shrestha
#rojas.shrestha85@myhunter.cuny.edu
#April 12, 2024
#This program uses turtle to draw triangles

import turtle
 

def triangle(t, length):
    if length > 10:
        for i in range (3):
            t.forward(length)
            t.left(120)
        triangle(t, length/2)
 
def nestedTriangle(t, length):
    if length > 10:
        for i in range (3):
            t.forward(length)
            t.left(120)
            triangle(t, length/2)
   
