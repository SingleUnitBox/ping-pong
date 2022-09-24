from turtle import Screen
from paddle import Paddle
from scoreboard import Score
from ball import Ball
import time

right_paddle = Paddle(370)
left_paddle = Paddle(-370)
ball = Ball()
right_score = Score(50)
left_score = Score(-50)

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
    time.sleep(ball.move_speed)

    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if ball.distance(right_paddle) < 50 and ball.xcor() < 360 or ball.distance(left_paddle) < 50 and ball.xcor() > -360:
        ball.paddle_bounce()

    if ball.xcor() > 390:
        ball.refresh()
        left_score.increase_score()

    if ball.xcor() < -390:
        ball.refresh()
        right_score.increase_score()












screen.exitonclick()
