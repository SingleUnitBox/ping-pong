from turtle import Screen
from paddle import Paddle
import time

right_paddle = Paddle(370)
left_paddle = Paddle(-370)

screen = Screen()
screen.bgcolor("black")
screen.setup(width= 800, height= 600)
screen.tracer(0)
screen.listen()

screen.onkeypress(key="Up", fun=right_paddle.move_up)
screen.onkeypress(key="Down", fun=right_paddle.move_down)



game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)











screen.exitonclick()
