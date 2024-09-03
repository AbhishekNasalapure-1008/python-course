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
        # y=self.ycor()

    def go_right(self):
        new_x=self.xcor()+10
        self.goto(new_x,self.ycor())
        
    def go_left(self):
        new_x=self.xcor()-10
        self.goto(new_x,self.ycor())
        # self.forward(10)

    def go_to_start(self):
        self.goto(0,-280)  