from turtle import Turtle
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto((-280, 270))
        self.level = 1
        self.display_level()

    def increase_level(self) -> None:
        """Increase the level by one unit."""
        self.level += 1
        self.clear()
        self.display_level()

    def display_level(self) -> None:
        """Show the current level of the player."""
        self.write(f"Level {self.level}", font=FONT)

    def game_over(self) -> None:
        """Show that the game has ended."""
        self.goto((0, 0))
        self.write("GAME OVER")

