import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

P1_POSITION = (-350, 0)
P2_POSITION = (350, 0)

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

l_paddle = Paddle(initial_position=P1_POSITION)
r_paddle = Paddle(initial_position=P2_POSITION)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="w", fun=l_paddle.go_up)
screen.onkey(key="s", fun=l_paddle.go_down)
screen.onkey(key="Up", fun=r_paddle.go_up)
screen.onkey(key="Down", fun=r_paddle.go_down)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Detect collision with a wall
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce("y")

    # Detect collision with right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.bounce("x")

    # Detect when right paddle misses
    if ball.xcor() > 390:
        scoreboard.l_point()
        ball.restart()

    # Detect when left paddle misses
    if ball.xcor() < -390:
        scoreboard.r_point()
        ball.restart()

screen.exitonclick()
