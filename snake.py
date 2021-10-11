from turtle import Turtle

SNAKE_SEGMENTS = []
DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
segments = 3
pos = 0


class Snake:
    def __init__(self):
        self.create_snake()
        self.snake_head = SNAKE_SEGMENTS[0]

    def create_snake(self):
        global pos
        for _ in range(segments):
            segment = Turtle("square")
            segment.color("white")
            segment.penup()
            segment.goto(pos, 0)
            SNAKE_SEGMENTS.append(segment)
            pos -= 20
        return SNAKE_SEGMENTS

    def move(self):
        for seg in range(len(SNAKE_SEGMENTS) - 1, 0, -1):
            SNAKE_SEGMENTS[seg].showturtle()
            new_x = SNAKE_SEGMENTS[seg - 1].xcor()
            new_y = SNAKE_SEGMENTS[seg - 1].ycor()
            SNAKE_SEGMENTS[seg].goto(new_x, new_y)
        SNAKE_SEGMENTS[0].forward(DISTANCE)

    def snake_incress(self):
        global pos
        pos -= 20
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(pos, 0)
        segment.hideturtle()
        SNAKE_SEGMENTS.append(segment)


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
