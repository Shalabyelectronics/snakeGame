# TODO 1 Create the snake body
from snake import Snake
from turtle import Screen
from food import Food
from scoreboard import Scoreboard
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
score_board = Scoreboard()
score_board.score_refresh()
screen.onkey(key="d", fun=test.turn_right)
screen.onkey(key="w", fun=test.turn_up)
screen.onkey(key="s", fun=test.turn_down)
screen.onkey(key="a", fun=test.turn_left)


x = 0

while x < 2000:
    screen.update()
    time.sleep(0.1)
    test.move()
    # print(test.snake_head.distance(food))
    if test.snake_head.distance(food) <= 15:
        screen.tracer(0)
        test.snake_incress()
        food.food_generator()
        score_board.update_score()
        print(score_board.score)
    x += 1


screen.exitonclick()
