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
    snake_body.setheading(270)
    snake_parts.append(snake_body)
screen.update()


# TODO 2 Create the Snake controller

def move_forward():
    part.forward(5)


def turn_left():
    part.setheading(180)


def turn_right():
    part.setheading(0)


def turn_down():
    part.setheading(270)


def turn_up():
    part.setheading(90)
    print("here")


# TODO 5 Create the border around the snake that will not allow her to go outside it

def snake_border(snake):
    if snake.heading() == 0:
        if snake.xcor() >= 290:
            return False
        else:
            return True
    elif snake.heading() == 90:
        if snake.ycor() == 300:
            return False
        else:
            return True
    elif snake.heading() == 180:
        if snake.xcor() == -300:
            return False
        else:
            return True
    elif snake.heading() == 270:
        if snake.ycor() == -290:
            return False
        else:
            return True
    else:
        return True



# TODO 4 Move snake parts forward
def snake_movement():
    is_on = True
    while is_on:
        screen.update()
        time.sleep(0.1)
        for part in reversed(snake_parts):
            part.forward(10)

            if not snake_border(part):
                is_on = False


snake_movement()
# screen.onkey(key="w", fun=turn_up)
# screen.onkey(key="a", fun=turn_left)
# screen.onkey(key="d", fun=turn_right)
# screen.onkey(key="s", fun=turn_down)

screen.exitonclick()
