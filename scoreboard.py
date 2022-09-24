from turtle import Turtle

class Score(Turtle):
    def __init__(self, xcoor):
        super().__init__()
        self.score = 0
        self.create_score(xcoor)

    def create_score(self, xcoor):
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(xcoor, 200)
        self.update_score()

    def update_score(self):
        self.write(self.score, move=False, align='center', font=('Times New Roman', 50, 'normal'))

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_score()