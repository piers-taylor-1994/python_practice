from turtle import Turtle

class Ball(Turtle):
    def __init__(self, shape = "circle", undobuffersize = 1000, visible = True):
        super().__init__(shape, undobuffersize, visible)
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.speed = 0.05
        self.reset()

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.setposition(new_x, new_y)

    def reset(self):
        self.setposition(0, 0)
        self.paddle_reflect()
        self.speed = 0.05

    def wall_reflect(self):
        self.y_move *= -1

    def paddle_reflect(self):
        self.x_move *= -1
        self.speed *= 0.9
