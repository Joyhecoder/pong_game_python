from turtle import Turtle


class Paddle:
    def __init__(self, position) -> None:
        self.segments = []
        self.paddle = self.create_paddle(position=position)
    
    def create_paddle(self, position):
        paddle = Turtle("square")
        paddle.color("white")
        paddle.shapesize(stretch_wid=5, stretch_len=1)
        paddle.penup()
        paddle.goto(position)
        return paddle
    
    def up(self):
        new_y = self.paddle.ycor() + 20
        self.paddle.goto(self.paddle.xcor(), new_y)
    
    def down(self):
        new_y = self.paddle.ycor() - 20
        self.paddle.goto(self.paddle.xcor(), new_y)