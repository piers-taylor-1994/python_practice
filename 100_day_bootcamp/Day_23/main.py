import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.up, "Up")
screen.onkeypress(player.left, "Left")
screen.onkeypress(player.right, "Right")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.move()
    car_manager.generate()

    for car in car_manager.cars:
        if car.distance(player) < 20:
            game_is_on = False

    if player.ycor() == 280:
        player.reset()
        car_manager.increment_speed()
        scoreboard.increment_level()

game_over = Turtle(visible=False)
game_over.clear()
game_over.color("black")
game_over.write(arg=f"Game Over!", align="center", font=("Courier", 24, "normal"))

screen.exitonclick()