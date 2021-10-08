from turtle import Turtle


class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
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
        snak_parts =self.snake_shape
        for seg in range(len(snak_parts) - 1, 0, -1):
           new_x = snak_parts[seg - 1].xcor()
           new_y = snak_parts[seg - 1].ycor()
           snak_parts[seg].goto(new_x, new_y)
        snak_parts[0].forward(20)



