from turtle import colormode, Screen, Turtle
from random import choice

def adjust_position(turn: int):
    if turn % 2 == 0:
        timmy.right(90)
        timmy.forward(50)
        timmy.right(90)
    else:
        timmy.left(90)
        timmy.forward(50)
        timmy.left(90)
    timmy.forward(40)



colormode(255)
COLOR_LIST = [(84, 254, 155), (173, 146, 118), (254, 250, 254),
(245, 39, 191), (158, 107, 56), (2, 1, 176), (151, 54, 251), (221, 254, 101)]

timmy = Turtle()
timmy.pensize(5)
timmy.penup()
timmy.hideturtle()

timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)

for i in range(10):
    for _ in range(10):
        timmy.dot(20, choice(COLOR_LIST))
        timmy.forward(40)

    adjust_position(i + 1)

screen = Screen()
screen.exitonclick()

