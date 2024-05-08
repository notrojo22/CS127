#Rojas Shrestha
#rojas.shrestha85@myhunter.cuny.edu
#March 4, 2024
#This program prompts the user to input 5 number of degrees for the turtle to turn towards and move forward

import turtle
RojasS = turtle.Turtle()

for i in range (5):
    Message = int(input("Enter a number: "))
    RojasS.left(Message)
    RojasS.forward(100)

turtle.exitonclick()
