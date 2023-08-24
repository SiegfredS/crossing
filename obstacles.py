import turtle
from turtle import Turtle
import random

turtle.colormode(255)


class Obstacle:

    def __init__(self,
                 difficulty=1):
        self.obstacle_list = []
        self.difficulty = difficulty
        self.obstacle_move_distance = 2 + 2*difficulty
        self.initial_obstacles()


    @staticmethod
    def generate_obstacle(start_x=0, start_y=0):
        new_obstacle = Turtle()
        new_obstacle.color(random.randint(0, 255),
                           random.randint(0, 255),
                           random.randint(0, 255))
        new_obstacle.shape("square")
        new_obstacle.shapesize(stretch_len=random.uniform(1, 15),
                               stretch_wid=random.uniform(0.5, 1.5))
        new_obstacle.penup()
        if start_x != 0 and start_y != 0:
            new_obstacle.goto(x=start_x, y=start_y)
        else:
            new_obstacle.goto(x=random.randint(-700, 1000), y=random.randint(-230, 300))
        return new_obstacle

    def initial_obstacles(self):
        for i in range(4*self.difficulty + 10):
            self.obstacle_list.append(self.generate_obstacle())
        return

    def move_obstacles(self):
        for obstacle in self.obstacle_list:
            obstacle.goto(x=obstacle.xcor() - self.obstacle_move_distance, y=obstacle.ycor())
        return

    def replenish_obstacles(self):
        start_x = random.randint(600, 800)
        start_y = random.randint(-240, 240)
        for obstacle in self.obstacle_list:
            if obstacle.xcor() <= -800:
                self.obstacle_list.remove(obstacle)
                self.obstacle_list.append(self.generate_obstacle(start_x=start_x, start_y=start_y))
            else:
                pass

    def increase_difficulty(self):
        self.difficulty += 1

    def reset_board(self):
        for obstacle in self.obstacle_list:
            obstacle.hideturtle()
            self.obstacle_list.remove(obstacle)
        self.initial_obstacles()


