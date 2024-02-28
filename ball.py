from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape('circle')
        self.color('red')
        self.penup()
    
    def move(self):
        x_cord = random.randint(-390, 390)
        y_cord = random.randint(-290, 290)
        new_x = self.xcor() + 10
        new_y = self.ycor() + 10
        self.goto(new_x, new_y)
        