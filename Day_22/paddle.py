from turtle import Turtle
LIMIT = 280
MOVE = 20
UP = 90
DOWN = 270

class Paddle(Turtle):
    def __init__(self, xcord, shape = "square", undobuffersize = 1000, visible = True):
        super().__init__(shape, undobuffersize, visible)
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.setposition(xcord, 0)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.direction = 1

    def add_segment(self, xcoord, ycoord):
        turtle = Turtle(shape="square")
        
        self.segments.append(turtle)

    def up(self):
        self.move(1)

    def down(self):
        self.move(-1)

    def move(self, direction):
        self.setposition(self.xcor(), self.ycor() + (20 * direction))

    def auto_move(self):
        if self.ycor() >= LIMIT:
            self.direction = -1
        elif self.ycor() <= -LIMIT:
            self.direction = 1
        
        self.setposition(self.xcor(), self.ycor() + (30 * self.direction))