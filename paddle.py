from turtle import Turtle
STARTING_Y_POSITION = [40, 20, 0, -20, -40]
MOVE_DISTANCE = 40
DIRECTIONS = {
    'UP': 90,
    'DOWN': 270,
    'LEFT': 180,
    'RIGHT': 0
}

class Paddle:
    def __init__(self, x_coord):
        self.paddle = []
        self.create_paddle(x_coord)


    def create_paddle(self, x_coord):
        for position in STARTING_Y_POSITION:
            paddle = Turtle("square")
            paddle.color("white")
            paddle.penup()
            paddle.seth(DIRECTIONS['UP'])
            paddle.goto(x_coord, position)
            self.paddle.append(paddle)

    def move_up(self):
        for segment in self.paddle:
            segment.forward(MOVE_DISTANCE)

    def move_down(self):
        for segment in self.paddle:
            segment.backward(MOVE_DISTANCE)

