class Playground:
    from turtle import Turtle

    def __init__(self):
        self.create_middle_line()

    def create_middle_line(self):
        for n in range(-285, 300, 20):
            item = self.Turtle(shape="square")
            item.penup()
            item.color("white")
            item.shapesize(.5, .1)
            item.goto(x=0, y=n)
