from invaders import Invaders
from ship import Ship
from scoreboard import ScoreBoard
from turtle import Screen
import time

SCREEN_WIDTH = 728
SCREEN_HEIGHT = 550
DEAULT_BOTTOM = SCREEN_HEIGHT/2 * -1 + 50
DEFENDER_COLOR = "LightGoldenrod3"

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.title("Python Turtle Space Invaders Game")
screen.bgcolor("black")
screen.tracer(0)

game_is_on = True

defender = Ship(color=DEFENDER_COLOR, position=(0, DEAULT_BOTTOM))
# Use gradient colors (color names end with 1234), see https://cs111.wellesley.edu/labs/lab02/colors
invaders = Invaders()
scoreboard = ScoreBoard()


def start_game():

    global game_is_on, defender, scoreboard
    start_time = round(time.time())
    counter = 0
    secs = 5.0

    while game_is_on:

        time.sleep(0.01)

        defender.move_bullets()
        if len(invaders.ships) > 0:
            invaders.move()
            invaders.move_bomb()
            if ((round(time.time()) - start_time) % secs == 0 and counter % 30 == 0):
                invaders.drop_bomb()
            counter += 1
        else:
            scoreboard.print_completed()
            game_is_on = False

        # collision detection
        for bullet in defender.bullets:
            for ship in invaders.ships:
                if bullet.distance(ship) < 18:
                    ship_index = invaders.ships.index(ship)
                    invaders.delete_ship(ship_index)
                    defender.delete_bullet(bullet)
                    scoreboard.add_points()
            for bomb in invaders.bombs:
                if bullet.distance(bomb) < 5:
                    invaders.delete_bomb(bomb)
                    defender.delete_bullet(bullet)

        for bomb in invaders.bombs:
            if bomb.distance(defender) < 18:
                scoreboard.decrease_lives()
                invaders.delete_bomb(bomb)
                defender.reset_position()

        if scoreboard.lives == 0:
            scoreboard.print_over()
            game_is_on = False

        screen.update()


def restart():
    global game_is_on, defender, scoreboard, invaders
    if not game_is_on:
        game_is_on = True
        scoreboard.reset_score()
        defender.delete_all_bullets()
        defender.reset_position()
        invaders.reset_layout()
        start_game()


screen.listen()
screen.onkey(defender.move_left, "Left")
screen.onkey(defender.move_right, "Right")
screen.onkey(lambda: defender.shoots(90), "space")
screen.onkey(restart, "r")
screen.onkey(screen.bye, "q")

start_game()


screen.exitonclick()
