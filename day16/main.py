from turtle import Turtle,Screen
import random

timmy=Turtle()
timmy.shape("turtle")
timmy.color("red")

colors=["red","green","blue","yellow","coral", "purple"]
for i in range(100):
    timmy.pensize(30)
    timmy.forward(200)
    timmy.color(random.choice(colors))
    timmy.left(140)
    timmy.forward(200)








print(timmy)

my_screen=Screen()
#class attributes
print(my_screen.canvheight)
print(my_screen.canvwidth)
my_screen.exitonclick()