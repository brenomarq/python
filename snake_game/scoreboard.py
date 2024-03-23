from turtle import Turtle
Y_POSITION = 280
TEXT_ALIGN = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(x=0, y=Y_POSITION)
        self.speed("fastest")
        self.display_score()

    def display_score(self) -> None:
        self.write(f"Score: {self.score}", align=TEXT_ALIGN, font=FONT)

    def increase_score(self) -> None:
        self.score += 1
        self.clear()
        self.display_score()

    def game_over(self) -> None:
        self.goto(0, 0)
        self.write("GAME OVER", align=TEXT_ALIGN, font=FONT)
