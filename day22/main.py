from turtle import Screen
from car_manager import Car_manager
from player import Player
from scoreboard import Scoreboard
import time

screen = Screen()
player = Player()
scoreboard=Scoreboard()
car_manager=Car_manager()

screen.setup(width=600,height=600)
screen.title('python turtle crossing')
screen.tracer(0)

screen.listen()
screen.onkey(player.go_up,'Up')


game_is_on=True
while game_is_on:
    time.sleep(.1)

    car_manager.create_car()
    car_manager.move_car()
    screen.update()
    scoreboard.update_scoreboard()

    for car in car_manager.all_cars:
        if car.distance(player)<20:
            game_is_on=False
            scoreboard.game_over()


    if player.ycor() >= 280:
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()


screen.exitonclick()