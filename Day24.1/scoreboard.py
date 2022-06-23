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
        with open("highscore.txt", mode="r") as file:
            self.highscore = int(file.read())

    def update_score(self):
        self.score += 1

    def display_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("highscore.txt", mode="w") as file:
                file.write(str(self.highscore))
        self.score = 0
        self.display_score()
