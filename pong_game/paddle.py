from turtle import Turtle
STEP = 20

class Paddle(Turtle):
    def __init__(self, initial_position: tuple[int, int] = (0, 0)) -> None:
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=1.5, stretch_wid=5)
        self.penup()
        self.goto(initial_position)

    def go_up(self) -> None:
        """Move the paddle upward."""
        x_position, y_position = self.position()

        if y_position < 250:
            self.goto(x=x_position, y=y_position + STEP)

    def go_down(self) -> None:
        """Move the paddle downward."""
        x_position, y_position = self.position()

        if y_position > -250:
            self.goto(x=x_position, y=y_position - STEP)

