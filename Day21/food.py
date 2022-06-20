from turtle import Turtle
from random import randint


class Food(Turtle):

    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")

        self.set_random_pos()

    def set_random_pos(self):
        x_pos = randint(-int((self.screen_width / 2)), self.screen_width / 2)
        y_pos = randint(-int((self.screen_height / 2)), self.screen_height / 2)
        self.goto(x_pos, y_pos)
