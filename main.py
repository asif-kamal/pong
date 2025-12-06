import turtle
import right_paddle
import left_paddle

main_screen = turtle.Screen()
main_screen.bgcolor("black")
main_screen.setup(width=800, height=600)
main_screen.title("Pong")
main_screen.tracer(0)

game_is_on = True
right_paddle = right_paddle.RightPaddle()
left_paddle = left_paddle.LeftPaddle()

main_screen.listen()
main_screen.onkey(lambda: right_paddle.move_paddle_up(50), "Up")
main_screen.onkey(lambda: right_paddle.move_paddle_down(50), "Down")
main_screen.onkey(lambda: left_paddle.move_paddle_up(50), "w")
main_screen.onkey(lambda: left_paddle.move_paddle_down(50), "s")

while game_is_on:
    main_screen.update()

main_screen.exitonclick()