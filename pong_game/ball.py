from turtle import Turtle
STEP = 2

class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed("slowest")
        self.x_move = STEP
        self.y_move = STEP

    def move(self) -> None:
        """Make the ball move."""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move

        self.goto(x=new_x, y=new_y)

    def bounce(self, axis: str) -> None:
        "Make the ball bounce and change movement."
        if axis == "y":
            self.y_move *= -1

        elif axis == "x":
            self.x_move *= -1



