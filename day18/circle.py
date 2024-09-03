import random
from turtle import Turtle,Screen

turtle=Turtle()
screen=Screen()

colours=['red','blue','green','yellow','skyblue','orange','coral','gray']
turtle.speed('fastest')
turtle.pensize(3)
screen.tracer(0)
for i in range(200):
    turtle.color(random.choice(colours))
    turtle.circle(100)
    turtle.right(10)
    turtle.left(120)
    turtle.forward(100)
    turtle.circle(100)
    turtle.forward(100)


screen.exitonclick()
