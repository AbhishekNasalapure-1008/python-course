from turtle import Turtle,Screen
import random

screen=Screen()

is_race_on=False

screen.setup(width=500,height=400)
colors=['red','blue','indigo','yellow','orange','green']
y_pos=[-70,-40,-10,20,50,80]

all_turtle=[]

for i in range(6):
    new_turtle=Turtle('turtle')
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto((-230,y_pos[i]))
    all_turtle.append(new_turtle)

user_bet=screen.textinput("chose Color","on which color do you want to bet? enter the color:")

if user_bet:
    is_race_on=True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor()>230:
            is_race_on=False
            winner=turtle.pencolor()
            if user_bet==winner:
                print('You Won!')
            else:
                print(f'You lose the game, Winner is {winner}')
        random_distance=random.randint(1,10)
        turtle.forward(random_distance)
            
screen.exitonclick()