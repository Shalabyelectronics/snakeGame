# TODO 1 Create the snake body
from snake import Snake, segments
from turtle import Screen
from food import Food
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Nokia 3310 Snake Game.")
screen.tracer(0)

screen.listen()
test = Snake()
screen.update()
food = Food()
screen.onkey(key="d", fun=test.turn_right)
screen.onkey(key="w", fun=test.turn_up)
screen.onkey(key="s", fun=test.turn_down)
screen.onkey(key="a", fun=test.turn_left)
print(test.snake_shape)
# x = 0
#
# while x < 200:
#     screen.update()
#     time.sleep(0.1)
#     test.move()
#     # print(test.snake_head.distance(food))
#     if test.snake_head.distance(food) <= 20:
#         food.food_generator()
#         segments += 1
#         print(segments)
#     x += 1


screen.exitonclick()
