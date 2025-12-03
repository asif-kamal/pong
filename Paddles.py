import turtle

COORDINATES = ((50, 10), (-50, 10), (-50, -10), (50, -10))

class Paddles(turtle.Turtle):
    def __init__(self):
        super().__init__()
        turtle.register_shape("rectangle", COORDINATES)
        self.penup()
        self.goto(375, 0)
        self.shape("rectangle")
        self.color("white", "white")

