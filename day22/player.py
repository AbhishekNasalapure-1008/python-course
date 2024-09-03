from turtle import Turtle


class Player(Turtle):
    def __init__(self) -> None:
        super().__init__()  
        self.shape('turtle')
        self.penup()
        self.speed('fastest')
        self.setheading(90)
        self.goto(0,-280)
        
    def go_up(self):
        self.forward(10)

    def go_to_start(self):
        self.goto(0,-280)   
