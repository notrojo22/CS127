#Rojas Shrestha
#rojas.shrestha8@myhunter.cuny.edu
#March 4, 2024
#This program prints a pentagon in the color of "Cornflower Blue" using the turtle module

import turtle
turtle.colormode(255)
RojasS = turtle.Turtle()
RojasS.shape("turtle")
RojasS.color(100,149,237)

for i in range (5):
    RojasS.forward(100)
    RojasS.left(72)
    RojasS.stamp()

turtle.exitonclick()
