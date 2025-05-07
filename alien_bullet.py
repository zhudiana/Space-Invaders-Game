from turtle import Turtle

class AlienBullet(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.hideturtle()
        self.is_fired = False

    def fire(self, x, y):
        # Fires the bullet from a given position.
        if not self.is_fired:
            self.goto(x, y)
            self.is_fired = True
            self.showturtle()

    def move(self):
        # Move the bullets downward
        if self.is_fired:
            self.sety(self.ycor() - 10)  # Move the bullet downwards
            # Check if the bullet is off-screen
            if self.ycor() < -250:
                self.reset_position()

    def reset_position(self):
        # Reset the bullet position and hide it.
        self.goto(0, 0)
        self.is_fired = False
        self.hideturtle()

    def is_off_screen(self):
        # Check if the bullet is off-screen.
        return self.ycor() < -250

    def check_collision_with_ship(self, ship):
        # Check if the bullet collides with the ship.
        if abs(self.xcor() - ship.xcor()) < 30 and abs(self.ycor() - ship.ycor()) < 20:
            return True
        return False

