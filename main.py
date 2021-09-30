# TODO 1 Create the snake body
import turtle as t

screen = t.Screen()
sha = t.Turtle("square")
sha.color("white")
screen.setup(width=600, height=800)
screen.bgcolor("black")

screen.listen()


# TODO 2 Create the Snake controller

def move_forward():
    sha.forward(10)


def turn_left():
    sha.setheading(180)


def turn_right():
    sha.setheading(0)


def turn_down():
    sha.setheading(270)


def turn_up():
    sha.setheading(90)


screen.onkey(key="w", fun=turn_up)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="s", fun=turn_down)

while True:
    sha.speed(10)
    sha.penup()
    move_forward()

screen.exitonclick()
