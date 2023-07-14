from turtle import Screen
from game import Paddle, Ball
from scoreboard import ScoreBoard
import random
screen = Screen()  # (y=400, x=300)
screen.bgcolor('black')
screen.listen()
screen.tracer(0)  # screen off

# initiating the paddles
paddle1 = Paddle()
paddle1.goto(450, 0)
paddle2 = Paddle()
paddle2.goto(-450, 0)

# initiating score
scoreboard1 = ScoreBoard()
scoreboard1.goto(120, 300)
scoreboard1.set_score()
scoreboard2 = ScoreBoard()
scoreboard2.goto(-120, 300)
scoreboard2.set_score()

# initiating the ball
ball = Ball()
STARTING_BALL = [(-430, 0), (430, 0)]
ball.goto(random.choice(STARTING_BALL))
ball.setheading(random.choice([45, 135, 225, 315]))

# setting moves to paddles
screen.onkey(fun=paddle1.moveup, key='Up')
screen.onkey(fun=paddle1.movedown, key='Down')
screen.onkey(fun=paddle2.moveup, key='w')
screen.onkey(fun=paddle2.movedown, key='s')
screen.tracer(1)   # screen on

# starting game
is_game_on = True
while is_game_on:
    if ball.ycor() > 385 or ball.ycor() < -380:
        ball.setheading(ball.heading()*-1)
        ball.fast()
    if ball.xcor() > 430 and ball.distance(paddle1) < 100 or ball.xcor() < -430 and ball.distance(paddle2) < 100:
        ball.setheading(180-ball.heading())
        ball.fast()
    elif ball.xcor() > 440 or ball.xcor() < -440:
        if ball.distance(paddle1) < ball.distance(paddle2):
            scoreboard2.refresh_score()
        else:
            scoreboard1.refresh_score()
        is_game_on = False
    ball.move()

screen.exitonclick()
