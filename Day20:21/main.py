import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# Constants
HEAD_OFFSET = 20

# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snek")
screen.tracer(0)

# Variables
game_is_on = True

# Objects
snake = Snake()
food = Food(screen.window_width(), screen.window_height())
scoreboard = Scoreboard(screen.window_height())

# Listener events
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.update()


def detect_food_collision():
    if snake.head.distance(food) < 15:
        food.set_random_pos()
        scoreboard.update_score()
        snake.extend()


def detect_wall_collision():
    head_x_pos = snake.head.xcor()
    head_y_pos = snake.head.ycor()
    if head_x_pos > (screen.window_width() / 2) - HEAD_OFFSET or head_x_pos < -(
            screen.window_width() / 2) + HEAD_OFFSET or head_y_pos > (
            screen.window_height() / 2) - HEAD_OFFSET or head_y_pos < -(screen.window_height() / 2) + HEAD_OFFSET:
        return True


def detect_tail_collision():
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            return True


while game_is_on:
    screen.update()
    scoreboard.display_score()
    time.sleep(0.1)
    snake.move()

    detect_food_collision()
    if detect_wall_collision() or detect_tail_collision():
        game_is_on = False
        scoreboard.game_over()

screen.exitonclick()
