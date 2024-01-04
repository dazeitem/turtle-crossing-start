import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

LEVEL = 0


def main():
    global LEVEL
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.title("Turtle Crossing")
    screen.tracer(0)

    player = Player()
    car_manager = CarManager()
    score = Scoreboard(LEVEL)

    screen.listen()
    screen.onkey(player.move_player, "Up")

# Creates a new car every sixth while-cycle
    game_is_on = True
    while game_is_on:
        time.sleep(0.1)
        screen.update()
        car_manager.implement_level(LEVEL)
        car_manager.move_cars()
        car_manager.create_car()

# Detects if player has completed a level and implements increment multiplier
        if player.ycor() >= 280:
            screen.clear()
            score.give_point()
            player.reset_player()
            LEVEL += 1
            main()

        for car in car_manager.cars:
            if car.distance(player) < 15:
                game_is_on = False
                score.game_over()

    screen.exitonclick()
if __name__ == "__main__":
    main()
