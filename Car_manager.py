from turtle import Turtle
import random
COLORS=["red","orange","green","blue","purple","yellow"]


class Car():
    def __init__(self):
        self.cars = []
        self.speed = 5

    def add_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 2:
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            newy = random.randrange(-240, 250)
            newx = random.randrange(380,410)
            new_car.goto(newx, newy)
            new_car.setheading(180)
            self.cars.append(new_car)


    def move(self):
        for car in self.cars:
            car.forward(self.speed)

    def speed_up(self):
        self.speed += 1

