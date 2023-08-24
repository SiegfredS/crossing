from turtle import Turtle


class Animal(Turtle):

    def __init__(self):
        super().__init__()
        self.initialize()

    def initialize(self):
        self.penup()
        self.shape(name="turtle")
        self.color("orange")
        self.goto(x=0, y=0)