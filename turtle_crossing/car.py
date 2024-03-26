import random
from turtle import Turtle
COLORS = ["green", "red", "blue", "orange", "pink", "yellow", "purple"]
STARTING_STEP = 5
STEP_INCREMENT = 1

class CarManager:
    def __init__(self) -> None:
        self.all_cars: list[Turtle] = []
        self.car_speed = STARTING_STEP

    def create_car(self) -> None:
        """Create a new car and adds to the manager."""
        random_chance = random.randint(1, 6)

        if random_chance == 1:
            new_car = Turtle(shape="square")
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_len=2)
            new_car.penup()
            new_car.setheading(180)
            new_position = (300, random.randint(-250, 250))
            new_car.goto(new_position)
            self.all_cars.append(new_car)

    def move_cars(self) -> None:
        """Make all the cars move across the screen."""
        for car in self.all_cars:
            car.forward(self.car_speed)

    def increase_speed(self) -> None:
        """Increase the movement speed of the cars by 10 units."""
        self.car_speed += STEP_INCREMENT
