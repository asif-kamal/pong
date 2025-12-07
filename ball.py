import time
import turtle

X = 0.05
Y = 0.04

class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=1)

    def move(self):
        new_x = self.xcor() + X
        new_y = self.ycor() + Y
        self.goto(new_x, new_y)


