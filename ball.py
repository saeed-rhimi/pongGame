import time
from turtle import Turtle


class Ball(Turtle):

    import random

    HEADINGS = [45, 45 + 90, 45 + 90 + 90, 45 + 90 + 90 + 90]

    def __init__(self):
        super().__init__()
        self.clear()
        self.color("white")
        self.penup()
        self.shape("circle")
        self.sety(self.random.randint(-270, 270))
        self.setheading(self.random.choice(self.HEADINGS))

    def move(self):
        self.forward(5)

    def bounce_from_wall(self):
        if self.ycor() > 280:
            if self.heading() == 45:
                self.setheading(315)
            elif self.heading() == 135:
                self.setheading(225)
        elif self.ycor() < -280:
            if self.heading() == 315:
                self.setheading(45)
            elif self.heading() == 225:
                self.setheading(135)

    def bounce_from_paddle(self):
        if self.xcor() > 465:
            if self.heading() == 45:
                self.setheading(135)
            elif self.heading() == 315:
                self.setheading(225)
        elif self.xcor() < -475:
            if self.heading() == 135:
                self.setheading(45)
            elif self.heading() == 225:
                self.setheading(315)

    def reset_ball(self):
        self.goto(0, self.random.randint(-270, 270))
        self.setheading(self.random.choice(self.HEADINGS))
