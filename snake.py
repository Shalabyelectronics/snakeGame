from turtle import Turtle


screen = Screen()
POSITIONS = [0, -20, -40]
SNAKE_SEGMENTS = []
DISTANCE = 20


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
            print(self.snake_shape[seg].heading())
        self.snake_shape[0].forward(DISTANCE)
        print(self.snake_shape[0].heading())

    # TODO Controler W, S, D, A
    def turn_right(self):
        self.snake_head.setheading(0)

    def turn_up(self):
        self.snake_head.setheading(90)

    def turn_down(self):
        self.snake_head.setheading(270)

    def turn_left(self):
        self.snake_head.setheading(180)
