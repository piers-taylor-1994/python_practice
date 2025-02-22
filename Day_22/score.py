from turtle import Turtle
ALIGNMENT = "center"
FONT = ("arial", 20, "bold")
Y_POSITION = 265

class Score(Turtle):
    def __init__(self, xcord, shape = "classic", undobuffersize = 1000, visible = False, ):
        super().__init__(shape, undobuffersize, visible)
        self.score = 0
        self.color("white")
        self.setposition(xcord, 270)
        self.show_score(False)

    def show_score(self, increment_score):
        if increment_score:
            self.score += 1
        self.clear()
        self.write(arg=f"{self.score}", font=FONT, align=ALIGNMENT)