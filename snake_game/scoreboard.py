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
        with open("data.txt") as data:
            self.highscore = int(data.read())
        self.set_score()

    def set_highscore(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as data:
                data.write(str(self.highscore))
        self.clear()
        self.score = 0
        self.set_score()

    def set_score(self):
        self.write(f'Score: {self.score}. High Score: {self.highscore}',
                   move=False, align=ALIGNMENT, font=FONT)

    def refresh_score(self):
        self.score += 1
        self.clear()
        self.set_score()
