import random
from alien_bullet import AlienBullet  # Your class that handles a single bullet



class AlienBulletManager():
    def __init__(self):
        self.active_bullets = []

    def fire_from_random_alien(self, aliens):
        if aliens:
            shooter = random.choice(aliens)
            bullet = AlienBullet()
            bullet.fire(shooter.xcor(), shooter.ycor() - 20)
            self.active_bullets.append(bullet)

    def move_bullets(self):
        for bullet in self.active_bullets[:]:
            bullet.move()
            if bullet.is_off_screen():
                bullet.hideturtle()
                self.active_bullets.remove(bullet)
