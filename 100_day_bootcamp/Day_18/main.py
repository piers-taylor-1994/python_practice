import random
import turtle as t
import colorgram

turtle = t.Turtle()
t.colormode(255)

def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

# for i in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(90)

colours = ["navy", "cyan", "medium aquamarine", "dark green", "khaki", "burlywood", "firebrick", "orange red", "light pink", "thistle"]
directions = [0, 90, 180, 270]
turtle.speed("fastest")
# turtle.pensize(10)

def draw_spiro(gap):
    for _ in range (int(360/ gap)):
        turtle.circle(100)
        turtle.color(random_colour())
        turtle.setheading(turtle.heading() + gap)

draw_spiro(5)

# for i in range(0, 90):
#     turtle.home()
#     turtle.right(4 * i)
#     turtle.circle(100)
#     turtle.color(random_colour())
#     # timmy_the_turtle.right(random.choice(directions))
#     # timmy_the_turtle.forward(30)
#     # for j in range(i):
#     #     angle = 360 / i
#     #     timmy_the_turtle.right(angle)
#     #     timmy_the_turtle.forward(100)