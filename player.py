from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 270


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(0, -280)
        self.setheading(90)
        self.color("black")

    def move_player(self):
        self.forward(MOVE_DISTANCE)

    def reset_player(self):
        self.goto(0, -280)
