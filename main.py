# TODO 1 Create the snake body
import turtle as t
import time

screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Nokia 3310 Snake Game.")
screen.tracer(0)

# TODO 3 Create the shape of the snake by for loop

snake_parts = []
parts_positions = [(0, 0), (-20, 0), (-40, 0)]
for block in range(3):
    snake_body = t.Turtle("square")
    snake_body.penup()
    snake_body.color("white")
    snake_body.goto(parts_positions[block])
    snake_parts.append(snake_body)

screen.listen()


# TODO 2 Create the Snake controller

def move_forward(snake_part):
    snake_part.forward(5)


def turn_left(sha):
    sha.setheading(180)


def turn_right(sha):
    sha.setheading(0)


def turn_down(sha):
    sha.setheading(270)


def turn_up(sha):
    sha.setheading(90)


# TODO 4 Move snake parts forward

while True:
    screen.update()
    time.sleep(0.1)
    for x in range(len(snake_parts)):
        move_forward(snake_parts[x])

screen.onkey(key="w", fun=turn_up)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="s", fun=turn_down)

screen.exitonclick()
