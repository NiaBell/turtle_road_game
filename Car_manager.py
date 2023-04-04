from turtle import Turtle
import random
COLORS=["red","orange","green","blue","purple","yellow"]


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.cars= []
        self.Generate_car()

    def Generate_car(self):
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.color(random.choice(COLORS))
        self.penup()
        newy = random.randrange(-300, 300)
        self.goto(400, newy)
        self.setheading(180)

    def add_car(self):
        new_car= Turtle("square")
        new_car.color(random.choice(COLORS))
        new_car.shapesize(stretch_wid=1, stretch_len=5)
        new_car.penup()
        newy = random.randrange(-240, 300)
        newx = random.randrange(380,400)
        new_car.goto(newx, newy)
        new_car.setheading(180)
        self.cars.append(new_car)



