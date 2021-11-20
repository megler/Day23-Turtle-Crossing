from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self) -> None:
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.move_speed = MOVE_INCREMENT * 0.10

    def make_car(self):
        """Everytime car_gen rolls a 1 generate a car and push to init."""
        car_gen = random.randint(1, 6)
        if car_gen == 1:
            new_car = Turtle()
            new_car.penup()
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            new_car.shape("square")
            new_car.shapesize(1, 2, 0)
            new_car.color(random.choice(COLORS))
            self.all_cars.append(new_car)

    def move_cars(self) -> None:
        """Move cars at constant speed."""
        for car in self.all_cars:
            car.backward(self.car_speed)

    def speed_up(self) -> None:
        """If player levels up, cars go faster"""
        self.move_speed += MOVE_INCREMENT
