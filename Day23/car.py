from turtle import Turtle
from random import choice, randint

# Constants
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class Car(Turtle):

    def __init__(self, starting_pos, min_move_speed, max_move_speed):
        super().__init__()
        self.shape("square")
        self.color(choice(COLORS))
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=2, outline=1)
        self.move_speed = randint(min_move_speed, max_move_speed)
        self.left(180)
        self.goto(starting_pos)

    def move_car(self):
        self.forward(self.move_speed)

    def increase_move_speed(self, move_increment):
        self.move_speed += move_increment
