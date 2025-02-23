from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.i = 0
        self.cap = 5
        self.move_distance = STARTING_MOVE_DISTANCE
        self.generate()

    def generate(self):
        if self.i % self.cap == 0:
            car = Turtle("square")
            car.penup()
            car.shapesize(stretch_wid=1, stretch_len=3)
            car.color(random.choice(COLORS))
            car.goto(300, random.randint(-260, 260))
            car.setheading(180)
            self.cars.append(car)
        
    def move(self):
        self.i += 1
        for c in self.cars:
            c.forward(self.move_distance)

    def increment_speed(self):
        self.move_distance += MOVE_INCREMENT
        self.cap -= 1
