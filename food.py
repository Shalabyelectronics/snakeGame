from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("green")
        self.penup()
        self.turtlesize(1)
        self.shapesize(0.5, 0.5)
        self.food_generator()


    def food_generator(self):
        x = random.randint(-280, 280)
        y = random.randint(-280, 260)
        self.goto(x, y)
