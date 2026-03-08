import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
STARTING_POSITION = ()
# size 20x40

class CarManager:
    def __init__(self):
        self.all_cars =[]
        self.car_speed = STARTING_MOVE_DISTANCE

    def car(self):
        random_chance = random.randint(1,6)
        if random_chance ==1:
            new_car = Turtle("square")
            new_car.shapesize(1, 2)
            new_car.penup()
            new_car.goto(x=300, y=random.randint(-250, 250))
            new_car.color(random.choice(COLORS))
            self.all_cars.append(new_car)

    def car_movement(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT





