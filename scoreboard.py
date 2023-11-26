from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.pen()
        self.left_score = 0
        self.right_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 240)
        self.write(self.left_score, align="center", font=("Courier", 30, "bold"))
        self.goto(100, 240)
        self.write(self.right_score, align="center", font=("Courier", 30, "bold"))

    def score_up(self, xcor):
        if xcor > 500:
            self.left_score += 1
        elif xcor < -500:
            self.right_score += 1
