from random import randint
from bullet import Bullet
from ship import Ship

ROWS = 4
COLUMNS = 8
INIT_X = -250
INIT_Y = 220
RIGHT_BOUNDARY = 280
LEFT_BOUNDARY = RIGHT_BOUNDARY * -1 - 5
# Use gradient colors (color names end with 1234), see https://cs111.wellesley.edu/labs/lab02/colors
INVADER_COLOR = "DarkOliveGreen"
BOMB_COLOR = "coral"


class Invaders:

    def __init__(self):
        self.head_left = True
        self.ships = []
        self.bombs = []
        self.bomb_color = BOMB_COLOR
        y = INIT_Y
        for i in range(ROWS):
            x = INIT_X
            for _ in range(COLUMNS):
                ship = Ship(color=INVADER_COLOR+str(i+1), position=(x, y))
                x = x + 70
                self.ships.append(ship)
            y = y - 28

    def delete_ship(self, ship_index):
        self.ships[ship_index].hide()
        self.ships.remove(self.ships[ship_index])

    def reset_layout(self):
        for ship in self.ships:
            ship.hide()
        for bomb in self.bombs:
            bomb.hide()
        self.ships.clear()
        self.bombs.clear()
        self.__init__()

    def get_boundary_x_cor(self):
        x_cors = [ship.xcor() for ship in self.ships]
        x_cors.sort()
        # left, right
        return x_cors[0], x_cors[-1]

    def moving_left(self):
        for i in range(len(self.ships)):
            x = self.ships[i].xcor()
            y = self.ships[i].ycor()
            self.ships[i].goto(x - 0.5, y)

    def moving_right(self):
        for i in range(len(self.ships)):
            x = self.ships[i].xcor()
            y = self.ships[i].ycor()
            self.ships[i].goto(x + 0.5, y)

    def move(self):
        self.moving_left() if self.head_left else self.moving_right()
        # change direction
        if self.get_boundary_x_cor()[0] < LEFT_BOUNDARY:
            self.head_left = False
        if self.get_boundary_x_cor()[1] > RIGHT_BOUNDARY:
            self.head_left = True

    def drop_bomb(self):
        ship_index = randint(0, len(self.ships)-1)
        ship = self.ships[ship_index]
        bomb = Bullet(color=self.bomb_color, position=(
            ship.xcor(), ship.ycor()), heading=-90)
        self.bombs.append(bomb)

    def move_bomb(self):
        for bomb in self.bombs:
            if bomb.ycor() < -250:
                bomb.hide()
                self.bombs.remove(bomb)
            bomb.move()

    def delete_bomb(self, bomb):
        bomb.hide()
        self.bombs.remove(bomb)
