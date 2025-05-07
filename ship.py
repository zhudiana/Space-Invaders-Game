from turtle import Turtle, Screen

class Ship(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("assets/rocket_ship.gif")
        self.penup()
        self.goto(0, -200)
        self.move_left = False
        self.move_right = False


    def start_left(self):
        global move_left
        self.move_left = True
        self.move_ship()

    def stop_left(self):
        global move_left
        self.move_left = False

    def start_right(self):
        global move_right
        self.move_right = True
        self.move_ship()

    def stop_right(self):
        global move_right
        self.move_right = False

    def move_ship(self):
        if self.move_left:
            new_x = self.xcor() - 10
            if new_x > -380:
                self.setx(new_x)
        if self.move_right:
            new_x = self.xcor() + 10
            if new_x < 380:
                self.setx(new_x)