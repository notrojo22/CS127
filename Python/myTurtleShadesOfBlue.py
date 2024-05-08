import turtle
turtle.colormode(255)
turtle.shape("turtle")
RojasS = turtle.Turtle()
RojasS.backward(10)


for i in range (0,255,10):
    RojasS.forward(10)
    RojasS.pensize(i)
    RojasS.color(0,0,i)