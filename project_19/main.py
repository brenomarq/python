from turtle import Turtle, Screen
from random import randint

def random_move(turtle: Turtle) -> None:
    """Makes the turtle move at a random step."""
    random_step = randint(1, 10)
    turtle.forward(random_step)


def check_position(turtle: Turtle) -> bool:
    """Return if the turtle has already gotten to the endline and won the race."""
    turtle_position = turtle.position()

    if turtle_position[0] >= 250:
        return True

    return False

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []
height = -60
for color in colors:
    turtle = Turtle(shape="turtle")
    turtle.color(color)
    turtle.penup()
    turtle.goto(x=-230, y=height)
    height += 20
    turtles.append(turtle)

winner = ""
should_continue = True
while should_continue:
    for turtle in turtles:
        random_move(turtle)

        is_finished = check_position(turtle)
        if is_finished:
            winner_color = turtle.color()[0]
            winner = winner_color
            should_continue = False
            break

if user_bet == winner:
    print(f"Great bet! The {winner} turtle won the the race.")
else:
    print(f"You lose! The winner was the {winner} turtle.")

screen.bye()
