from turtle import Turtle


class Bullet(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=0.3, stretch_len=0.3)
        self.penup()
        self.is_fired = False
        self.hideturtle()

    def fire(self, x, y):
        if not self.is_fired:
            self.goto(x, y)
            self.is_fired = True
            self.showturtle()

    def move(self):
        if self.is_fired:
            self.sety(self.ycor() + 10)
            # Check if bullet is off-screen
            if self.ycor() > 250:
                self.reset_position()

    def reset_position(self):
        self.goto(0, -175)
        self.is_fired = False
        self.hideturtle()
