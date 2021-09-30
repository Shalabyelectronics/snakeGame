# TODO 1 Create the snake body
import turtle as t

screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Nokia 3310 Snake Game.")

# TODO 3 Create the shape of the snake by for loop
pos_x = 0

for block in range(3):
    snake_body = t.Turtle("square")
    snake_body.color("white")
    snake_body.setx(pos_x)
    pos_x -= 20



screen.listen()


# TODO 2 Create the Snake controller
#
# def move_forward():
#     sha.forward(10)
#
#
# def turn_left():
#     sha.setheading(180)
#
#
# def turn_right():
#     sha.setheading(0)
#
#
# def turn_down():
#     sha.setheading(270)
#
#
# def turn_up():
#     sha.setheading(90)


# screen.onkey(key="w", fun=turn_up)
# screen.onkey(key="a", fun=turn_left)
# screen.onkey(key="d", fun=turn_right)
# screen.onkey(key="s", fun=turn_down)

# while True:
#     sha.speed(10)
#     sha.penup()
#     move_forward()

screen.exitonclick()
