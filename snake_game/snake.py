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
        for index in range(3):
            segment = Turtle("square")
            segment.color("white")
            segment.penup()
            segment.goto(STARTING_POSITIONS[index])
            self.segments.append(segment)

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

