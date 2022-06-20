from turtle import Turtle

# Constants
ALIGNMENT = "center"
FONT_SIZE = 25
FONT = ("Courier", FONT_SIZE, "normal")
TOP_OFFSET = FONT_SIZE + 5


class Scoreboard(Turtle):

    def __init__(self, screen_height):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=(screen_height / 2) - TOP_OFFSET)
        self.score = 0

    def update_score(self):
        self.clear()
        self.score += 1

    def display_score(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
