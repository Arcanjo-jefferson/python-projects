import time
from turtle import Screen
from car_manager import CarManager
from player import Player
from score_board import Scoreboard

screen = Screen()
screen.setup(width=600, height= 600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
score_board = Scoreboard()
screen.listen()
screen.onkey(player.turtle_moving, "Up")

car_speed = "fast"



game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.car()
    car_manager.car_movement()

#   Detect if the car hit the turtle
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            score_board.game_over()
            game_is_on = False

#   Detect successful crossing
    if player.turtle_finish():
        player.go_to_start()
        car_manager.level_up()
        score_board.score_point()





screen.exitonclick()