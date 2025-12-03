import turtle
import Paddles


main_screen = turtle.Screen()
main_screen.bgcolor("black")
main_screen.setup(width=800, height=600)
main_screen.title("Pong")
main_screen.tracer(0)

right_paddle = Paddles.Paddles()

main_screen.update()
main_screen.exitonclick()
