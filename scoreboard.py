from turtle import Turtle
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self, level):
        super().__init__()
        self.penup()
        self.goto(-260, 250)
        self.hideturtle()
        self.pencolor("black")
        self.score = level + 1
        self.write(arg=f"Level {self.score}", align="left", font=FONT)

    def give_point(self):
        self.score += 1
        self.clear()
        self.write(arg=f"Level {self.score}", align="left", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)