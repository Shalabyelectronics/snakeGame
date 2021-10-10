from turtle import Turtle

POSITIONS = [0, -20, -40]
SNAKE_SEGMENTS = []
DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake(Turtle):
    def __init__(self):
        self.snake_shape = self.create_snake()
        self.snake_head = self.snake_shape[0]

    def create_snake(self):
        for seg in range(3):
            segment = Turtle("square")
            segment.color("white")
            segment.penup()
            segment.goto(POSITIONS[seg], 0)
            SNAKE_SEGMENTS.append(segment)
        return SNAKE_SEGMENTS

    def move(self):
        for seg in range(len(self.snake_shape) - 1, 0, -1):
            new_x = self.snake_shape[seg - 1].xcor()
            new_y = self.snake_shape[seg - 1].ycor()
            self.snake_shape[seg].goto(new_x, new_y)
        self.snake_shape[0].forward(DISTANCE)

    # TODO Controler W, S, D, A
    def turn_right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)

    def turn_up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)

    def turn_down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)

    def turn_left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)
