# TODO 1 Create the snake body
import turtle as t

screen = t.Screen()
sha = t.Turtle("square")
sha.color("white")
screen.setup(width=600, height=800)
screen.bgcolor("black")

screen.listen()

def move_forward():
    sha.forward(10)

screen.onkey(key="w", fun=move_forward)

screen.exitonclick()