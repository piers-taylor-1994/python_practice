from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a colour: ")
colours = ("red", "orange", "yellow", "green", "blue", "purple")
turtles = []
game_is_running = True
winner = ""

for i in range(len(colours)):
    turtle = Turtle(shape="turtle")
    turtle.penup()
    turtle.color(colours[i])
    turtle.goto(x=-230, y=(-100 + (i * 40)))
    turtles.append(turtle)
    
while game_is_running:
    for t in turtles:
        move = random.randint(0, 5)
        t.forward(move)
        if t.position()[0] >= 230:
            winner = t.pencolor()
            game_is_running = False

if user_bet.lower() == winner.lower():
    print(f"Your bet won! {winner} was the winning turtle!")
else:
    print(f"Your bet lost! {winner} was the winning turtle!")
screen.exitonclick()