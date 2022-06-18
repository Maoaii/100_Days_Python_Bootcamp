from turtle import Turtle, Screen

# Constants
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
Y_POSITIONS = [-100, -60, -20, 20, 60, 100]

# Instance screen
screen = Screen()

# Set up screen size
screen.setup(width=500, height=400)

# Input user for a turtle bet
user_bet = screen.textinput(title="Make your bet.", prompt="Which turtle will win the race? Enter a color: ")

# Set up turtle position
for turtle_index in range(0, 6):
    boy = Turtle(shape="turtle")
    boy.color(COLORS[turtle_index])
    boy.penup()
    boy.goto(x=(-screen.window_width()/2) + 20, y=Y_POSITIONS[turtle_index])



screen.exitonclick()