from turtle import Turtle

paddle = Turtle()


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('square')
        self.penup()
        self.left(90)
        self.shapesize(1, 10, 5)

    def moveup(self):
        self.forward(40)

    def movedown(self):
        self.forward(-40)


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.penup()
        self.speed('fastest')
        self.shapesize(1, 1, 0)
        self.velocit = 10

    def move(self):
        self.forward(self.velocit)

    def fast(self):
        self.velocit += 0.5
