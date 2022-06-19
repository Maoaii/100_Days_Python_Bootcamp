import random
from turtle import Turtle, Screen
from random import randint

# Constants
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
Y_POSITIONS = [-100, -60, -20, 20, 60, 100]

# Variables
is_race_on = False
turtles = []

# Instance screen
screen = Screen()

# Set up screen size
screen.setup(width=500, height=400)

# Set up turtles
for turtle_index in range(0, 6):
    boy = Turtle(shape="turtle")
    boy.color(COLORS[turtle_index])
    boy.penup()
    boy.goto(x=(-screen.window_width()/2) + 20, y=Y_POSITIONS[turtle_index])
    turtles.append(boy)

# Input user for a turtle bet
user_bet = screen.textinput(title="Make your bet.", prompt="Which turtle will win the race? Enter a color: ")

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        # Check if a turtle won
        if turtle.xcor() > screen.window_width()/2 - 20:
            is_race_on = False
            winning_color = turtle.pencolor()

            # Print final message
            if winning_color == user_bet:
                print(f"You won! The {winning_color} turtle is the winner!")
            else:
                print(f"You lost :c. The {winning_color} turtle is the winner!")
        
        # Move turtle random distance
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()