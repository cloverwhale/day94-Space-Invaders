from turtle import Turtle

INIT_POSITION = (-342, -255)
FONT = ("Courier New", 16, "normal")
ALIGN = "left"
TEXT_COLOR = "white"
POINT = 50
LIVES = 3


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color(TEXT_COLOR)
        self.goto(INIT_POSITION)
        self.point = 0
        self.lives = LIVES
        self.print_score()

    def print_score(self):
        self.clear()
        self.write(arg=f"Score: {self.point} / Lives: {self.lives}", align=ALIGN, font=FONT)

    def print_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(arg=f"Game Over / Final score: {self.point} / Press r to restart", align="center", font=FONT)

    def print_completed(self):
        self.clear()
        self.goto(0, 0)
        self.write(arg=f"Game Cleared / Final score: {self.point} / Press r to restart", align="center", font=FONT)

    def add_points(self):
        self.point += POINT
        self.print_score()

    def decrease_lives(self):
        self.lives -= 1
        self.print_score()

    def reset_score(self):
        self.clear()
        self.lives = 3
        self.point = 0
        self.goto(INIT_POSITION)
        self.print_score()
