from turtle import Turtle
import random

CAR_STARTING_SPEED=5
SPEED_UP=10
COLORS=['red','yellow','blue','green','gray','coral','#d4955f', '#d7503e', '#2f5e8e', '#e7da5c', '#94425b', '#161b28', '#9b493c', '#7aa7c3', '#28161d', 
              '#27130f', '#d14659', '#c08c9f', '#27835b', '#7db38d', '#4ba460', '#e5a9b7', '#0f1f16', '#333766',
              '#e9dc0c', '#9fb136', '#632c3f', '#23a4c4', '#eaaba2', '#692c27', '#a4d1bb', '#97cedc'
              ]

class Car_manager(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.hideturtle()
        self.all_cars=[]
        self.car_speed=CAR_STARTING_SPEED

    def create_car(self):
        random_num=random.randint(1,6)
        if random_num==3:
            new_car=Turtle()
            new_car.shape('square')
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_len=2,stretch_wid=1)
            new_car.penup()
            random_y=random.randint(-250,250)
            new_car.goto(300,random_y)
            self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += SPEED_UP
        
