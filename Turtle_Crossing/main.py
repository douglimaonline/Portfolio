import time
from turtle import Screen
from game_settings import Ted, Car
from scoreboard import ScoreBoard
import random

screen = Screen()  # Setup screen
screen.setup(width=600, height=600)
screen.bgcolor('white')
screen.title('Crossing Turtle')
screen.tracer(0)
screen.listen()

ted = Ted()  # creating Ted object and setting his movements
screen.onkey(fun=ted.up, key='Up')
screen.onkey(fun=ted.down, key='Down')

score = ScoreBoard()  # creating ScoreBoard object

list_of_car = []  # list of cars created bellow

game_is_on = True  # starting the game
while game_is_on:
    screen.update()
    time.sleep(0.1)
    score.set_score()
    if ted.ycor() >= 280:  # Setting level up
        score.refresh_score()
        ted.set_position()
        car.velocity += 1
    if random.randint(0, 100) <= 20:
        car = Car()  # creating Car object
        list_of_car.append(car)
    for car in list_of_car:   # Test of impact with car
        if car.distance(ted) < 20:
            game_is_on = False
            score.game_over()
        else:   # setting Cars object movements
            car.moviment()
screen.exitonclick()
