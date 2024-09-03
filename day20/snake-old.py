import random
import turtle
from turtle import Turtle,Screen
import time
# colors=['red','white','yellow','blue','green']

screen=Screen()
screen.setup(width=500,height=400)
screen.title('Windows snake game')
screen.bgcolor('black')
# t1=Turtle('square')
# t1.color(random.choice(colors))


# t2=Turtle('square')
# t2.color(random.choice(colors))
# t2.penup()
# t2.goto(-20,0)
# t2.penup()

# t3=Turtle('square')
# t3.color(random.choice(colors))
# t3.penup()
# t3.goto(-40,0)
positions = [(0, 0), (-20, 0), (-40, 0)] 
turtles = []
colors = ["red", "green", "blue"]

screen.tracer(0)

for i in range(3):
    t = turtle.Turtle()
    t.shape("square")
    t.color(colors[i])
    t.speed(0)
    t.penup()
    turtles.append(t)
    t.goto(positions[i])
screen.update()
game_is_on=True

while game_is_on:
    screen.update()
    for segment in turtles:
        segment.forward(20)
        time.sleep(.1)
        

screen.exitonclick()

# for i in range(1,50,10):
#     print(i)
