import time
from turtle import Screen
from paddle import Paddle
from ball import Ball

P1_POSITION = (-350, 0)
P2_POSITION = (350, 0)

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle(initial_position=P1_POSITION)
l_paddle = Paddle(initial_position=P2_POSITION)
ball = Ball()

screen.listen()
screen.onkey(key="w", fun=r_paddle.go_up)
screen.onkey(key="s", fun=r_paddle.go_down)
screen.onkey(key="Up", fun=l_paddle.go_up)
screen.onkey(key="Down", fun=l_paddle.go_down)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.01)
    ball.move()

    # Detect collision with a wall
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce("y")

    # Detect collision with left paddle
    if ball.distance(r_paddle) < 15 or (ball.ycor() > 315 and ball.distance(r_paddle) < 50):
        ball.bounce("x")

screen.exitonclick()
