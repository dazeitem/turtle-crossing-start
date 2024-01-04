from turtle import Turtle
from random import randint, choice

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.create_car()
        self.increment_multiplier = 0

    def create_car(self):
        random_chance = choice(range(0, 6))
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.setheading(180)
            new_car.goto(280, randint(-250, 250))
            new_car.color(choice(COLORS))
            self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.forward(STARTING_MOVE_DISTANCE + MOVE_INCREMENT*self.increment_multiplier)
            if car.xcor() < -280:
                car.hideturtle()

    def implement_level(self, level):
        if level > 0:
            self.increment_multiplier = level
