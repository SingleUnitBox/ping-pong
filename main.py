from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

right_paddle = Paddle(370)
left_paddle = Paddle(-370)
ball = Ball()

screen = Screen()
screen.bgcolor("black")
screen.setup(width= 800, height= 600)
screen.tracer(0)
screen.listen()

screen.onkeypress(key="Up", fun=right_paddle.move_up)
screen.onkeypress(key="Down", fun=right_paddle.move_down)

screen.onkeypress(key="w", fun=left_paddle.move_up)
screen.onkeypress(key="s", fun=left_paddle.move_down)



game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()











screen.exitonclick()
