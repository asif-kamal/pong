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


    def move_right_paddle_up(self, y_change):
        if self.ycor() < 275:
            self.goto(self.xcor(), self.ycor() + y_change)

    def move_right_paddle_down(self, y_change):
        if self.ycor() > -275:
            self.goto(self.xcor(), self.ycor() - y_change)


