import time
import turtle
import Paddles


main_screen = turtle.Screen()
main_screen.bgcolor("black")
main_screen.setup(width=800, height=600)
main_screen.title("Pong")

game_is_on = True
right_paddle = Paddles.Paddles()
main_screen.listen()
main_screen.onkey(lambda: right_paddle.move_right_paddle_up(10), "Up")
main_screen.onkey(lambda: right_paddle.move_right_paddle_down(10), "Down")

while game_is_on:
    main_screen.update()

main_screen.exitonclick()