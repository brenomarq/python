from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_STEP = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self) -> None:
        self.segments: list[Turtle] = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self) -> None:
        """Create a default snake."""
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position: tuple[int, int]):
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self) -> None:
        """Make the snake move."""
        for index in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[index - 1].pos()[0]
            new_y = self.segments[index - 1].pos()[1]
            self.segments[index].goto(x=new_x, y=new_y)
        self.head.forward(MOVE_STEP)

    def up(self) -> None:
        """Make the snake move upwards."""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self) -> None:
        """Make the snake move downwards."""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self) -> None:
        """Make the snake move to the left."""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self) -> None:
        """Make the snake move to the right."""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self) -> None:
        """Reset the game and create a new snake in the middle of the screen."""
        for segment in self.segments:
            segment.goto((1000, 1000))

        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

