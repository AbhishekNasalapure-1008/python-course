from ball import Ball
from turtle import Turtle,Screen
from paddle import Paddle
import time
from scoreboard import Scoreboard

screen=Screen()
scoreboard=Scoreboard()
screen.bgcolor('black')
screen.setup(width=800,height=600)
screen.title('pong')
screen.tracer(0)


l_paddle=Paddle((350,0))
screen.listen()
screen.onkeypress(l_paddle.go_up,"Up")
screen.onkeypress(l_paddle.go_down,"Down")

r_paddle=Paddle((-350,0))
screen.onkeypress(r_paddle.go_down,"s")
screen.onkeypress(r_paddle.go_up,"w")

ball = Ball()
ball.move()

game_is_on=True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor()>290 or ball.ycor()<-290:
        ball.bounce_y()
    
    if (ball.distance(l_paddle)<50 and ball.xcor()>320) or (ball.distance(r_paddle)<50 and ball.xcor()>-340):
        ball.bounce_x()
        

    if ball.xcor()>380:
        ball.reset_position()
        scoreboard.clear()
        scoreboard.l_point()
        
    
    if ball.xcor()<-380:
        ball.reset_position()
        scoreboard.clear()
        scoreboard.r_point()
screen.exitonclick()