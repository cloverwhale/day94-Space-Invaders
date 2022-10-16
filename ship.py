from turtle import Turtle
from bullet import Bullet

MOVE_DIST = 15
BULLET_COLOR = "SkyBlue"


class Ship(Turtle):

    def __init__(self, **kargs):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=2, stretch_wid=0.7)
        self.color(kargs['color'])
        self.goto(kargs['position'])
        self.initial_position = (self.xcor(), self.ycor())
        self.bullet_color = BULLET_COLOR
        self.bullets = []

    def move_left(self):
        if self.xcor() > -320:
            self.backward(MOVE_DIST)

    def move_right(self):
        if self.xcor() < 310:
            self.forward(MOVE_DIST)

    def reset_position(self):
        self.goto(self.initial_position[0], self.initial_position[1])

    def hide(self):
        self.hideturtle()

    def shoots(self, heading):
        bullet = Bullet(color=self.bullet_color, position=(
            self.xcor(), self.ycor()), heading=heading)
        self.bullets.append(bullet)

    def move_bullets(self):
        for bullet in self.bullets:
            if bullet.ycor() > 250 or bullet.ycor() < -250:
                self.delete_bullet(bullet)
            bullet.move()

    def delete_bullet(self, bullet):
        bullet.hide()
        self.bullets.remove(bullet)

    def delete_all_bullets(self):
        for bullet in self.bullets:
            bullet.hide()
        self.bullets.clear()