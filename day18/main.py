
from turtle import Turtle,Screen
import random

turtle=Turtle()
screen=Screen()

turtle.speed('fastest')
turtle.setheading(225)
turtle.penup()
turtle.forward(300)

color_list = ['#d4955f', '#d7503e', '#2f5e8e', '#e7da5c', '#94425b', '#161b28', '#9b493c', '#7aa7c3', '#28161d', 
              '#27130f', '#d14659', '#c08c9f', '#27835b', '#7db38d', '#4ba460', '#e5a9b7', '#0f1f16', '#333766',
              '#e9dc0c', '#9fb136', '#632c3f', '#23a4c4', '#eaaba2', '#692c27', '#a4d1bb', '#97cedc']

def something():
    turtle.setheading(0)

    for i in range(10):
        turtle.dot(20,random.choice(color_list))  
        turtle.penup()
        turtle.forward(50)

    turtle.setheading(90)
    turtle.forward(50)
    turtle.setheading(180)
    turtle.forward(500)


for i in range(10):
    something()



screen.exitonclick()