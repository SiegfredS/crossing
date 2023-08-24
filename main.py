from screen import NewScreen
from animal import Animal
from obstacles import Obstacle
import time

screen = NewScreen()
my_screen = screen.screen
my_screen.tracer(0)
my_turtle = Animal()
my_turtle.update_score()
obstacle = Obstacle(difficulty=2)

my_screen.update()
my_screen.listen()
my_screen.onkeypress(key="Up", fun=my_turtle.move_up)
my_screen.onkeypress(key="Down", fun=my_turtle.move_down)

is_playing = True

while is_playing:
    time.sleep(0.0167)
    my_screen.update()
    obstacle.move_obstacles()
    obstacle.replenish_obstacles()

    if my_turtle.win():
        obstacle.increase_difficulty()
        obstacle.reset_board()
    else:
        pass

    if my_turtle.lose(obstacle):
        is_playing = False
    else:
        pass


my_screen.exitonclick()
