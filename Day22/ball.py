from turtle import Turtle

# Constants
BALL_SHAPE = "circle"
BALL_COLOR = "white"
BALL_SIZE = 0.7
MOVEMENT_SPEED = 10


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color(BALL_COLOR)
        self.shape(BALL_SHAPE)
        self.shapesize(BALL_SIZE)
        self.x_move = MOVEMENT_SPEED
        self.y_move = MOVEMENT_SPEED
        self.move_speed = 0.09

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1

    def paddle_bounce(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset(self):
        self.goto(0, 0)
        self.paddle_bounce()
        self.move_speed = 0.09
