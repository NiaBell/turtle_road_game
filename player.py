from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("white")
        self.penup()
        self.setheading(90)
        self.goto(0,-280)

    def move(self):
        self.forward(10)

    def reset_position(self):
        self.goto(0, -280)