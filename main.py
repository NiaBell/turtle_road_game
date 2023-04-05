import time
from turtle import Turtle, Screen
from player import Player
from Car_manager import Car
from scoreboard import ScoreBoard


screen=Screen()
screen.screensize(canvwidth=800, canvheight=600)
screen.tracer(0)
screen.bgcolor("black")

player = Player()
car = Car()
scoreboard = ScoreBoard()


screen.listen()
screen.onkey(player.move,'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.add_car()
    car.move()
    for cars in car.cars:
        if cars.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False
    if player.ycor() > 260:
        player.reset_position()
        scoreboard.scored()
        car.speed_up()


screen.exitonclick()
