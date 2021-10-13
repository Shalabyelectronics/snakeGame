from turtle import Turtle

DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
segments = 3
pos = 0


class Snake:
    def __init__(self):
        self.snake_segments = []
        self.create_snake()
        self.snake_head = self.snake_segments[0]

    def create_snake(self):
        global pos
        for _ in range(segments):
            segment = Turtle("square")
            segment.color("white")
            segment.penup()
            segment.goto(pos, 0)
            self.snake_segments.append(segment)
            pos -= 20
        return self.snake_segments

    def move(self):
        for seg in range(len(self.snake_segments) - 1, 0, -1):
            self.snake_segments[seg].showturtle()
            new_x = self.snake_segments[seg - 1].xcor()
            new_y = self.snake_segments[seg - 1].ycor()
            self.snake_segments[seg].goto(new_x, new_y)
        self.snake_segments[0].forward(DISTANCE)

    def snake_incress(self):
        global pos
        pos -= 20
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(pos, 0)
        segment.hideturtle()
        self.snake_segments.append(segment)

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
