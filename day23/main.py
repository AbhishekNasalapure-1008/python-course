from turtle import Screen
from car_maneger import CarManeger
from player import Player
from scoreboard import Scoreboard
import time

screen=Screen()
car_maneger=CarManeger()
player=Player()
scoreboard=Scoreboard()

screen.setup(width=600,height=600)
screen.title("python Turtle Crossing")
screen.tracer(0)

screen.listen()
screen.onkey(player.go_up,"Up")
screen.onkey(player.go_right,"Right")
screen.onkey(player.go_left,"Left")

game_is_on=True
while game_is_on:
    time.sleep(.1)

    car_maneger.create_car()
    car_maneger.move_car()
    screen.update()
    scoreboard.update_scoreboard()

    for car in car_maneger.all_cars:
        if car.distance(player)<=18:
            game_is_on=False
            scoreboard.game_over()

    if player.ycor()>280:
        player.go_to_start()
        car_maneger.level_up()
        scoreboard.increase_level()


screen.exitonclick()