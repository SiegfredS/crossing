from turtle import Screen


class NewScreen():

    def __init__(self):
        self.screen = Screen()
        self.setup()

    def setup(self):
        self.screen.title(titlestring="Crossing")
        self.screen.setup(width=1200, height=600)
        self.screen.bgcolor("black")

