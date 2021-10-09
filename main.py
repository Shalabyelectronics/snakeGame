# TODO 1 Create the snake body
from snake import Snake
from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Nokia 3310 Snake Game.")
screen.tracer(0)

screen.listen()

test = Snake()


def snake_forward():
    screen.update()
    time.sleep(0.1)
    test.snake_animation()
    test.snake_shape[0].forward(20)


# TODO Controler W, S, D, A
def turn_right():
    test.snake_animation()
    test.snake_shape[0].setheading(0)


def turn_up():
    test.snake_animation()
    test.snake_shape[0].setheading(90)


def turn_down():
    test.snake_animation()
    test.snake_shape[0].setheading(270)


def turn_left():
    test.snake_animation()
    test.snake_shape[0].setheading(180)






screen.onkey(key="w", fun=turn_up)
screen.onkey(key="s", fun=turn_down)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="a", fun=turn_left)
screen.onkeypress(key="space", fun=snake_forward)


screen.exitonclick()
