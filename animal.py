from turtle import Turtle
from obstacles import Obstacle

FONT = ("Courier", 36, "normal")
ALIGN = "left"

class Animal(Turtle):

    def __init__(self):
        super().__init__()
        self.initialize()
        self.move_distance = 10
        self.score = 0
        self.writer = Turtle()
        self.writer.penup()
        self.writer.hideturtle()
        self.writer.color("white")
        self.writer.goto(x=-600, y=240)

    def initialize(self):
        self.speed(speed=10)
        self.penup()
        self.shape(name="turtle")
        self.color("orange")
        self.setheading(90)
        self.shapesize(stretch_wid=2, stretch_len=2)
        self.goto(x=0, y=-280)
        return

    def move_up(self):
        self.forward(self.move_distance)
        return

    def move_down(self):
        if self.ycor() > -280:
            self.goto(x=self.xcor(), y=self.ycor() - self.move_distance)
        else:
            pass
        return

    def win(self):
        if self.ycor() > 280:
            self.goto(x=self.xcor(), y=-280)
            self.add_score()
            self.update_score()
            return True
        else:
            return False

    def lose(self, obstacles:Obstacle):
        for obstacle in obstacles.obstacle_list:
            if self.distance(obstacle) <= 30:
                return True
            else:
                pass
        return False

    def add_score(self):
        self.score += 1

    def update_score(self):
        self.writer.clear()
        self.writer.write(f"Score : {self.score}", align=ALIGN, font=FONT)
