import turtle as t
from turtle import Screen

turtle = t.Turtle()
screen = Screen()

def move_foward():
    turtle.forward(10)

def move_backward():
    turtle.forward(-10)

def turn_left():
    turtle.left(5)

def turn_right():
    turtle.right(5)

screen.listen()
#The below functions don't have parameters as 1) that calls it straight away 2) Functions as arguments are parameterless
screen.onkeypress(move_foward, "w")
screen.onkeypress(move_backward, "s")
screen.onkeypress(turn_left, "a")
screen.onkeypress(turn_right, "d")
screen.onkey(turtle.reset, "c")
screen.exitonclick()