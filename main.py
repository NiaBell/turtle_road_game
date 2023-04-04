import time
from turtle import Turtle, Screen
from player import Player
from Car_manager import Car


screen=Screen()
screen.screensize(canvwidth=800, canvheight=600)
screen.tracer(0)
screen.bgcolor("black")

player = Player()
car = Car()


screen.listen()
screen.onkey(player.move,'Up')



game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.add_car()



screen.exitonclick()
