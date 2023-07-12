import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)
screen.listen()

snake = Snake()  # creating snake object and setting his movements
screen.onkey(fun=snake.up, key='Up')
screen.onkey(fun=snake.down, key='Down')
screen.onkey(fun=snake.right, key='Right')
screen.onkey(fun=snake.left, key='Left')

food = Food()  # Creating food
scoreboard = ScoreBoard()  # Creating scoreboard

game_is_on = True  # starting the game
while game_is_on:
    screen.update()
    time.sleep(0.1)
    scoreboard  # Setup score
    snake.move()
    if snake.head.distance(food) < 15:  # Detecting collision with food
        scoreboard.refresh_score()
        snake.create_new_segment()
        food.refresh()

    if snake.head.xcor() > 280 or snake.head.xcor() < -290 or snake.head.ycor() > 300 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
