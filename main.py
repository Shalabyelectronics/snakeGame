# TODO 1 Create the snake body
from snake import Snake
from turtle import Turtle, Screen
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Nokia 3310 Snake Game.")
screen.tracer(0)

test = Snake()

while True:
   screen.update()
   time.sleep(0.1)
   test.snake_animation()

screen.exitonclick()
