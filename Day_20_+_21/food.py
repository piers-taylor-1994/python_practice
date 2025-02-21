from turtle import Turtle
import random

MIN_LIMIT = -280
MAX_LIMIT = 280

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()
        

    def refresh(self):
        self.setposition(random.randint(MIN_LIMIT, MAX_LIMIT), random.randint(MIN_LIMIT, MAX_LIMIT))