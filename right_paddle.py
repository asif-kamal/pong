import paddle

class RightPaddle(paddle.Paddle):
    def __init__(self):
        super().__init__()
        self.goto(380, 0)


