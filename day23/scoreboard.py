from turtle import Turtle

POSITION=(-280,280)

class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.level=1
        self.hideturtle()
        self.penup()
        self.goto(-280,250)
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()
        self.write(f"Level:{self.level} ",align='left',font=('courier',24))
    
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align='center',font=("Arial",24))

    
    def increase_level(self):
        self.level+=1
        self.update_scoreboard()
