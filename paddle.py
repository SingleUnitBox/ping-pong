from turtle import Turtle
STARTING_Y_POSITION = [40, 20, 0, -20, -40]
MOVE_DISTANCE = 40
DIRECTIONS = {
    'UP': 90,
    'DOWN': 270,
    'LEFT': 180,
    'RIGHT': 0
}

class Paddle(Turtle):
    def __init__(self, x_coord):
        super().__init__()
        self.create_paddle(x_coord)


    def create_paddle(self, x_coord):
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.penup()
        self.setheading(DIRECTIONS['UP'])
        self.goto(x_coord, 0)


    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def move_down(self):
        self.backward(MOVE_DISTANCE)

