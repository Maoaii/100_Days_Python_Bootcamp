from turtle import Turtle, Screen, colormode
from data import color_list
from random import choice

color_data = color_list

square_size = 10
dot_spacing = 50
dot_size = 20

screen = Screen()

boy = Turtle()
boy.shape("turtle")
boy.speed("fastest")
boy.penup()
boy.hideturtle()
colormode(255)


def pick_random_color():
    return choice(color_data)


def get_new_row_pos(row):
    return -screen.window_width() / 2 + dot_spacing, -screen.window_height() / 2 + ((row+1) * dot_spacing)


def draw_dot():
    boy.pendown()
    boy.dot(dot_size, pick_random_color())
    boy.penup()


for row in range(square_size):
    boy.setpos(get_new_row_pos(row))
    for _ in range(square_size):
        draw_dot()
        boy.forward(dot_spacing)



screen.exitonclick()
