from turtle import Turtle


class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.snake_shape = self.snake_body()

    def snake_body(self):
        snake_segments = []
        positions = [0, -20, -40]
        for seg in range(3):
            segment = Turtle("square")
            segment.color("white")
            segment.penup()
            segment.goto(positions[seg], 0)
            snake_segments.append(segment)
        return snake_segments

    def snake_animation(self):
        for seg in range(len(self.snake_shape) - 1, 0, -1):
            new_x = self.snake_shape[seg - 1].xcor()
            new_y = self.snake_shape[seg - 1].ycor()
            self.snake_shape[seg].goto(new_x, new_y)
            # print(f"the seg {seg} and position  {snake_shape[seg].pos()}")
        # self.snake_shape[0].forward(20)
        # print(f"the head {snake_shape[0].pos()}")
