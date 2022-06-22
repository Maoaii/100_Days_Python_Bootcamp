from car import Car
from random import randint

CAR_SPAWN_BUFFER = 60
STARTING_SPAWN_TIMER = 5
SPAWN_TIMER_DECREMENT = 1
MOVE_INCREMENT = 4


class CarManager:

    def __init__(self, screen_width, screen_height):
        self.cars = []
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.spawn_timer = STARTING_SPAWN_TIMER
        self.min_move_speed = 4
        self.max_move_speed = 6

    def spawn_car(self):
        self.spawn_timer -= SPAWN_TIMER_DECREMENT
        if self.spawn_timer <= 0:
            x_pos = self.screen_width / 2
            y_pos = randint(-int((self.screen_height / 2)) + CAR_SPAWN_BUFFER, int((self.screen_height / 2)) - CAR_SPAWN_BUFFER)

            car = Car((x_pos, y_pos), self.min_move_speed, self.max_move_speed)
            self.cars.append(car)
            self.spawn_timer = STARTING_SPAWN_TIMER

    def move_cars(self):
        for car in self.cars:
            car.move_car()

    def player_collided_car(self, player_pos):
        for car in self.cars:
            if car.distance(player_pos) < 20:
                return True

    def increase_car_speed(self):
        self.min_move_speed += MOVE_INCREMENT
        self.max_move_speed += MOVE_INCREMENT
        for car in self.cars:
            car.increase_move_speed(MOVE_INCREMENT)
