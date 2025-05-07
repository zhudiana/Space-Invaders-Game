import time
from turtle import Turtle


class Alien(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("assets/alien.gif")
        self.penup()
        self.goto(x, y)
        self.direction = 1  # Direction of movement (1: right, -1: left)

    def move(self):
        # Move horizontally
        new_x = self.xcor() + (4 * self.direction)
        self.goto(new_x, self.ycor())

