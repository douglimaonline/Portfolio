from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 20, 'bold')
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(0, 270)
        self.score = 0
        self.set_score()

    def set_score(self):
        self.write(f'Score: {self.score}',
                   move=False, align=ALIGNMENT, font=FONT)
    def refresh_score(self):
        self.score += 1
        self.clear()
        self.set_score()

    def game_over(self):
        self.goto(0, 0)
        self.write('Game Over',
                   move=False, align=ALIGNMENT, font=FONT)
