from turtle import Turtle

class MapWritter(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.hideturtle()
        self.penup()

    def write_answer(self, name: str, position: tuple[float, float]) -> None:
        """Write the name of the state in the specified location."""
        self.goto(position)
        self.write(name, align="center")
