import turtle
import time

from alien import Alien
from alien_bullet import AlienBullet
from alien_bullet_manager import AlienBulletManager
from bullet import Bullet
from ship import Ship

screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=800, height=500)
screen.tracer(0)

# Load and register ship
screen.register_shape("assets/rocket_ship.gif")
screen.register_shape("assets/alien.gif")
screen.register_shape("assets/explosion.gif")

ship = Ship()
bullet = Bullet()
bullet_manager = AlienBulletManager()

# Bind key press and release events
screen.listen()
screen.onkeypress(ship.start_left, "Left")
screen.onkeyrelease(ship.stop_left, "Left")
screen.onkeypress(ship.start_right, "Right")
screen.onkeyrelease(ship.stop_right, "Right")


def fire_bullet():
    bullet.fire(ship.xcor(), ship.ycor() + 25)


screen.onkeypress(fire_bullet, "space")

aliens = []

# Create aliens in rows and columns
for row in range(3):  # 3 rows
    for col in range(9):  # 5 aliens in each row
        alien = Alien(col * 60 - 150, row * 50 + 100)  # Position aliens in a grid
        aliens.append(alien)


def alien_fire():
    bullet_manager.fire_from_random_alien(aliens)
    screen.ontimer(alien_fire, 10000)


alien_fire()


def move_aliens():
    for alien in aliens:
        alien.move()


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    ship.move_ship()
    bullet.move()
    move_aliens()
    bullet_manager.move_bullets()
    if any(alien.xcor() > 380 or alien.xcor() < -380 for alien in aliens):
        for alien in aliens:
            alien.direction *= -1
            alien.goto(alien.xcor(), alien.ycor() - 20)

    for alien in aliens:
        if (
                abs(bullet.xcor() - alien.xcor()) < 40 and
                abs(bullet.ycor() - alien.ycor()) < 30
        ):
            alien.shape("assets/explosion.gif")
            alien.showturtle()
            screen.ontimer(alien.hideturtle, 100)
            aliens.remove(alien)  # Remove from list to avoid rechecking
            bullet.reset_position()
            break
    for b in bullet_manager.active_bullets:
        if b.check_collision_with_ship(ship):
            game_over_writer = turtle.Turtle()
            game_over_writer.hideturtle()
            game_over_writer.color("red")
            game_over_writer.penup()
            game_over_writer.goto(0, 0)
            game_over_writer.write("GAME OVER", align="center", font=("Arial", 32, "bold"))
            time.sleep(2)
            game_is_on = False

    screen.update()
screen.exitonclick()
