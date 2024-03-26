from turtle import Turtle
ALIGN = "center"
FONT = ("Courier", 80, "normal")

class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=250)
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def update_score(self) -> None:
        """Updates the scoreboard with the current score."""
        self.clear()
        self.write(f"{self.l_score} {self.r_score}", align=ALIGN, font=FONT)

    def l_point(self) -> None:
        """Increases the left paddle score by one point."""
        self.l_score += 1
        self.update_score()

    def r_point(self) -> None:
        """Increases the right paddle score by one point."""
        self.r_score += 1
        self.update_score()
