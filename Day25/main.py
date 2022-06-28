import turtle
import pandas

# Setup screen
screen = turtle.Screen()
screen.title("U.S. States Game")

# Add image as a shape
image = "blank_states_img.gif"
screen.addshape(image)

# Set up turtle
turtle.shape(image)
game_is_on = True

# Set up datas
data = pandas.read_csv("50_states.csv")
states = data.state.to_list()
guessed_states = []

while len(guessed_states) < len(states):
    # User input
    answer_state = screen.textinput(title=f"{len(guessed_states)}/{len(states)} states guessed",
                                    prompt="What's another state's name?").title()
    # If user wants to exit, save missing states to a new csv
    if answer_state == "Exit":
        missing_states = [state for state in states if state not in guessed_states]
        pandas.DataFrame(missing_states).to_csv("states_guessed.csv")
        break

    # If guessed correctly, write on the correct coordinates the name of the state
    # and update variables
    if answer_state in states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

screen.exitonclick()
