from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self, shape = "classic", undobuffersize = 1000, visible = False):
        super().__init__(shape, undobuffersize, visible)
        self.color("black")
        self.goto(-200, 250)
        self.level = 1
        self.show_text()

    def show_text(self):
        self.clear()
        self.write(arg=f"Level: {self.level}", align="center", font=("Courier", 24, "normal"))

    def increment_level(self):
        self.level += 1
        self.show_text()
