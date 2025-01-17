from turtle import Turtle
import random

starting_positions = [(0, 0), (-20, 0), (-40, 0)]
MOVE_FORWARD=20
UP=90
DOWN=270
LEFT=180
RIGHT=0 

colors=['red','white','yellow','blue','green']
class Snake():
    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in starting_positions:
            self.add_segments(position)

    def add_segments(self,position):
        new_segment=Turtle('circle')
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
     
    def extend(self):
        self.add_segments(self.segments[-1].position())


    def move(self):
        for seg_num in range(len(self.segments)-1,0,-1):
            new_x=self.segments[seg_num-1].xcor()
            new_y=self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.head.forward(MOVE_FORWARD)
        
    def up(self):
        if self.head.heading() !=DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() !=UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() !=RIGHT:
            self.head.setheading(LEFT)
        
    def right(self):
        if self.head.heading() !=LEFT:
            self.head.setheading(RIGHT)
            


