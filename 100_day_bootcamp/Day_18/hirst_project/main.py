import colorgram
import turtle as t
import random

turtle = t.Turtle()
t.colormode(255)

# colours = colorgram.extract("Day 18\hirst_project\image.jpeg", 80)
# colours_tuple = []
# for c in colours:
#     colours_tuple.append((c.rgb.r, c.rgb.g, c.rgb.b))

colours_tuple = [(54, 89, 131), (146, 91, 40), (140, 26, 48), (222, 206, 108), (132, 177, 203), (46, 55, 103), (158, 46, 83), (167, 160, 39), (128, 189, 143), (83, 20, 44), (37, 42, 67), (186, 93, 105), (186, 139, 170), (84, 123, 181), (59, 39, 31), (79, 153, 165), (88, 157, 91), (195, 79, 71), (161, 202, 220), (45, 74, 77), (80, 73, 44), (57, 131, 124), (218, 176, 187), (220, 183, 167), (166, 207, 163), (179, 188, 211), (149, 37, 35), (46, 73, 71), (45, 65, 62)]
turtle.penup()
turtle.hideturtle()
home = (-250, -250)

def paint_painting():
    for i in range(10):
        for j in range(10):
            turtle.setposition(home[0] + 50 * j, home[1] + 50 * i)
            turtle.dot(25, random.choice(colours_tuple))

paint_painting()