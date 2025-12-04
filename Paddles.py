import turtle

COORDINATES = ((50, 10), (-50, 10), (-50, -10), (50, -10))
X = 375
Y = 0

class Paddles(turtle.Turtle):
    def __init__(self):
        super().__init__()
        turtle.register_shape("rectangle", COORDINATES)
        self.penup()
        self.goto(X, Y)
        self.shape("rectangle")
        self.color("white", "white")


    def move_right_paddle_up(self, screen):
        if -275 < Y < 275:
            self.goto(X, Y + 20)
            screen.update()

    def move_right_paddle_down(self, screen):
        if -275 < self.y < 275:
            self.goto(X, Y - 10)
            screen.update()


