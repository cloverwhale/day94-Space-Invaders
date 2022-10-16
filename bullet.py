from turtle import Turtle


class Bullet(Turtle):

    def __init__(self, **kargs):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color(kargs['color'])
        self.shapesize(stretch_len=0.2, stretch_wid=0.2)
        self.goto(kargs['position'])
        self.initial_position = (self.xcor(), self.ycor())
        self.left(kargs['heading'])

    def move(self):
        self.forward(2)

    def hide(self):
        self.hideturtle()