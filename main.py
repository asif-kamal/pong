import turtle
import RightPaddle
from LeftPaddle import LeftPaddle

main_screen = turtle.Screen()
main_screen.bgcolor("black")
main_screen.setup(width=800, height=600)
main_screen.title("Pong")

game_is_on = True
right_paddle = RightPaddle.RightPaddle()
left_paddle = LeftPaddle.LeftPaddle()

main_screen.listen()
main_screen.onkey(lambda: right_paddle.move_paddle_up(40), "Up")
main_screen.onkey(lambda: right_paddle.move_paddle_down(40), "Down")
main_screen.onkey(lambda: left_paddle.move_paddle_up(40), "w")
main_screen.onkey(lambda: left_paddle.move_paddle_down(40), "s")

while game_is_on:
    main_screen.update()

main_screen.exitonclick()