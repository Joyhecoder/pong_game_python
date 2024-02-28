from turtle import Screen
import time
from paddle import Paddle
from ball import Ball

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

RIGHT_POSITION = (350,0)
LEFT_POSITION = (-350,0)
r_paddle = Paddle(position=RIGHT_POSITION)
l_paddle = Paddle(position=LEFT_POSITION)
ball = Ball()

    
screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")
  
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    
    #Detect collision with wall
    if ball.ycor() > 285 or ball.ycor() < -285:
        #bounce 
        ball.bounce()
    
    #Detect collision with r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()
    
    #Detect collision with l_paddle
    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        
    #Detect a ball goes out of bounds
    if ball.xcor() > 390 or ball.xcor() < -390:
        ball.restart()

screen.exitonclick()