# turtleCrossing.py
#
# Python Bootcamp Day 23 - Turtle Crossing
# Usage:
#      Using the arrow keys, get your turtle across the road without being hit.
#
# Marceia Egler November 17, 2021

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Initialize screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Initialze player and car manager
player = Player()
car_manager = CarManager()

# Allow player to move up with up arrow button
player.move_turtle("Up")

game_is_on = True


while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.make_car()
    car_manager.move_cars()
    # Check for collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            player.game_over()
    player.reset_player()


screen.exitonclick()
