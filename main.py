import turtle
import Paddles


main_screen = turtle.Screen()
main_screen.bgcolor("black")
main_screen.setup(width=800, height=600)
main_screen.title("Pong")
main_screen.tracer(0)

main_screen.listen()
right_paddle = Paddles.Paddles()

main_screen.onkeypress(right_paddle.move_right_paddle_up(main_screen), "Up")

main_screen.exitonclick()