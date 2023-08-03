from turtle import Turtle
import random

COLOR_LIST = ('blue', 'red', 'aqua', 'yellow', 'orange', 'black', 'violet', 'brown', 'pink')


class Ted(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('green')
        self.penup()
        self.setheading(90)
        self.set_position()

    def set_position(self):
        self.goto(0, -280)

    def up(self):
        self.forward(20)

    def down(self):
        self.forward(-20)


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.penup()
        self.setheading(180)
        self.color(random.choice(COLOR_LIST))
        self.shapesize(1, 2, 5)
        self.goto(260, random.randint(-200, 200))
        self.velocity = 5

    def moviment(self):
        self.forward(self.velocity)
