import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Scoreboard setup
scoreboard = Scoreboard((-(screen.window_width() / 2) + 75, (screen.window_height() / 2) - 40))

# Player setup
player = Player()

# Car manager setup
car_manager = CarManager(screen.window_width(), screen.window_height())

# Listener events
screen.listen()
screen.onkey(player.move_up, "Up")
screen.onkey(player.move_up, "w")

game_is_on = True
while game_is_on:
    time.sleep(0.1)

    # Spawn cars
    car_manager.spawn_car()
    car_manager.move_cars()

    # Check if player crossed finish line
    if player.crossed_finish_line():
        player.reset_position()
        car_manager.increase_car_speed()
        scoreboard.update_level()

    # Check if player collided with car
    if car_manager.player_collided_car(player.pos()):
        game_is_on = False
        scoreboard.game_over()

    screen.update()

screen.exitonclick()
