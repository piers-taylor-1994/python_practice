from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.tracer(0)

paddle = Paddle(-350)
robot_paddle = Paddle(350)
ball = Ball()
my_score = Score(-50)
robot_score = Score(50)

screen.listen()
screen.onkeypress(paddle.up, "Up")
screen.onkeypress(paddle.down, "Down")
screen.onkeypress(ball.wall_reflect, "Left")

game_is_running = True
while game_is_running:
    time.sleep(ball.speed)
    screen.update()
    
    ball.move()
    robot_paddle.auto_move()

    if ball.distance(paddle) < 50 and ball.xcor() < -340 or ball.distance(robot_paddle) < 30 and ball.xcor() > 340:
        ball.paddle_reflect()
    
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.wall_reflect()
            
    if ball.xcor() < -360:
        robot_score.show_score(True)
        ball.reset()
    elif ball.xcor() > 360:
        my_score.show_score(True)
        ball.reset()
    

screen.exitonclick()