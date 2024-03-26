from turtle import Turtle
INITIAL_POSITION = (0, -280)
STEP = 10
FINISH_LINE = 200

class Player(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.setheading(90)
        self.goto(INITIAL_POSITION)

    def move_up(self) -> None:
        """Make the turtle move upwards."""
        self.forward(STEP)

    def refresh(self) -> None:
        """Make the turtle go back to the initial position."""
        self.goto(INITIAL_POSITION)
