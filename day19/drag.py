import turtle
from turtle import Turtle,Screen

screen=Screen()

t=Turtle('turtle')
t.speed(-1)
t.pensize(5)

t.penup()
t.goto(-200,-0)
t.pendown()

def dragging(x,y):
    t.ondrag(None)
    t.setheading(t.towards(x,y))
    t.goto(x,y)
    t.ondrag(dragging)

def main():
    turtle.listen()

    t.ondrag(dragging)

    # turtle.onscreenclick(clickRight,3)

    screen.mainloop()

main()
    