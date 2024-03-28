from turtle import Turtle
Y_POSITION = 280
TEXT_ALIGN = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.high_score = self.get_highscore()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(x=0, y=Y_POSITION)
        self.speed("fastest")
        self.display_score()

    def display_score(self) -> None:
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=TEXT_ALIGN, font=FONT)

    def increase_score(self) -> None:
        self.score += 1
        self.display_score()

    def restart(self) -> None:
        """Restart the game and store the high score."""
        self.set_highscore()
        self.score = 0
        self.display_score()

    def get_highscore(self) -> int:
        """Get the high score from the txt file and set it to the game."""
        with open("data.txt") as file:
            high_score = int(file.read())

        return high_score

    def set_highscore(self) -> None:
        """Set the new high score for the game."""
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as file:
                file.write(str(self.score))

