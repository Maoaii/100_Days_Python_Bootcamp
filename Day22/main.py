import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

# Constants
PLAYER1_PADDLE_POS = (350, 0)
PLAYER2_PADDLE_POS = (-350, 0)

# Screen setup
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# Scoreboard setup
scoreboard = Scoreboard()

# Set up paddles
player1_paddle = Paddle(PLAYER1_PADDLE_POS)
player2_paddle = Paddle(PLAYER2_PADDLE_POS)

# Set up ball
ball = Ball()

# Listener events
screen.listen()
screen.onkey(player1_paddle.up, "Up")
screen.onkey(player1_paddle.down, "Down")
screen.onkey(player2_paddle.up, "w")
screen.onkey(player2_paddle.down, "s")

# Variables
game_is_on = True


def ball_oob_colliding():
    if ball.ycor() > (screen.window_height() / 2) - 20 or ball.ycor() < -(screen.window_height() / 2) + 20:
        ball.bounce()


def ball_paddle_colliding():
    if ball.distance(player1_paddle) < 50 and ball.xcor() > 320 or ball.distance(player2_paddle) < 50 and ball.xcor() < -320:
        ball.paddle_bounce()



def ball_score():
    if ball.xcor() > 380:
        ball.reset()
        scoreboard.l_scored()
    if ball.xcor() < -380:
        ball.reset()
        scoreboard.r_scored()


while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    ball_oob_colliding()
    ball_paddle_colliding()
    ball_score()

screen.exitonclick()
