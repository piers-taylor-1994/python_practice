from turtle import Turtle
ALIGNMENT = "center"
FONT = ("arial", 20, "bold")
Y_POSITION = 265

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.setposition(0, Y_POSITION)
        self.color("white")
        self.score = 0

        with open("Day_20_+_21/data.txt") as file:
            self.high_score = int(file.read())
        
        self.show_score(increment_score=False)

    def increment_score(self):
        self.show_score(increment_score=True)

    def show_score(self, increment_score):
        if increment_score:
            self.score += 1
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", font=FONT, align=ALIGNMENT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("Day 20 + 21/data.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.show_score(False)

    # def game_over(self):
    #     self.setposition(0, 0)
    #     self.write(arg=f"GAME OVER", font=FONT, align=ALIGNMENT)
        