from turtle import Turtle

# Constants
PADDLE_WIDTH = 1
PADDLE_HEIGHT = 5
PADDLE_COLOR = "white"
PADDLE_SHAPE = "square"
MOVEMENT_SPEED = 20


class Paddle(Turtle):

    def __init__(self, paddle_pos):
        super().__init__()
        self.shape(PADDLE_SHAPE)
        self.penup()
        self.color(PADDLE_COLOR)
        self.shapesize(stretch_wid=PADDLE_HEIGHT, stretch_len=PADDLE_WIDTH)
        self.goto(paddle_pos)

    def up(self):
        self.goto(self.xcor(), self.ycor() + MOVEMENT_SPEED)

    def down(self):
        self.goto(self.xcor(), self.ycor() - MOVEMENT_SPEED)