# TODO 1 Create the snake body
import turtle as t
import time

screen = t.Screen()
screen.listen()
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


# TODO 2 Create the Snake controller

def move_forward():
    snake_body.forward(5)


def turn_left():
    snake_body.setheading(180)


def turn_right():
    snake_body.setheading(0)


def turn_down():
    snake_body.setheading(270)


def turn_up():
    snake_body.setheading(90)
    print("here")


# TODO 5 Create the border around the snake that will not allow her to go outside it

def snake_border(snake):
    if snake.heading() == 0:
        if snake.xcor() >= 270:
            return False
        else:
            return True
    elif snake.heading() == 90:
        if snake.ycor() >= 280:
            return False
        else:
            return True
    elif snake.heading() == 180:
        if snake.xcor() >= -280:
            return False
        else:
            return True
    elif snake.heading() == 270:
        if snake.ycor() >= -270:
            return False
        else:
            return True
    else:
        return True


# # TODO 4 Move snake parts forward

is_on = True
while is_on:
    screen.update()
    time.sleep(0.1)
    for part in range(len(snake_parts) - 1, 0, -1):
        new_x = snake_parts[part - 1].xcor()
        new_y = snake_parts[part - 1].ycor()
        snake_parts[part].goto(new_x, new_y)
        if not snake_border(snake_parts[part]):
            is_on = False
    snake_parts[0].forward(20)
    snake_parts[0].left(90)

screen.onkey(key="w", fun=turn_up)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="s", fun=turn_down)

screen.exitonclick()
