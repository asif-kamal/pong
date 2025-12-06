import turtle

COORDINATES = ((30, 7), (-30, 7), (-30, -7), (30, -7))


class Paddle(turtle.Turtle):
    def __init__(self):
        super().__init__()
        turtle.register_shape("rectangle", COORDINATES)
        self.penup()
        self.shape("rectangle")
        self.color("white", "white")
        #self.speed(0)


    def move_paddle_up(self, y_change):
        if self.ycor() < 260:
            self.goto(self.xcor(), self.ycor() + y_change)

    def move_paddle_down(self, y_change):
        if self.ycor() > -260:
            self.goto(self.xcor(), self.ycor() - y_change)