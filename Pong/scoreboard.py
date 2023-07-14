from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('HololensMDL2 Assets', 80, 'bold')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('white')
        self.score = 0

    def set_score(self):
        self.write(f'{self.score}',
                   move=False, align=ALIGNMENT, font=FONT)

    def refresh_score(self):
        self.score += 1
        self.clear()
        self.set_score()

    def game_over(self):
        self.goto(0, 0)
        self.write('Game Over',
                   move=False, align=ALIGNMENT, font=FONT)
