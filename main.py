import turtle
import time

from bullet import Bullet
from ship import Ship

screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=800, height=500)
screen.tracer(0)

# Load and register ship
screen.register_shape("rocket_ship.gif")

ship = Ship()
bullet = Bullet()

# Bind key press and release events
screen.listen()
screen.onkeypress(ship.start_left, "Left")
screen.onkeyrelease(ship.stop_left, "Left")
screen.onkeypress(ship.start_right, "Right")
screen.onkeyrelease(ship.stop_right, "Right")


def fire_bullet():
    bullet.fire(ship.xcor(), ship.ycor() + 25)


screen.onkeypress(fire_bullet, "space")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    ship.move_ship()
    bullet.move()
    screen.update()

screen.exitonclick()
